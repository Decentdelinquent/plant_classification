from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.animation import Animation
from kivymd.uix.behaviors.hover_behavior import HoverBehavior
from kivymd.uix.button import MDFillRoundFlatIconButton
import tensorflow as tf
from kivy.uix.image import Image
from PIL import Image as PILImage
from datetime import date
import os
import numpy as np
import re  # Import the regular expression module
from kivymd.uix.label import MDLabel
import sqlite3


from kivy.core.image import Image as CoreImage
from io import BytesIO
import sqlite3
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.uix.image import Image
import os
from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.screenmanager import Screen

from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDSwitch
import tkinter as tk
from tkinter import messagebox





from kivy.core.image import Image as CoreImage
from io import BytesIO
import sqlite3
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.uix.image import Image
import os
from kivy.uix.widget import Widget
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.screenmanager import Screen

from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from kivy.config import Config


from kivy.uix.image import Image
from plyer import filechooser
from kivymd.toast import toast
import tensorflow.lite as tflite

TFLITE_MODEL_PATH = "D:/my_model_quantized.tflite"

DATASET_PATH =r"D:/Dataset"
DATABASE_PATH = r"C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db"
TARGET_SIZE = (256, 256)  # Replace with your model's expected input size
Window.size = (350, 600)  # Set the window size



kv ='''


ScreenManager:

    EStoreScreen:
        name: "estore"
        

<EStoreScreen>
    BoxLayout:
        orientation: 'vertical'

        MDBoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: dp(50)
            padding: dp(10)
            md_bg_color: 0.9, 0.9, 0.9, 1

            MDLabel:
                text: "Store"
                halign: "center"
                valign: "middle"
                font_style: "Subtitle1"
                theme_text_color: "Primary"

        ScreenManager:
            id: screen_manager

            # Buy Product Page
            Screen:
                name: "buy_screen"
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(50)
                        padding: dp(10)
                        spacing: dp(20)

                        MDFlatButton:
                            text: "Sell Product"
                            on_release: app.change_screen("sell_screen")
                            font_size: "18sp"
                            size_hint_x: 0.5
                            halign: "center"

                        MDFlatButton:
                            text: "Buy Product"
                            on_release: app.change_screen("buy_screen")
                            theme_text_color: "Custom"
                            text_color:0.2, 0.6, 0.2, 1 
                            font_size: "18sp"
                            size_hint_x: 0.5
                            halign: "center"

                    ScrollView:
                        MDBoxLayout:
                            id: product_list
                            orientation: 'vertical'
                            padding: dp(10)
                            spacing: dp(10)
                            size_hint_y: None
                            height: self.minimum_height

            # Sell Product Page
            Screen:
                name: "sell_screen"
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(10)

                    MDBoxLayout:
                        orientation: 'horizontal'
                        size_hint_y: None
                        height: dp(50)
                        padding: dp(10)
                        spacing: dp(5)

                        MDFlatButton:
                            text: "Sell Product"
                            on_release: app.change_screen("sell_screen")
                            theme_text_color: "Custom"
                            text_color: 0.2, 0.6, 0.2, 1 
                            font_size: "18sp"
                            size_hint_x: 0.5
                            halign: "center"

                        MDFlatButton:
                            text: "Buy Product"
                            on_release: app.change_screen("buy_screen")
                            font_size: "18sp"
                            size_hint_x: 0.5
                            halign: "center"

                    ScrollView:
                        do_scroll_x: False
                        do_scroll_y: True
                        bar_width: dp(10)

                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: dp(10)
                            spacing: dp(10)
                            size_hint_y: None
                            height: self.minimum_height

                            BoxLayout:
                                orientation: 'vertical'
                                size_hint_y: None
                                height: dp(370)
                                spacing: dp(10)

                                BoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(50)
                                    MDLabel:
                                        text: "Product Name:"
                                    MDTextField:
                                        id: product_name
                                        hint_text: "Enter product name"
                                        size_hint_x: 1

                                BoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(50)
                                    MDLabel:
                                        text: "Size/Amount:"
                                    MDTextField:
                                        id: size_amount
                                        hint_text: "Enter size/amount"
                                        size_hint_x: 1

                                BoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(50)
                                    MDLabel:
                                        text: "Price:"
                                    MDTextField:
                                        id: price
                                        hint_text: "Enter price"
                                        size_hint_x: 1

                                BoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(50)
                                    MDLabel:
                                        text: "Location:"
                                    MDTextField:
                                        id: location
                                        hint_text: "Enter location"
                                        size_hint_x: 1

                                BoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(50)
                                    MDLabel:
                                        text: "Contact Info:"
                                    MDTextField:
                                        id: contact_info
                                        hint_text: "Enter contact info"
                                        size_hint_x: 1

                                

                            Image:
                                id: user_img
                                source: ""
                                size_hint:None, None
                                width:dp(80)
                                height: dp(80)
                                allow_stretch: True
                                keep_ratio: True

                            MDRaisedButton:
                                text: "Upload Image"
                                on_release: app.upload_image()
                                size_hint_y: None
                                height: dp(50)
                                md_bg_color:0.2, 0.6, 0.2, 1
                                text_color: 1, 1, 1, 1  # Set text color to white

                            MDRaisedButton:
                                text: "OK"
                                on_release: app.on_ok_pressed()
                                size_hint_y: None
                                height: dp(50)
                                md_bg_color:0.2, 0.6, 0.2, 1
                                text_color: 1, 1, 1, 1  # Set text color to white
                                
                                

                            

        MDBoxLayout:
            size_hint_y: 0.15
            panel_color: 0.9, 0.9, 0.9, 1  # Light gray background
            text_color_active: 0.5, 0.5, 0.5, 1  # Neutral gray text color
            selected_color_background: 0, 0, 0, 0  # No background color for selected tab
            unselected_color: 0.5, 0.5, 0.5, 1  # Gray color for unselected icons
            

            MDBottomNavigation:
                MDBottomNavigationItem:
                    icon: "account-circle"
                    text: "Profile"
                    on_tab_press: app.show_login_dialog_or_navigate("profile")

                MDBottomNavigationItem:
                    icon: "camera"
                    text: "Camera"
                    on_tab_press: app.show_login_dialog_or_navigate("camera")

                MDBottomNavigationItem:
                    icon: "home"
                    text: "Home"
                    on_tab_press: app.show_login_dialog_or_navigate("home")

                MDBottomNavigationItem:
                    icon: "storefront"
                    text: "E-store"
                    on_tab_press: app.show_login_dialog_or_navigate("estore")

                MDBottomNavigationItem:
                    icon: "bell-ring-outline"
                    text: "Reminder"
                    on_tab_press: app.show_login_dialog_or_navigate("reminder")
    

'''

