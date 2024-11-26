import sqlite3
from datetime import date
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from PIL import Image as PILImage
import numpy as np
from kivy.core.window import Window
import tensorflow as tf  # Ensure TensorFlow is imported
import os
from kivy.metrics import dp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton  # Required for dialog buttons




Window.size = (350, 600)

# Constants
TFLITE_MODEL_PATH = r"D:/my_model_quantized.tflite"
TARGET_SIZE = (256, 256)
DATASET_PATH = "D:/Dataset"
DATABASE_PATH = r"C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db"

# Kivy Layout
KV = '''
ScreenManager:
    CameraScreen :
    PlantForCameraInfoScreen:

<CameraScreen>:
    name: "camera"
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: 0, 0, 0, dp(50)
            size_hint_y: None
            height: dp(500)

            Camera:
                id: camera
                play: True
                resolution: (640, 480)
                size_hint: (1, None)
                height: dp(300)

            MDLabel:
                id: prediction_label
                text: "Prediction:"
                halign: "center"

            MDRaisedButton:
                text: "Capture Image"
                size_hint: None, None
                size: dp(200), dp(50)
                pos_hint: {"center_x": 0.5}
                md_bg_color: 0.26, 0.62, 0.28, 1
                text_color: 1, 1, 1, 1
                on_release: app.capture_and_infer()

            MDRaisedButton:
                id: show_info_button
                text: "Show Plant Info"
                size_hint: None, None
                size: dp(200), dp(50)
                pos_hint: {"center_x": 0.5}
                md_bg_color: 0.12, 0.47, 0.75, 1
                text_color: 1, 1, 1, 1
                opacity: 0
                on_release: app.show_plant_info()

            MDRaisedButton:
                text: "Quit"
                size_hint: None, None
                size: dp(200), dp(50)
                pos_hint: {"center_x": 0.5}
                md_bg_color: 0.89, 0.32, 0.32, 1
                text_color: 1, 1, 1, 1
                on_release: app.go_back_to_home()

<PlantForCameraInfoScreen>:
    name: "Camera_plant_info"
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)

        MDLabel:
            text: "Plant Information"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Primary"
            size_hint_y: None
            height: dp(40)

        MDSeparator:
            height: dp(1)

        ScrollView:
            do_scroll_x: False

            MDBoxLayout:
                orientation: 'vertical'
                padding: dp(10)
                spacing: dp(10)
                adaptive_height: True

                MDLabel:
                    text: "[b]Scientific Name:[/b]"
                    markup: True
                    font_style: "Subtitle2"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    id: scientific_name
                    text: ""
                    font_style: "Body1"
                    theme_text_color: "Secondary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDSeparator:
                    height: dp(1)

                MDLabel:
                    text: "[b]Care Instructions:[/b]"
                    markup: True
                    font_style: "Subtitle2"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    id: care_instructions
                    text: ""
                    font_style: "Body1"
                    theme_text_color: "Secondary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDSeparator:
                    height: dp(1)

                MDLabel:
                    text: "[b]Sunlight Requirements:[/b]"
                    markup: True
                    font_style: "Subtitle2"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    id: sunlight_requirements
                    text: ""
                    font_style: "Body1"
                    theme_text_color: "Secondary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDSeparator:
                    height: dp(1)

                MDLabel:
                    text: "[b]Watering Frequency:[/b]"
                    markup: True
                    font_style: "Subtitle2"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    id: watering_frequency
                    text: ""
                    font_style: "Body1"
                    theme_text_color: "Secondary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDSeparator:
                    height: dp(1)

                MDLabel:
                    text: "[b]Environment:[/b]"
                    markup: True
                    font_style: "Subtitle2"
                    theme_text_color: "Primary"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    id: environment
                    text: ""
                    font_style: "Body1"
                    theme_text_color: "Secondary"
                    size_hint_y: None
                    height: self.texture_size[1]

        MDRaisedButton:
            text: "Save Plant"
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.12, 0.47, 0.75, 1
            text_color: 1, 1, 1, 1
            on_release: app.save_to_safe_plant()
            
        MDRaisedButton:
            text: "Back to camera"
            size_hint: None, None
            size: dp(200), dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.26, 0.62, 0.28
            text_color: 1, 1, 1, 1
            on_release: app.go_back_to_camera()



            
'''


class CameraScreen(Screen):
    pass

class PlantForCameraInfoScreen(Screen):
    pass



