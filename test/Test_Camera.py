import unittest
from unittest.mock import MagicMock, patch
from PIL import Image as PILImage
import numpy as np
import sqlite3
import os


class TestCameraApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        file_path = r"C:/Users/layal/OneDrive - University of Jeddah/app with test/camera.py"

        with open(file_path, "r", encoding="utf-8") as file:
            app_code = file.read()

        local_namespace = {}
        exec(app_code, local_namespace)

        cls.CameraApp = local_namespace.get("cameraa")
        cls.PlantForCameraInfoScreen = local_namespace.get("PlantForCameraInfoScreen")
        cls.CameraScreen = local_namespace.get("CameraScreen")

        cls.app = cls.CameraApp()
        cls.app.database_path = "test_bloom_app.db"

        # Create required tables
        conn = sqlite3.connect(cls.app.database_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PlantInformation (
                plant_name TEXT PRIMARY KEY,
                scientific_name TEXT,
                care_instructions TEXT,
                sunlight_requirements TEXT,
                watering_frequency TEXT,
                environment TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS SafePlant (
                plant_name TEXT,
                scientific_name TEXT,
                care_instructions TEXT,
                sunlight_requirements TEXT,
                watering_frequency TEXT,
                environment TEXT,
                added_date TEXT,
                user_id INTEGER,
                PRIMARY KEY (plant_name, user_id)
            )
        """)
        cursor.execute("""
            INSERT OR IGNORE INTO PlantInformation 
            VALUES ('Tomato', 'Solanum lycopersicum', 'Needs regular watering', 'Full Sun', 'Weekly', 'Outdoor')
        """)
        conn.commit()
        conn.close()

    @classmethod
    def tearDownClass(cls):
        if cls.app.conn:
            cls.app.conn.close()
        if os.path.exists(cls.app.database_path):
            os.remove(cls.app.database_path)

    def setUp(self):
        self.app.load_tflite_model = MagicMock()
        self.app.load_dataset = MagicMock(return_value=["Tomato", "Potato"])
        self.app.preprocess_image = MagicMock()
        self.app.run_tflite_inference = MagicMock()

        # Mock root and screens
        self.app.root = MagicMock()
        camera_screen_mock = MagicMock()
        self.app.root.get_screen = MagicMock(return_value=camera_screen_mock)

        # Mock database connection
        self.app.conn = sqlite3.connect(self.app.database_path)
        self.app.cursor = MagicMock()  # Mock cursor

    def test_load_tflite_model(self):
        interpreter = MagicMock()
        with patch("tensorflow.lite.Interpreter", return_value=interpreter):
            result = self.app.load_tflite_model("D:/my_model_quantized.tflite")
            self.assertEqual(result, interpreter)

    def test_preprocess_image(self):
        image = PILImage.new("RGB", (300, 300))
        target_size = (256, 256)

        def mock_resize(size):
            self.assertEqual(size, target_size)
            return image

        image.resize = mock_resize
        self.app.preprocess_image(image, target_size)

    def test_run_tflite_inference(self):
        interpreter = MagicMock()
        img_array = np.random.randint(-128, 127, size=(1, 256, 256, 3), dtype=np.int8)
        interpreter.get_input_details.return_value = [{'index': 0}]
        interpreter.get_output_details.return_value = [{'index': 1}]

        output_mock = np.array([[0.1, 0.9]], dtype=np.float32)
        interpreter.get_tensor = MagicMock(return_value=output_mock)

        result = self.app.run_tflite_inference(interpreter, img_array)
        self.assertTrue(np.array_equal(result, output_mock))

    def test_capture_and_infer(self):
        camera_screen_mock = self.app.root.get_screen.return_value
        camera_screen_mock.ids.camera.texture = MagicMock()
        camera_screen_mock.ids.camera.texture.pixels = b"\x00" * (256 * 256 * 4)
        camera_screen_mock.ids.camera.texture.width = 256
        camera_screen_mock.ids.camera.texture.height = 256

        self.app.run_tflite_inference.return_value = [0, 1]
        self.app.PLANT_NAMES = ["Potato", "Tomato"]

        self.app.capture_and_infer()

        self.app.run_tflite_inference()
        self.assertEqual(self.app.current_prediction, "Tomato")
        

    def test_save_to_safe_plant(self):
        self.app.cursor.execute = MagicMock()  # Mock execute method
        self.app.current_user_id = 1
        self.app.current_plant_info = {
            "plant_name": "Tomato",
            "scientific_name": "Solanum lycopersicum",
            "care_instructions": "Needs regular watering",
            "sunlight_requirements": "Full Sun",
            "watering_frequency": "Weekly",
            "environment": "Outdoor",
            "added_date": "2024-11-25",
        }

        self.app.save_to_safe_plant()
        self.app.cursor.execute(
            "INSERT INTO SafePlant (plant_name, scientific_name, care_instructions, sunlight_requirements, "
            "watering_frequency, environment, added_date, user_id) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                "Tomato",
                "Solanum lycopersicum",
                "Needs regular watering",
                "Full Sun",
                "Weekly",
                "Outdoor",
                "2024-11-25",
                1,
            )
        )


if __name__ == "__main__":
    unittest.main()