class EStoreScreen(Screen):
    pass


class StorePage(MDApp):
        
    dialog = None
    logged_in = False
    db_path = r"C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db"  # Ensure the database is shared with your friend
    image_folder = "C:/Users/layal/OneDrive - University of Jeddah/app with test/product_images"  # Ensure this folder is shared with your friend

   
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user_id = 1  # Initialize user ID to None
        self.selected_image_path = None
        
        
        
          
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, email TEXT, password TEXT)")
        self.screen_manager = ScreenManager()
        
        

        return Builder.load_string(kv)
    
    
    def upload_image(self):
        """Open file chooser to upload an image."""
        file_path = filechooser.open_file(filters=[("Image Files", ".png;.jpg;*.jpeg")])
        if file_path:
            # Display the selected image
            file_path = file_path[0]
            self.root.get_screen('estore').ids.user_img.source = file_path  # Update the image in the UI
            self.selected_image_path = file_path  # Save the selected path
            toast("Image uploaded successfully!")
        else:
            toast("No image selected.")

    def change_screen(self, screen_name):
        self.root.get_screen('estore').ids.screen_manager.current = screen_name
        if screen_name == "buy_screen":
            self.load_products_store()

    def on_ok_pressed(self):
        """Save product details to the database and validate image upload."""
        product_name = self.root.get_screen('estore').ids.product_name.text
        size_amount = self.root.get_screen('estore').ids.size_amount.text
        price = self.root.get_screen('estore').ids.price.text
        location = self.root.get_screen('estore').ids.location.text
        contact_info = self.root.get_screen('estore').ids.contact_info.text

        # Check if all required fields are filled
        if not all([product_name, size_amount, price, location, contact_info]):
            toast("Please fill in all fields")
            return

        # Check if an image is uploaded
        if not self.selected_image_path:
            toast("You must upload an image for the product!")
            return

        try:
            price = float(price)  # Validate price is a number
        except ValueError:
            toast("Price must be a number.")
            return

        # Save the product in the database
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                # Read the image as binary data
                with open(self.selected_image_path, 'rb') as f:
                    product_image_blob = f.read()

                cursor.execute("""
                    INSERT INTO EStoreProducts (user_id, product_name, size_amount, price, location, contact_info, product_image)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (self.current_user_id, product_name, size_amount, price, location, contact_info, product_image_blob))
                conn.commit()

            toast("Product saved successfully!")

            # Clear the input fields
            self.root.get_screen('estore').ids.product_name.text = ""
            self.root.get_screen('estore').ids.size_amount.text = ""
            self.root.get_screen('estore').ids.price.text = ""
            self.root.get_screen('estore').ids.location.text = ""
            self.root.get_screen('estore').ids.contact_info.text = ""
            self.root.get_screen('estore').ids.user_img.source = ""
            self.selected_image_path = None  # Reset the image path

            # Refresh the Sell page
            self.change_screen("sell_screen")
        except Exception as e:
            toast(f"Error saving product: {str(e)}")

    def load_products_store(self):
    # Define the direct database path here
     db_path = "C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db"

    # Clear the existing product list
     self.root.get_screen('estore').ids.product_list.clear_widgets()


    # Ensure the product_images folder exists
     if not os.path.exists(self.image_folder):
        os.makedirs(self.image_folder)

    # Initialize valid_rowids as an empty list
     valid_rowids = []

     with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Fetch all products from the database
        cursor.execute("""
            SELECT rowid, product_name, size_amount, price, location, contact_info, product_image
            FROM EStoreProducts
            ORDER BY rowid DESC
        """)
        products = cursor.fetchall()

        for product in products:
            rowid = product[0]
            valid_rowids.append(rowid)  # Append to valid_rowids to track row IDs
            product_name = product[1]
            size_amount = product[2]
            price = product[3]
            location = product[4]
            contact_info = product[5]
            product_image = product[6]

            # Create a product card
            card = MDCard(
                orientation='vertical',
                size_hint=(0.9, None),
                height=330,
                padding=15,
                spacing=10,
                md_bg_color=(1, 1, 1, 1),
                shadow_softness=6,
                shadow_offset=(1, 1),
                radius=[12, 12, 12, 12],
                elevation=4,
                pos_hint={"center_x": 0.5}
            )

            # Save the image temporarily using rowid for unique identification
            if product_image:
                image_path = f"{self.image_folder}/product_{rowid}.png"
                if not os.path.exists(image_path):  # Avoid re-saving if it exists
                    with open(image_path, "wb") as img_file:
                        img_file.write(product_image)

                img = Image(
                    source=image_path,
                    size_hint=(None, None),
                    size=(120, 120),
                    allow_stretch=True,
                    keep_ratio=True,
                )
                image_box = BoxLayout(
                    orientation="vertical",
                    size_hint=(1, None),
                    height=140,
                    padding=[0, 10, 0, 10],
                )
                img.pos_hint = {"center_x": 0.5}
                image_box.add_widget(img)
                card.add_widget(image_box)

            # Add product details
            details_box = BoxLayout(
                orientation="vertical",
                padding=[10, 0, 10, 10],
                spacing=8
            )

            product_name_label = Label(text=f"[b]Product Name:[/b] {product_name}", halign="left", markup=True, color=(0, 0, 0, 1))
            size_amount_label = Label(text=f"[b]Size/Amount:[/b] {size_amount}", halign="left", markup=True, color=(0, 0, 0, 1))
            price_label = Label(text=f"[b]Price:[/b] {price} SAR", halign="left", markup=True, color=(0, 0, 0, 1))
            location_label = Label(text=f"[b]Location:[/b] {location}", halign="left", markup=True, color=(0, 0, 0, 1))
            contact_info_label = Label(text=f"[b]Contact Info:[/b] {contact_info}", halign="left", markup=True, color=(0, 0, 0, 1))

            details_box.add_widget(product_name_label)
            details_box.add_widget(size_amount_label)
            details_box.add_widget(price_label)
            details_box.add_widget(location_label)
            details_box.add_widget(contact_info_label)

            card.add_widget(details_box)

            # Add the card to the product list
            self.root.get_screen('estore').ids.product_list.add_widget(card)

        # Clean up orphaned image files
        self.cleanup_image_files(valid_rowids)

    def cleanup_image_files(self, valid_rowids):
        # Get all image files in the product_images folder
        folder_path = self.image_folder
        for file_name in os.listdir(folder_path):
            if file_name.startswith("product_") and file_name.endswith(".png"):
                try:
                    # Extract the rowid from the file name
                    file_rowid = int(file_name.replace("product_", "").replace(".png", ""))
                    # If the rowid is not valid, delete the file
                    if file_rowid not in valid_rowids:
                        os.remove(os.path.join(folder_path, file_name))
                except ValueError:
                    # Skip files that do not match the expected naming convention
                    continue


    def on_stop(self):
        # Delete all images in the 'product_images' folder
        folder_path = "C:/Users/layal/OneDrive - University of Jeddah/bloom/product_images"
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if file.startswith("product_images") and file.endswith(".png"):
                os.remove(file_path)


     
       


    



    
    
    
           

if __name__ == '__main__':
   StorePage().run()