class camera(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user_id = None  # Initialize user ID to None
        self.selected_image_path = None

        
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, email TEXT, password TEXT)")
        self.interpreter = self.load_tflite_model(TFLITE_MODEL_PATH)  # Load the TFLite model
        self.PLANT_NAMES = self.load_dataset(DATASET_PATH)# Load plant names from dataset
        
        self.screen_manager = ScreenManager()

        return Builder.load_string(KV)

    
        


    def capture_and_infer(self):
     try:
        # Access camera widget from the Camera screen
        camera_screen = self.root.get_screen('camera')
        camera_widget = camera_screen.ids.camera

        if not camera_widget.texture:
            raise AttributeError("Camera texture is not available. Ensure that the camera is initialized correctly.")

        # Get the current frame as pixels
        camera_frame = camera_widget.texture.pixels
        pil_image = PILImage.frombytes('RGBA', (camera_widget.texture.width, camera_widget.texture.height), camera_frame)

        # Preprocess the image for the model
        img_array = self.preprocess_image(pil_image, TARGET_SIZE)

        # Run inference
        output_data = self.run_tflite_inference(self.interpreter, img_array)

        # Get the predicted index (highest probability)
        predicted_index = np.argmax(output_data)
        predicted_label = self.PLANT_NAMES[predicted_index]

        # Update the label with the prediction
        camera_screen.ids.prediction_label.text = f"Prediction: {predicted_label}"

        # Store the prediction for use in the save or show plant info methods
        self.current_prediction = predicted_label

        # Make the 'Show Plant Info' button visible
        camera_screen.ids.show_info_button.opacity = 1

     except AttributeError as e:
        print("Error accessing camera texture:", e)
        camera_screen.ids.prediction_label.text = "Error: Camera not initialized"
     except Exception as e:
        print("Unexpected error:", e)
        camera_screen.ids.prediction_label.text = "An unexpected error occurred"

        

    def show_plant_info(self):
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT scientific_name, care_instructions, sunlight_requirements, watering_frequency, environment "
                       "FROM PlantInformation WHERE plant_name = ?", (self.current_prediction,))
        plant_info = cursor.fetchone()
        conn.close()

        if plant_info:
            scientific_name, care_instructions, sunlight, watering, environment = plant_info
            plant_info_screen = self.root.get_screen('Camera_plant_info')
            
            # Set text for each label
            plant_info_screen.ids.scientific_name.text = scientific_name
            plant_info_screen.ids.care_instructions.text = care_instructions
            plant_info_screen.ids.sunlight_requirements.text = sunlight
            plant_info_screen.ids.watering_frequency.text = watering
            plant_info_screen.ids.environment.text = environment

            # Store plant data for saving
            self.current_plant_info = {
                "plant_name": self.current_prediction,
                "scientific_name": scientific_name,
                "care_instructions": care_instructions,
                "sunlight_requirements": sunlight,
                "watering_frequency": watering,
                "environment": environment,
                "added_date": date.today()
            }
        else:
            plant_info_screen = self.root.get_screen('Camera_plant_info')
            plant_info_screen.ids.scientific_name.text = "No information available."
            plant_info_screen.ids.care_instructions.text = ""
            plant_info_screen.ids.sunlight_requirements.text = ""
            plant_info_screen.ids.watering_frequency.text = ""
            plant_info_screen.ids.environment.text = ""
            self.current_plant_info = None

        # Navigate to the plant information screen
        self.root.current = 'Camera_plant_info'

    def save_to_safe_plant(self):
    # Check if plant information is available
     if not hasattr(self, 'current_plant_info') or not self.current_plant_info:
        MDDialog(
            text="No plant information available to save.",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: x.parent.parent.dismiss()
                )
            ],
        ).open()
        return

    # Check if the user is logged in
     if self.current_user_id is None:
        dialog = MDDialog(
            title="Login Required",
            text="Please login or create an account to access this feature.",
            buttons=[
                MDFlatButton(
                    text="LOGIN",
                    on_release=lambda x: self.navigate_to_login(dialog)
                ),
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()
        return  # Prevent further execution if user is not logged in

    # Try to save the plant information
     try:
        # Check if the plant is already saved for the current user
        self.cursor.execute('''
            SELECT * FROM SafePlant WHERE plant_name = ? AND user_id = ?
        ''', (self.current_plant_info["plant_name"], self.current_user_id))
        existing_plant = self.cursor.fetchone()

        if existing_plant:
            dialog = MDDialog(
                text="This plant is already saved in your Profile.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: dialog.dismiss()
                    )
                ],
            )
            dialog.open()
        else:
            # Insert the plant information with the current user's ID
            self.cursor.execute('''
                INSERT INTO SafePlant (plant_name, scientific_name, care_instructions, sunlight_requirements, watering_frequency, environment, added_date, user_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                self.current_plant_info["plant_name"],
                self.current_plant_info["scientific_name"],
                self.current_plant_info["care_instructions"],
                self.current_plant_info["sunlight_requirements"],
                self.current_plant_info["watering_frequency"],
                self.current_plant_info["environment"],
                self.current_plant_info["added_date"],
                self.current_user_id
            ))
            self.conn.commit()
            dialog = MDDialog(
                text=f"Successfully saved {self.current_plant_info['plant_name']}!",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: dialog.dismiss()
                    )
                ],
            )
            
            dialog.open()
            # Optionally, refresh the saved plants list
            self.load_saved_plants()
     except sqlite3.Error as e:
        print(f"An error occurred while saving to SafePlant: {e}")
        MDDialog(
            text="An error occurred while saving the plant. Please try again.",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: x.parent.parent.dismiss()
                )
            ],
        ).open()


 
    def navigate_to_login(self, dialog):
        dialog.dismiss()
        self.root.current = 'log_in'  # Navigate to the login screen

    def load_dataset(self,dataset_path):
     class_names = sorted(os.listdir(dataset_path))
     return class_names

    def load_tflite_model(self,model_path):
     interpreter = tf.lite.Interpreter(model_path=model_path)
     interpreter.allocate_tensors()
     return interpreter

    def preprocess_image(self,image, target_size):
     image = image.resize(target_size)
     image = image.convert("RGB")
     img_array = np.array(image).astype(np.float32) / 255.0
     img_array = np.clip(img_array * 127, -128, 127).astype(np.int8)
     img_array = np.expand_dims(img_array, axis=0)
     return img_array

    def run_tflite_inference(self,interpreter, img_array):
     input_details = interpreter.get_input_details()
     output_details = interpreter.get_output_details()
     interpreter.set_tensor(input_details[0]['index'], img_array)
     interpreter.invoke()
     output_data = interpreter.get_tensor(output_details[0]['index'])
     return output_data

    def go_back_to_camera(self):
        self.last_page = None  # Reset last page to indicate it's the home page
        self.root.current = 'camera'

    
if __name__ == "__main__":
    camera().run()
