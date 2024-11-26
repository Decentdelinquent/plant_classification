import unittest
from unittest.mock import patch, MagicMock
import os
from kivy.base import EventLoop
from kivy.core.window import Window
import sys

if not EventLoop.event_listeners:
    from kivy.config import Config
    Config.set('graphics', 'width', '350')
    Config.set('graphics', 'height', '600')
    EventLoop.ensure_window()

file_path = r"C:/Users/layal/OneDrive - University of Jeddah/app with test/store.py"
directory = os.path.dirname(file_path)
if directory not in sys.path:
    sys.path.append(directory)

module_name = os.path.splitext(os.path.basename(file_path))[0]
StorePage = getattr(__import__(module_name), 'StorePage')


class TestStorePage(unittest.TestCase):

    def setUp(self):
        Window.create_window = MagicMock()
        Window.close = MagicMock()

        self.app = StorePage()
        self.app.root = self.app.build()

    @patch("plyer.filechooser.open_file")
    def test_upload_image(self, mock_filechooser):
        mock_filechooser.return_value = ["C:/Users/layal/OneDrive - University of Jeddah/soy.jpg"]
        self.app.upload_image()
        self.assertEqual(self.app.selected_image_path, "C:/Users/layal/OneDrive - University of Jeddah/soy.jpg")
        self.assertEqual(self.app.root.get_screen("estore").ids.user_img.source, "C:/Users/layal/OneDrive - University of Jeddah/soy.jpg")

    @patch("sqlite3.connect")
    def test_on_ok_pressed(self, mock_sqlite_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_sqlite_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        self.app.root.get_screen("estore").ids.product_name.text = "Plant"
        self.app.root.get_screen("estore").ids.size_amount.text = "Medium"
        self.app.root.get_screen("estore").ids.price.text = "15.5"
        self.app.root.get_screen("estore").ids.location.text = "Jeddah"
        self.app.root.get_screen("estore").ids.contact_info.text = "1234567890"
        self.app.selected_image_path = "C:/Users/layal/OneDrive - University of Jeddah/soy.jpg"

        self.app.on_ok_pressed()

        mock_cursor.execute(
            """
            INSERT INTO EStoreProducts (user_id, product_name, size_amount, price, location, contact_info, product_image)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (1, "Plant", "Medium", 15.5, "Jeddah", "1234567890", b"C:/Users/layal/OneDrive - University of Jeddah/soy.jpg")
        )

    @patch("sqlite3.connect")
    @patch("os.makedirs")
    def test_load_products_store(self, mock_makedirs, mock_sqlite_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_sqlite_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [
            (1, "Plant A", "Small", 10.0, "Jeddah", "1234567890", b"FakeImageBytes")
        ]



if __name__ == "__main__":
    unittest.main()
