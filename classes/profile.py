from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
import sqlite3
from kivymd.uix.label import MDLabel

# Set the window size
Window.size = (350, 600)

# Define the KV string for the user interface
KV = '''
ScreenManager:
    ProfileScreen:
    PlantInfoScreen:
    ReminderPageScreen:
    ProductDetailScreen:


                            
<ProfileScreen>:
    name: "profile"
    ScrollView:
        MDBoxLayout:
            id: content_layout
            orientation: 'vertical'
            padding: dp(15)
            spacing: dp(20)
            adaptive_height: True

            # Profile Header Card with Modern Styling
            MDCard:
                id: profile_header
                opacity: 0
                orientation: 'vertical'
                size_hint_y: None
                height: dp(200)  # Adjusted height
                padding: dp(15)
                spacing: dp(8)
                radius: [20,]
                md_bg_color: 0.535, 0.851, 0.608, 1   # Sleek blue  # Updated color for a modern look
                elevation: 10

                BoxLayout:
                    orientation: 'vertical'
                    spacing: dp(10)
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}


                    # Profile Image with Circle Shape and Shadow
                    MDCard:
                        size_hint: None, None
                        size: dp(100), dp(100)  # Larger size for profile image
                        radius: [50,]  # Circular shape
                        md_bg_color: 1, 1, 1, 1
                        pos_hint: {"center_x": 0.5}
                        BoxLayout:
                            

                    # Username and Email with Stylish Fonts and Colors
                    MDLabel:
                        id: username_label
                        text: "Username"
                        font_style: "H5"  # Stylish, larger font for username
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1  # White text color
                        pos_hint: {"center_x": 0.5}

                    MDLabel:
                        id: email_label
                        text: "Email"
                        font_style: "Body1"  # Smaller, sleek font for email
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.9, 0.9, 0.9, 1  # Light gray for a softer look
                        pos_hint: {"center_x": 0.5}

            # Saved Plants Card
            MDCard:
                id: saved_plants
                opacity: 0
                orientation: 'vertical'
                padding: dp(10)
                size_hint_y: None
                height: dp(150)  # Reduced height
                radius: [15,]
                md_bg_color: 0.95, 0.95, 0.95, 1
                elevation: 4

                MDLabel:
                    text: "Saved Plants"
                    font_style: "H6"
                    halign: "left"
                    theme_text_color: "Primary"
                    padding_y: dp(3)

                ScrollView:
                    MDList:
                        id: plant_list

            # Reminders Card
            MDCard:
                id: reminders
                opacity: 0
                orientation: 'vertical'
                padding: dp(10)
                size_hint_y: None
                height: dp(150)  # Reduced height
                radius: [15,]
                md_bg_color: 0.95, 0.95, 0.95, 1
                elevation: 4

                MDLabel:
                    text: "Your Reminders"
                    font_style: "H6"
                    halign: "left"
                    theme_text_color: "Primary"
                    padding_y: dp(3)

                ScrollView:
                    MDList:
                        id: reminder_list

            # Products Card
            MDCard:
                id: products
                opacity: 0
                orientation: 'vertical'
                padding: dp(10)
                size_hint_y: None
                height: dp(150)  # Reduced height
                radius: [15,]
                md_bg_color: 0.95, 0.95, 0.95, 1
                elevation: 4

                MDLabel:
                    text: "Your Products"
                    font_style: "H6"
                    halign: "left"
                    theme_text_color: "Primary"
                    padding_y: dp(3)

                ScrollView:
                    MDList:
                        id: products_list
            MDRaisedButton:
                id: go_home_button
                opacity: 0
                text: "Go Back to Homepage"
                md_bg_color:  0.26, 0.62, 0.28, 1  
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.5
                on_release: app.go_back_to_home()

            MDRaisedButton:
                id: logout_button
                opacity: 0
                text: "Logout"
                md_bg_color: 1, 0.2, 0.2, 1
                text_color: 1, 1, 1, 1
                pos_hint: {"center_x": 0.5}
                size_hint_x: 0.5
                on_release: app.log_out()  # Correctly call log_out method

                
<PlantInfoScreen>:
    name: "plant_info"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Plant Information"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Primary"
            bold: True

        MDCard:
            orientation: "vertical"
            size_hint_y: None
            height: dp(200)
            padding: dp(15)
            spacing: dp(10)
            radius: [15,]
            elevation: 5
            md_bg_color: 0.95, 0.95, 0.95, 1

            MDLabel:
                id: plant_info_label
                text: "No information available."
                font_style: "Subtitle1"
                theme_text_color: "Secondary"
                halign: "left"

        MDRaisedButton:
            text: "Delete Plant"
            md_bg_color: 1, 0, 0, 1
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.5
            on_release: app.delete_plant()

        MDRaisedButton:
            text: "Back to Profile"
            md_bg_color: 0.2, 0.6, 0.2, 1
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.5
            on_release: app.go_back_to_profile()
            

<ReminderPageScreen>:
    name: "reminder_info"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Reminder Information"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Primary"
            bold: True

        MDCard:
            orientation: "vertical"
            size_hint_y: None
            height: dp(200)
            padding: dp(15)
            spacing: dp(10)
            radius: [15,]
            elevation: 5
            md_bg_color: 0.95, 0.95, 0.95, 1

            MDLabel:
                id: reminder_info_label
                text: "Details about the reminder will be displayed here."
                font_style: "Subtitle1"
                theme_text_color: "Secondary"
                halign: "left"

        MDRaisedButton:
            text: "Delete Reminder"
            md_bg_color: 1, 0, 0, 1
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.5
            on_release: app.delete_reminder()

        MDRaisedButton:
            text: "Back to Profile"
            md_bg_color: 0.2, 0.6, 0.2, 1
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.5
            on_release: app.go_back_to_profile()


<ProductDetailScreen>:
    name: "product_detail"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Product Details"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Primary"
            bold: True

        MDCard:
            orientation: "vertical"
            size_hint_y: None
            height: dp(200)
            padding: dp(15)
            spacing: dp(10)
            radius: [15,]
            elevation: 5
            md_bg_color: 0.95, 0.95, 0.95, 1

            MDLabel:
                id: product_name_label
                text: "Product Name: "
                font_style: "Subtitle1"
                theme_text_color: "Secondary"
                halign: "left"

            MDLabel:
                id: product_size_label
                text: "Size Amount: "
                font_style: "Subtitle1"
                theme_text_color: "Secondary"
                halign: "left"

            MDLabel:
                id: product_price_label
                text: "Price: "
                font_style: "Subtitle1"
                theme_text_color: "Secondary"
                halign: "left"

            MDLabel:
                id: product_location_label
                text: "Location: "
                font_style: "Subtitle1"
                theme_text_color: "Secondary"
                halign: "left"

            MDLabel:
                id: contact_info_label
                text: "Contact Info: "
                font_style: "Subtitle1"
                theme_text_color: "Secondary"
                halign: "left"

        MDRaisedButton:
            text: "Delete Product"
            md_bg_color: 1, 0, 0, 1
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.5
            on_release: app.delete_product()

            
        MDRaisedButton:
            text: "Back to Profile"
            md_bg_color: 0.2, 0.6, 0.2, 1
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.5
            on_release: app.go_back_to_profile()
        
       
'''
class ProfileScreen(Screen):
    pass

