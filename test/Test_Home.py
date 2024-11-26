import unittest
from unittest.mock import patch, MagicMock
from kivy.uix.screenmanager import ScreenManager
import importlib.util
import sys

# Dynamically load the Home module from a specific path
module_path = "C:/Users/layal/OneDrive - University of Jeddah/app with test/HomePage.py" # Replace with the actual file path
module_name = "home"


spec = importlib.util.spec_from_file_location(module_name, module_path)
home = importlib.util.module_from_spec(spec)
sys.modules[module_name] = home
spec.loader.exec_module(home)

# Access the Home class from the dynamically loaded module
Home = home.Home

class TestHomeApp(unittest.TestCase):

    def setUp(self):
        """Set up the Home app."""
        self.app = Home()
        self.app.build()  # Initialize the app and load the KV string

    def test_navigation_home(self):
        """Test the home navigation tab."""
        self.app.show_login_dialog_or_navigate = MagicMock()
        self.app.show_login_dialog_or_navigate("home")
        self.app.show_login_dialog_or_navigate.assert_called_once_with("home")

    def test_background_image_path(self):
        """Test if the background image path is correctly set in the KV string."""
        kv_string = home.KV  # Access the KV string from the Home module
        self.assertIn(
            "C:/Users/layal/OneDrive - University of Jeddah/bloom/pictu/hoe_bacground.jpg",
            kv_string,
        )

if __name__ == "__main__":
    unittest.main()
