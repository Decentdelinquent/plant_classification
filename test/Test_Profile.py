import unittest
import sqlite3
import importlib.util
from unittest.mock import patch, MagicMock

# Load the ProfilePage class from the specified file path
file_path = "C:/Users/layal/OneDrive - University of Jeddah/app with test/profile.py" # Replace with your actual file path
spec = importlib.util.spec_from_file_location("profile_page", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ProfilePage = module.ProfilePage  # Access the ProfilePage class from the module

class TestProfilePage(unittest.TestCase):

    def setUp(self):
        # Set up a mock ProfilePage instance
        self.app = ProfilePage()
        self.app.current_user_id = 1
        self.app.logged_in = True

        # Use an in-memory SQLite database for testing
        self.app.conn = sqlite3.connect(":memory:")
        self.app.cursor = self.app.conn.cursor()

        # Create mock tables and insert mock data
        self.app.cursor.execute("CREATE TABLE Users (user_id INTEGER, username TEXT, email TEXT)")
        self.app.cursor.execute("CREATE TABLE SafePlant (user_id INTEGER, plant_name TEXT)")
        self.app.cursor.execute("CREATE TABLE Reminders (user_id INTEGER, plant_name TEXT, task TEXT)")
        self.app.cursor.execute("CREATE TABLE EStoreProducts (user_id INTEGER, product_name TEXT)")
        self.app.cursor.execute("INSERT INTO Users VALUES (1, 'TestUser', 'test@example.com')")
        self.app.cursor.execute("INSERT INTO SafePlant VALUES (1, 'TestPlant')")
        self.app.cursor.execute("INSERT INTO Reminders VALUES (1, 'TestPlant', 'Water')")
        self.app.cursor.execute("INSERT INTO EStoreProducts VALUES (1, 'TestProduct')")
        self.app.conn.commit()

        # Mock the app's root attribute and its get_screen method
        self.app.root = MagicMock()
        self.app.root.get_screen = MagicMock()
        mock_screen = MagicMock()
        self.app.root.get_screen.return_value = mock_screen

        # Mock IDs within each screen
        mock_screen.ids = MagicMock()

    def tearDown(self):
        # Close the database connection
        self.app.conn.close()

    def test_load_user_profile(self):
        # Mock the username_label and email_label IDs for the profile screen
        mock_screen = self.app.root.get_screen.return_value
        mock_screen.ids.username_label.text = ""
        mock_screen.ids.email_label.text = ""

        # Call the method
        self.app.load_user_profile()

        # Check the mocked labels were updated
        self.assertEqual(mock_screen.ids.username_label.text, "Username: TestUser")
        self.assertEqual(mock_screen.ids.email_label.text, "Email: test@example.com")

    def test_load_saved_plants(self):
        # Mock the plant_list ID for the profile screen
        mock_screen = self.app.root.get_screen.return_value
        mock_screen.ids.plant_list.clear_widgets = MagicMock()
        mock_screen.ids.plant_list.add_widget = MagicMock()

        # Call the method
        self.app.load_saved_plants()

        # Verify that a widget was added
        mock_screen.ids.plant_list.add_widget.assert_called()

    def test_load_reminders(self):
        # Mock the reminder_list ID for the profile screen
        mock_screen = self.app.root.get_screen.return_value
        mock_screen.ids.reminder_list.clear_widgets = MagicMock()
        mock_screen.ids.reminder_list.add_widget = MagicMock()

        # Call the method
        self.app.load_reminders()

        # Verify that a widget was added
        mock_screen.ids.reminder_list.add_widget.assert_called()

    def test_load_products(self):
        # Mock the products_list ID for the profile screen
        mock_screen = self.app.root.get_screen.return_value
        mock_screen.ids.products_list.clear_widgets = MagicMock()
        mock_screen.ids.products_list.add_widget = MagicMock()

        # Call the method
        self.app.load_products()

        # Verify that a widget was added
        mock_screen.ids.products_list.add_widget.assert_called()

    def test_delete_product(self):
        # Mock the product_name_label ID for the product_detail screen
        mock_screen = self.app.root.get_screen.return_value
        mock_screen.ids.product_name_label.text = "Product Name: TestProduct"

        # Call the method
        self.app.delete_product()

        # Verify the product was deleted from the database
        self.app.cursor.execute("SELECT * FROM EStoreProducts WHERE product_name = 'TestProduct'")
        product = self.app.cursor.fetchone()
        self.assertIsNone(product)

    def test_delete_plant(self):
        # Mock the plant_info_label ID for the plant_info screen
        mock_screen = self.app.root.get_screen.return_value
        mock_screen.ids.plant_info_label.text = "Name: TestPlant"

        # Call the method
        self.app.delete_plant()

        # Verify the plant was deleted from the database
        self.app.cursor.execute("SELECT * FROM SafePlant WHERE plant_name = 'TestPlant'")
        plant = self.app.cursor.fetchone()
        self.assertIsNone(plant)

    def test_delete_reminder(self):
        # Mock the reminder_info_label ID for the reminder_info screen
        mock_screen = self.app.root.get_screen.return_value
        mock_screen.ids.reminder_info_label.text = "Plant Name: TestPlant\nTask: Water"

        # Call the method
        self.app.delete_reminder()

        # Verify the reminder was deleted from the database
        self.app.cursor.execute("SELECT * FROM Reminders WHERE plant_name = 'TestPlant' AND task = 'Water'")
        reminder = self.app.cursor.fetchone()
        self.assertIsNone(reminder)


            

if __name__ == '__main__':
    unittest.main()