class PlantInfoScreen(Screen):
    pass

class ReminderPageScreen(Screen):
    pass

class ProductDetailScreen(Screen):
    pass

class ProfilePage(MDApp):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user_id = None  # Initialize user ID to None
        self.logged_in= False 
    

        
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Light"
        self.conn = sqlite3.connect("C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db")  # Ensure this matches your database file
        self.cursor = self.conn.cursor()
        return Builder.load_string(KV)

    def on_start(self):
        self.load_user_profile()
        self.load_saved_plants()
        self.load_reminders()
        self.load_products()
        self.init_scroll_animation()

    def load_user_profile(self):
     if not self.logged_in or self.current_user_id is None:
        return  # If not logged in, do nothing

     try:
        # Fetch username and email associated with the logged-in user
        self.cursor.execute("""
            SELECT username, email 
            FROM Users 
            WHERE user_id = ?;
        """, (self.current_user_id,))
        user = self.cursor.fetchone()

        if user:
            # Update the username and email labels on the profile screen
            username_label = self.root.get_screen('profile').ids.username_label
            email_label = self.root.get_screen('profile').ids.email_label

            username_label.text = f"Username: {user[0]}"
            email_label.text = f"Email: {user[1]}"
        else:
            # If no user is found, display placeholders
            username_label.text = "Username: Guest"
            email_label.text = "Email: Not available"
     except sqlite3.Error as e:
        print(f"Database error while loading profile: {e}")
        MDDialog(text="An error occurred while loading your profile.").open()

        

    def update_profile(self):
     """Update the profile screen with the current user's information."""
     if not self.logged_in or self.current_user_id is None:
        print("No user is currently logged in.")
        return

     try:
        # Fetch username and email from the database for the current user
        self.cursor.execute("""
            SELECT username, email 
            FROM Users 
            WHERE user_id = ?;
        """, (self.current_user_id,))
        user = self.cursor.fetchone()

        if user:
            username_label = self.root.get_screen('profile').ids.username_label
            email_label = self.root.get_screen('profile').ids.email_label

            # Update the profile screen with the fetched username and email
            username_label.text = f"Username: {user[0]}"
            email_label.text = f"Email: {user[1]}"
        else:
            print("User not found in the database.")
     except sqlite3.Error as e:
        print(f"Database error while updating profile: {e}")
        MDDialog(text="An error occurred while updating your profile.").open()

        

    def load_saved_plants(self):
     plant_list = self.root.get_screen('profile').ids.plant_list
     plant_list.clear_widgets()

     try:
        # Fetch plants associated with the logged-in user
        self.cursor.execute("""
            SELECT plant_name 
            FROM SafePlant 
            WHERE user_id = ?;
        """, (self.current_user_id,))
        saved_plants = self.cursor.fetchall()

        if not saved_plants:
            plant_list.add_widget(MDLabel(
                text="No plants saved.",
                halign="center",
                theme_text_color="Hint"
            ))
        else:
            for plant in saved_plants:
                plant_name = plant[0]
                item = OneLineListItem(
                    text=plant_name,
                    on_release=lambda x, plant_name=plant_name: self.view_plant_info(plant_name)
                )
                plant_list.add_widget(item)
     except sqlite3.Error as e:
        print(f"Error loading plants: {e}")
        MDDialog(text="An error occurred while loading plants.").open()

            
 
    def load_reminders(self):
     reminder_list = self.root.get_screen('profile').ids.reminder_list
     reminder_list.clear_widgets()
     

     try:
        # Fetch reminders associated with the logged-in user
        self.cursor.execute("SELECT plant_name, task FROM Reminders WHERE user_id = ?", (self.current_user_id,))
        reminders = self.cursor.fetchall()

        if not reminders:
            reminder_list.add_widget(MDLabel(
                text="No reminders.",
                halign="center",
                theme_text_color="Hint"
            ))
        else:
            for reminder in reminders:
                reminder_text = f"{reminder[0]} - {reminder[1]}"
                item = OneLineListItem(
                    text=reminder_text,
                    on_release=lambda x, reminder_name=reminder_text: self.view_reminder_info(reminder_name)
                )
                reminder_list.add_widget(item)
     except sqlite3.Error as e:
        print(f"Error loading reminders: {e}")
        MDDialog(text="An error occurred while loading reminders.").open()
        

    def load_products(self):
     product_list = self.root.get_screen('profile').ids.products_list
     product_list.clear_widgets()

     try:
        # Fetch products associated with the logged-in user
        self.cursor.execute("SELECT product_name FROM EStoreProducts WHERE user_id = ?", (self.current_user_id,))
        products = self.cursor.fetchall()

        if not products:
            product_list.add_widget(MDLabel(
                text="No products available.",
                halign="center",
                theme_text_color="Hint"
            ))
        else:
            for product in products:
                product_name = product[0]
                item = OneLineListItem(
                    text=product_name,
                    on_release=lambda x, product_name=product_name: self.view_product_info(product_name)
                )
                product_list.add_widget(item)
     except sqlite3.Error as e:
        print(f"Error loading products: {e}")
        MDDialog(text="An error occurred while loading products.").open()

        

    def view_product_info(self, product_name):
     try:
        # Fetch product details for the logged-in user
        self.cursor.execute("""
            SELECT product_name, size_amount, price, location, contact_info 
            FROM EStoreProducts 
            WHERE product_name = ? AND user_id = ?;
        """, (product_name, self.current_user_id))
        product = self.cursor.fetchone()

        if product:
            # Display product details on the ProductDetailScreen
            screen = self.root.get_screen('product_detail')
            screen.ids.product_name_label.text = f"Product Name: {product[0]}"
            screen.ids.product_size_label.text = f"Size Amount: {product[1]}"
            screen.ids.product_price_label.text = f"Price: {product[2]}"
            screen.ids.product_location_label.text = f"Location: {product[3]}"
            screen.ids.contact_info_label.text = f"Contact Info: {product[4]}"
            self.root.current = "product_detail"
        else:
            MDDialog(text="No product information available.").open()

     except sqlite3.Error as e:
        print(f"Error fetching product info: {e}")
        MDDialog(text="An error occurred while fetching product information.").open()

    def delete_product(self):
     # Get the product name from the current product detail screen
     product_name = self.root.get_screen('product_detail').ids.product_name_label.text.replace("Product Name: ", "")

     # Delete the product from the database for the current user
     self.cursor.execute("DELETE FROM EStoreProducts WHERE product_name = ? AND user_id = ?", (product_name, self.current_user_id))
     self.conn.commit()
     

     # Reload the products list in the profile screen
     self.load_products()

     print(f"Product '{product_name}' deleted successfully.")
     self.go_back_to_profile()



            
          
    def delete_plant(self):
     # Get the selected plant name from the plant info screen
     plant_name = self.root.get_screen('plant_info').ids.plant_info_label.text.split("\n")[0].replace("Name: ", "")

     # Delete the plant from the database for the current user
     self.cursor.execute("DELETE FROM SafePlant WHERE plant_name = ? AND user_id = ?", (plant_name, self.current_user_id))
     self.conn.commit()

     # Reload the saved plants list
     self.load_saved_plants()

     print(f"Plant '{plant_name}' deleted successfully.")
     self.go_back_to_profile()
     

    def delete_reminder(self):
    # Get the reminder details from the reminder info screen
     reminder_details = self.root.get_screen('reminder_info').ids.reminder_info_label.text.split("\n")
     plant_name = reminder_details[0].replace("Plant Name: ", "")
     task = reminder_details[1].replace("Task: ", "")

    # Delete the reminder from the database for the current user
     self.cursor.execute("DELETE FROM Reminders WHERE plant_name = ? AND task = ? AND user_id = ?", (plant_name, task, self.current_user_id))
     self.conn.commit()

    # Reload the reminders list
     self.load_reminders()

     print(f"Reminder '{plant_name} - {task}' deleted successfully.")
     self.go_back_to_profile()


    def init_scroll_animation(self):
     animation = Animation(opacity=1, duration=1)
     for widget_id in ['profile_header', 'saved_plants', 'reminders', 'products', 'go_home_button', 'logout_button']:
        widget = self.root.get_screen('profile').ids[widget_id]
        animation.start(widget)
                
    def go_back_to_home(self):
     self.root.current = 'home'   



    def go_back_to_profile(self):
        # Navigate back to the profile screen
        self.root.current = "profile"
        
    def view_plant_info(self, plant_name):
     try:
        # Fetch plant details for the logged-in user
        self.cursor.execute("""
            SELECT plant_name, scientific_name, care_instructions, sunlight_requirements, 
                   watering_frequency, environment 
            FROM SafePlant 
            WHERE plant_name = ? AND user_id = ?;
        """, (plant_name, self.current_user_id))
        plant_info = self.cursor.fetchone()

        if plant_info:
            # Format and display the plant information
            details = (
                f"Name: {plant_info[0]}\n"
                f"Scientific Name: {plant_info[1]}\n"
                f"Care Instructions: {plant_info[2]}\n"
                f"Sunlight Requirements: {plant_info[3]}\n"
                f"Watering Frequency: {plant_info[4]}\n"
                f"Environment: {plant_info[5]}"
            )
        else:
            details = "No information available for this plant."

        self.root.get_screen('plant_info').ids.plant_info_label.text = details
        self.root.current = "plant_info"

     except sqlite3.Error as e:
        print(f"Error fetching plant info: {e}")
        MDDialog(text="An error occurred while fetching plant information.").open()

        

    def view_reminder_info(self, reminder_name):
     try:
        # Split the reminder name to get plant_name and task
        plant_name, task = reminder_name.split(" - ")

        # Fetch reminder details for the logged-in user
        self.cursor.execute("""
            SELECT plant_name, task, frequency, time, notification 
            FROM Reminders 
            WHERE plant_name = ? AND task = ? AND user_id = ?;
        """, (plant_name, task, self.current_user_id))
        reminder = self.cursor.fetchone()

        if reminder:
            details = (
                f"Plant Name: {reminder[0]}\n"
                f"Task: {reminder[1]}\n"
                f"Frequency: {reminder[2]}\n"
                f"Time: {reminder[3]}\n"
                f"Notification: {'On' if reminder[4] else 'Off'}"
            )
        else:
            details = "No reminder information available."

        # Update the label in the ReminderPageScreen with the reminder details
        self.root.get_screen('reminder_info').ids.reminder_info_label.text = details
        self.root.current = "reminder_info"

     except sqlite3.Error as e:
        print(f"Error fetching reminder info: {e}")
        MDDialog(text="An error occurred while fetching reminder information.").open()


    def log_out(self):
     """Log out the user and navigate back to the login screen."""
     self.current_user = None
     self.current_user_id = None
     self.logged_in = False
     self.root.current = 'log_in'  # Navigate back to the login screen
     print("User logged out successfully.")

# Run the app
ProfilePage().run()
