import unittest
from unittest.mock import MagicMock, patch
import sqlite3
import importlib.util
import sys
from kivy.uix.screenmanager import ScreenManager  # Import ScreenManager

import coverage
# Dynamically load the login_signup module from a specific path
module_path = "C:/Users/layal/OneDrive - University of Jeddah/app with test/login_signup.py" # Replace this with your actual file path
module_name = "login_signup"

spec = importlib.util.spec_from_file_location(module_name, module_path)
login_signup = importlib.util.module_from_spec(spec)
sys.modules[module_name] = login_signup
spec.loader.exec_module(login_signup)

# Access the Login class from the dynamically loaded module
Login = login_signup.Login

class TestBloomApp(unittest.TestCase):

    def setUp(self):
     """Set up the Login app with an in-memory database for testing."""
     self.app = Login()
     self.app.conn = sqlite3.connect(":memory:")  # Use an in-memory database
     self.app.cursor = self.app.conn.cursor()
     self.app.cursor.execute(
        "CREATE TABLE users (username TEXT PRIMARY KEY, email TEXT, password TEXT)"
    )
     self.app.cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
        ("test_user", "test@example.com", "password123")
    )
     self.app.conn.commit()

    # Mock the Kivy root and screen manager
     self.app.root = MagicMock(spec=ScreenManager)
     self.login_screen = MagicMock()
     self.signup_screen = MagicMock()
     self.app.root.get_screen.side_effect = lambda screen_name: (
        self.login_screen if screen_name == "log_in" else self.signup_screen
    )

    # Mock input fields
     self.login_screen.ids = {
        "login_username": MagicMock(text=""),
        "login_password": MagicMock(text=""),
    }
     self.signup_screen.ids = {
        "username": MagicMock(text=""),
        "email": MagicMock(text=""),
        "password": MagicMock(text=""),
    }
    def test_valid_login(self):
        """Test login with valid credentials."""
        self.login_screen.ids["login_username"].text = "test_user"
        self.login_screen.ids["login_password"].text = "password123"

        with patch("builtins.print") as mocked_print:
            self.app.log_in()

        self.app.root.current = "profile"  # Ensure navigation to profile screen
        mocked_print.assert_any_call("Logged in user ID: test_user")

    def test_invalid_login(self):
        """Test login with invalid credentials."""
        self.login_screen.ids["login_username"].text = "invalid_user"
        self.login_screen.ids["login_password"].text = "wrong_password"

        with patch("kivymd.uix.dialog.MDDialog.open") as mocked_dialog:
            self.app.log_in()

        mocked_dialog.assert_called_once()  # Ensure error dialog is shown

    def test_sign_up_existing_user(self):
        """Test sign-up with an existing username or email."""
        self.signup_screen.ids["username"].text = "test_user"
        self.signup_screen.ids["email"].text = "test@example.com"
        self.signup_screen.ids["password"].text = "password123"

        with patch("kivymd.uix.dialog.MDDialog.open") as mocked_dialog:
            self.app.sign_up()

        mocked_dialog.assert_called_once_with()

    def test_sign_up_new_user(self):
        """Test sign-up with a new username and email."""
        self.signup_screen.ids["username"].text = "new_user"
        self.signup_screen.ids["email"].text = "new@example.com"
        self.signup_screen.ids["password"].text = "newpassword"

        self.app.sign_up()

        # Verify the new user is added to the database
        self.app.cursor.execute(
            "SELECT * FROM users WHERE username = ?", ("new_user",)
        )
        user = self.app.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[0], "new_user")
        self.assertEqual(user[1], "new@example.com")

    def test_email_validation(self):
        """Test sign-up with invalid email format."""
        self.signup_screen.ids["username"].text = "invalid_user"
        self.signup_screen.ids["email"].text = "invalid_email"
        self.signup_screen.ids["password"].text = "password123"

        with patch("kivymd.uix.dialog.MDDialog.open") as mocked_dialog:
            self.app.sign_up()

        mocked_dialog.assert_called_once()  # Ensure error dialog is shown

    def test_empty_fields(self):
        """Test sign-up with empty fields."""
        self.signup_screen.ids["username"].text = ""
        self.signup_screen.ids["email"].text = ""
        self.signup_screen.ids["password"].text = ""

        with patch("kivymd.uix.dialog.MDDialog.open") as mocked_dialog:
            self.app.sign_up()

        mocked_dialog.assert_called_once()  # Ensure error dialog is shown

    def test_continue_as_guest(self):
        """Test the 'Continue as Guest' functionality."""
        self.app.continue_as_guest()
        self.assertEqual(self.app.root.current, "home")  # Ensure navigation to home screen

    

    def tearDown(self):
        """Close the database connection."""
        self.app.conn.close()

    

if __name__ == "__main__":
    unittest.main()
    
