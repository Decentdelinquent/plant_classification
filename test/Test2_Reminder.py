import unittest
from unittest.mock import MagicMock, patch
import os

# Define a mock root with all necessary attributes
class MockRoot:
    """Mock the root and its IDs for testing."""
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
                "time_button": self.MockID(text="Select Time"),  # Add missing time_button
                "notification_switch": self.MockID(active=False),
            },
        )()

class TestSetReminder(unittest.TestCase):
    """Unit tests for the SetReminder class."""

    @classmethod
    def setUpClass(cls):
        """Load the application dynamically."""
        # Update this path to your file location
        file_path = r"C:/Users/layal/OneDrive - University of Jeddah/app with test/reminder.py"
        with open(file_path, "r", encoding="utf-8") as file:
            app_code = file.read()
        local_namespace = {}
        exec(app_code, local_namespace)
        cls.SetReminder = local_namespace.get("SetReminder")

    def setUp(self):
      """Set up a test instance of the application."""
      self.app = self.SetReminder()
      self.app.root = MockRoot()  # Use the mocked root
      self.app.current_user_id = 1  # Mock a logged-in user
      self.app.conn = MagicMock()  # Mock database connection
      self.app.cursor = MagicMock()  # Mock database cursor
      self.app.plant_menu = MagicMock()  # Mock plant_menu
      self.app.reminder_task_menu = MagicMock()  # Mock reminder_task_menu
      self.app.repeat_menu = MagicMock()  # Mock repeat_menu

 

    def test_save_reminder_missing_fields(self):
        """Test saving a reminder with missing fields."""
        # Ensure all required fields are missing
        self.app.root.ids.plant_name_button.text = "Select Plant"
        self.app.root.ids.remind_me_about_button.text = "Select Task"
        self.app.root.ids.repeat_frequency_button.text = "Select Frequency"
        self.app.root.ids.time_input.text = ""

      

    def test_save_reminder_valid_fields(self):
        """Test saving a reminder with all fields provided."""
        # Provide valid data for all fields
        self.app.root.ids.plant_name_button.text = "Tomato"
        self.app.root.ids.remind_me_about_button.text = "Watering"
        self.app.root.ids.repeat_frequency_button.text = "Daily"
        self.app.root.ids.time_input.text = "08:00 AM"

    def test_set_plant(self):
        """Test setting the plant name."""
        self.app.root.ids.plant_name_button.text = "Select Plant"
        self.app.set_plant("Tomato")
        self.assertEqual(self.app.root.ids.plant_name_button.text, "Tomato")

    def test_set_task(self):
        """Test setting the task name."""
        self.app.root.ids.remind_me_about_button.text = "Select Task"
        self.app.set_task("Watering")
        self.assertEqual(self.app.root.ids.remind_me_about_button.text, "Watering")

    def test_set_repeat(self):
        """Test setting the repeat frequency."""
        self.app.root.ids.repeat_frequency_button.text = "Select Frequency"
        self.app.set_repeat("Daily")
        self.assertEqual(self.app.root.ids.repeat_frequency_button.text, "Daily")

if __name__ == "__main__":
    unittest.main()
