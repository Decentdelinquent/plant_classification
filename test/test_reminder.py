import unittest
from unittest.mock import MagicMock, patch
from kivymd.uix.dialog import MDDialog

class MockRoot:
    class MockID:
        def __init__(self, text="", active=False):
            self.text = text
            self.active = active

    def __init__(self):
        self.ids = type(
            "MockIDs",
            (object,),
            {
                "plant_name_button": self.MockID(text="Select Plant"),
                "remind_me_about_button": self.MockID(text="Select Task"),
                "repeat_frequency_button": self.MockID(text="Select Frequency"),
                "time_input": self.MockID(text=""),
                "time_button": self.MockID(text="Select Time"),  # Added here
                "notification_switch": self.MockID(active=False),
            },
        )()

class TestSetReminder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load the application dynamically."""
        file_path = "C:/Users/layal/OneDrive - University of Jeddah/app with test/reminder.py"
        with open(file_path, "r", encoding="utf-8") as file:
            app_code = file.read()
        local_namespace = {}
        exec(app_code, local_namespace)
        cls.SetReminder = local_namespace.get("SetReminder")

    def setUp(self):
        """Set up a test instance of the application."""
        self.app = self.SetReminder()
        self.app.root = MockRoot()  # Set the mock root
        self.app.plant_menu = MagicMock()  # Mock plant_menu

    def test_save_reminder_missing_fields(self):
        """Test saving a reminder with missing fields."""
        # Ensure all required fields are missing
        self.app.root.ids.plant_name_button.text = "Select Plant"
        self.app.root.ids.remind_me_about_button.text = "Select Task"
        self.app.root.ids.repeat_frequency_button.text = "Select Frequency"
        self.app.root.ids.time_input.text = ""  # Missing time input
        self.app.root.ids.time_button.text = "Select Time"  # Ensure this is empty

        

    def test_set_plant(self):
        """Test setting the plant name."""
        self.app.root.ids.plant_name_button.text = "Select Plant"
        self.app.set_plant("Tomato")
        self.assertEqual(self.app.root.ids.plant_name_button.text, "Tomato")

if __name__ == "__main__":
    unittest.main()
