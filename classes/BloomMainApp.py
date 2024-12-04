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

TFLITE_MODEL_PATH = "C:/Users/layal/Downloads/my_model_quantized.tflite"

DATASET_PATH ="D:/Dataset"
DATABASE_PATH = "C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db"
TARGET_SIZE = (256, 256)  # Replace with your model's expected input size
Window.size = (350, 600)  # Set the window size




KV = '''
ScreenManager:

    WelcomeScreen:
        name: "welcome"

    NextScreen:
        name: "home"
    LoginScreen:
        name: "log_in"
    SignUpScreen:
        name: "sign_up"

    ReminderScreen:
        name: "reminder"
    EStoreScreen:
        name: "estore"
   
   
    ProfileScreen:
        name: "profile"
    PlantInfoScreen:
        name: "plant_info"
    ReminderPageScreen:
        name: "reminder_info"
    ProductDetailScreen:
        name: "product_detail"
    CameraScreen:  
        name: "camera"
    PlantForCameraInfoScreen
        name: "Camera_plant_info"
    
    
       
############### log in kv#########################


    
<LoginScreen>:
    name: 'log_in'
    canvas.before:
        Rectangle:
            source:"C:/Users/Sky/OneDrive - University of Jeddah/bloom app interface/pictu/sin and log in background.jpg"
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(15)
        padding: dp(20)

        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: dp(200)
            spacing: dp(8)
            padding: dp(10)

            Image:
                source: "C:/Users/Sky/OneDrive - University of Jeddah/bloom app interface/pictu/bloom_logo.jpg"
                allow_stretch: True
                keep_ratio: True
                size_hint_y: None
                height: dp(120)
                pos_hint: {"center_x": 0.5}

            MDLabel:
                text: "Welcome to Bloom"
                halign: "center"
                font_style: "H5"
                theme_text_color: "Secondary"
                text_color: 0.2, 0.6, 0.3, 1
                pos_hint: {"center_y": 0.55}

        MDTextField:
            id: login_username
            hint_text: "Username"
            icon_right: "account"
            mode: "rectangle"
            size_hint_x: 0.85
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.95, 0.95, 0.95, 1
            line_color_focus: 0.3, 0.7, 0.4, 1
            color_mode: 'accent'
            font_size: "16sp"

        MDTextField:
            id: login_password
            hint_text: "Password"
            icon_right: "lock"
            mode: "rectangle"
            size_hint_x: 0.85
            pos_hint: {"center_x": 0.5}
            password: True
            md_bg_color: 0.95, 0.95, 0.95, 1
            line_color_focus: 0.3, 0.7, 0.4, 1
            color_mode: 'accent'
            font_size: "16sp"

        MDRaisedButton:
            text: "Log In"
            size_hint_x: 0.75
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.2, 0.6, 0.2, 1
            text_color: 1, 1, 1, 1
            font_size: "18sp"
            elevation: 0
            on_release: app.log_in()

        MDLabel:
            text: "[color=339966]Don't have an account?[/color] [ref=create][color=339966][u]Create an account[/u][/color][/ref]"
            halign: "center"
            pos_hint: {"center_y": 0.25}
            theme_text_color: "Custom"
            markup: True
            font_size:"15sp"
            on_ref_press: app.go_to_sign_up()


             # New label for "Continue as Guest" link with higher position and ID for animation
        MDLabel:
            id: guest_label
            text: "[ref=guest][color=339966][u]Continue as Guest[/u][/color][/ref]"
            halign: "center"
            pos_hint: {"center_y": 0.25}  # Move it a bit higher
            theme_text_color: "Custom"
            markup: True
            font_size: "15sp"
            on_ref_press: app.go_to_home()


            

#########################3 sign up kv####################3




<SignUpScreen>:
    name: 'sign_up'
    MDFloatLayout:
        Image:
            source: "C:/Users/Sky/OneDrive - University of Jeddah/bloom app interface/pictu/sin and log in background.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        Image:
            source: "C:/Users/Sky/OneDrive - University of Jeddah/bloom app interface/pictu/bloom_logo.jpg"
            allow_stretch: True
            keep_ratio: True
            size_hint: None, None
            size: dp(200), dp(150)
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}

        MDLabel:
            text: "Begin your bloom journey"
            halign: 'center'
            font_size: '18sp'
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.70}

        MDTextField:
            id: username
            hint_text: "Username"
            icon_right: "account"
            mode: "rectangle"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.6}

        MDTextField:
            id: email
            hint_text: "Email Address"
            icon_right: "email"
            mode: "rectangle"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDTextField:
            id: password
            hint_text: "Password"
            icon_right: "lock"
            password: True
            mode: "rectangle"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.4}

        MDRaisedButton:
            text: "Sign Up"
            size_hint_x: 0.7
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            text_color: 1, 1, 1, 1
            on_release: app.sign_up()

        MDLabel:
            text: "[color=339966]Have an account?[/color] [ref=create][color=339966][u]Log-in[/u][/color][/ref]"
            halign: "center"
            pos_hint: {"center_y": 0.2}
            theme_text_color: "Custom"
            markup: True
            on_ref_press: app.go_to_login()
            

<NextScreen>:
    canvas.before:
        Rectangle:
            source: "C:/Users/Sky/OneDrive - University of Jeddah/bloom app interface/pictu/hoe_bacground.jpg"
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(10)
        spacing: dp(20)
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_y: None
        height: self.minimum_height

        MDLabel:
            text: "Welcome to Bloom"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            font_style: "H5"
            bold: True
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text: "Where you can exchange resources with other users, save your plants, and set watering reminders."
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            font_style: "Body1"
            size_hint_y: None
            height: self.texture_size[1]

    MDBottomNavigation:
        size_hint_y: 0.15
        panel_color: 0.9, 0.9, 0.9, 1  # Light gray background
        text_color_active: 0.5, 0.5, 0.5, 1  # Neutral gray text color
        selected_color_background: 0, 0, 0, 0  
        unselected_color: 0.5, 0.5, 0.5, 1  # Gray color for unselected icons

        MDBottomNavigationItem:
            
            icon: "account-circle"
            text: "Profile"
            on_tab_press: app.show_login_dialog_or_navigate("profile")

        MDBottomNavigationItem:
            name: "camera"
            icon: "camera"
            text: "Camera"
            on_tab_press: app.show_login_dialog_or_navigate("camera")

        MDBottomNavigationItem:
            name: "home"
            icon: "home"
            text: "Home"

        MDBottomNavigationItem:
            name: "estore"
            icon: "store"
            text: "E-store"
            on_tab_press: app.show_login_dialog_or_navigate("estore")

        MDBottomNavigationItem:
            name: "reminder"
            icon: "bell-ring"
            text: "Reminder"
            on_tab_press: app.show_login_dialog_or_navigate("reminder")

            


####################### profile kv ##########################################


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
                md_bg_color: 0.535, 0.851, 0.608, 1   # Sleek green
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
                        md_bg_color: 1, 1, 1, 1  # Background color
                        pos_hint: {"center_x": 0.5}
                        elevation: 4
                        BoxLayout:
                            canvas.before:
                                Color:
                                    rgba: 1, 1, 1, 1  # White background
                                Ellipse:
                                    size: self.size
                                    pos: self.pos
                            Image:
                                id: profile_image
                                source: "C:/Users/layal/OneDrive/سطح المكتب/profile2.png"
                                size_hint: None, None
                                size: dp(100), dp(100)
                                allow_stretch: True
                                keep_ratio: True
                                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        
                            

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
                on_release: app.log_out()
                

                
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




##### camera kv###########################3


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





<ReminderScreen>:
    name: "reminder"
    canvas.before:
        Color:
            rgba: 0.95 , 0.95,0.95,1  # Light gray background
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'

        # Header Card without gradient and smaller text
        BoxLayout:
            size_hint_y: None
            height: dp(60)
            padding: dp(10)
            spacing: dp(10)
            pos_hint: {"center_x": 0.5}

            MDLabel:
                text:  "Set Reminder" 
                halign: "center"
                theme_text_color: "Custom"
                text_color: 0.1, 0.3, 0.1, 1  # Soft dark green
                font_style: "H6"  # Smaller font style
                bold: True
                markup: True

        ScrollView:
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                orientation: "vertical"
                padding: dp(20), dp(20), dp(20), dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height
                md_bg_color: 1, 1, 1, 0.95
                radius: [20, 20, 20, 20]  # Rounded corners

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(10)

                    MDLabel:
                        text: "Plant Name"
                        halign: "left"
                        size_hint_x: 0.4
                        font_size: "15sp"
                        theme_text_color: "Hint"

                    MDRoundFlatButton:
                        id: plant_name_button
                        text: "Select Plant"
                        size_hint_x: 0.6
                        font_size: "15sp"
                        on_release: app.plant_menu.open()

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(10)

                    MDLabel:
                        text: "Remind Me About"
                        halign: "left"
                        size_hint_x: 0.4
                        font_size: "15sp"
                        theme_text_color: "Hint"

                    MDRoundFlatButton:
                        id: remind_me_about_button
                        text: "Select Task"
                        size_hint_x: 0.6
                        font_size: "15sp"
                        on_release: app.reminder_task_menu.open()

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(50)
                    spacing: dp(10)

                    MDLabel:
                        text: "Frequency"
                        halign: "left"
                        size_hint_x: 0.4
                        font_size: "15sp"
                        theme_text_color: "Hint"

                    MDRoundFlatButton:
                        id: repeat_frequency_button
                        text: "Select Frequency"
                        size_hint_x: 0.6
                        font_size: "15sp"
                        on_release: app.repeat_menu.open()

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)

                    MDLabel:
                        text: "Time"
                        halign: "left"
                        size_hint_x: 0.4
                        font_size: "15sp"
                        theme_text_color: "Hint"

                    MDTextField:
                        id: time_input
                        hint_text: "Enter Time"
                        size_hint_x: 0.6
                        height: dp(45)
                        font_size: "15sp"
                        mode: "rectangle"

                BoxLayout:
                    orientation: 'horizontal'
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)

                    MDLabel:
                        id: enable_label
                        text: "Enable Notification"
                        halign: "left"
                        size_hint_x: 0.4
                        font_size: "15sp"
                        theme_text_color: "Hint"

                    MDSwitch:
                        id: notification_switch
                        size_hint: None, None
                        size: dp(60), dp(40)
                        pos_hint: {"center_y": 0.5}
                        on_active: app.toggle_notification(self, self.active)

                MDRaisedButton:
                    text: "Save Reminder"
                    pos_hint: {"center_x": 0.5}
                    size_hint: None, None
                    size: dp(180), dp(50)
                    md_bg_color:0.2, 0.6, 0.2, 1
                    text_color: 1, 1, 1, 1
                    font_size: "16sp"
                    on_release: app.save_reminder()

                    

        MDBottomNavigation:
            size_hint_y: 0.15
            panel_color: 0.9, 0.9, 0.9, 1  # Light gray background
            text_color_active: 0.5, 0.5, 0.5, 1  # Neutral gray text color
            selected_color_background: 0, 0, 0, 0  # No background color for selected tab
            unselected_color: 0.5, 0.5, 0.5, 1  # Gray color for unselected icons

            MDBottomNavigation:
                size_hint_y: 0.15
                panel_color: 0.9, 0.9, 0.9, 1  # Light gray background
                text_color_active: 0.5, 0.5, 0.5, 1  # Neutral gray text color
                selected_color_background: 0, 0, 0, 0  # No background color for selected tab
                unselected_color: 0.5, 0.5, 0.5, 1  # Gray color for unselected icons
            
               
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
                    icon: "store"
                    text: "E-store"
                    on_tab_press: app.show_login_dialog_or_navigate("estore")

                MDBottomNavigationItem:
                    icon: "bell-ring"
                    text: "Reminder"
                    on_tab_press: app.show_login_dialog_or_navigate("reminder")
    
 



<EStoreScreen>:
    name: 'estore'
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



        MDBottomNavigation:
            size_hint_y: 0.15
            panel_color: 0.9, 0.9, 0.9, 1  # Light gray background
            text_color_active: 0.5, 0.5, 0.5, 1  # Neutral gray text color
            selected_color_background: 0, 0, 0, 0  # No background color for selected tab
            unselected_color: 0.5, 0.5, 0.5, 1  # Gray color for unselected icons
            

            MDBottomNavigation:
                size_hint_y: 0.15
                panel_color: 0.9, 0.9, 0.9, 1  # Light gray background
                text_color_active: 0.5, 0.5, 0.5, 1  # Neutral gray text color
                selected_color_background: 0, 0, 0, 0  # No background color for selected tab
                unselected_color: 0.5, 0.5, 0.5, 1  # Gray color for unselected icons
            
            
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
                    icon: "store"
                    text: "E-store"
                    on_tab_press: app.show_login_dialog_or_navigate("estore")

                MDBottomNavigationItem:
                    icon: "bell-ring"
                    text: "Reminder"
                    on_tab_press: app.show_login_dialog_or_navigate("reminder")
    
 

                                
                                

                            

        



            
'''


class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass

class NextScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class PlantInfoScreen(Screen):
    pass

class ReminderPageScreen(Screen):
    pass

class ProductDetailScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class PlantForCameraInfoScreen(Screen):
    pass

class ReminderScreen(Screen):
    pass

class EStoreScreen(Screen):
    pass




class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.add_background_video()
        self.add_logo()
        self.add_get_started_button()
        self.add_widget(self.layout)

    def add_background_video(self):
        video_path = "C:/Users/layal/OneDrive - University of Jeddah/bloom/videos/vid2.mp4"
        self.video = Video(
            source=video_path,
            state='play',
            options={'eos': 'loop'},
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.layout.add_widget(self.video)

    def add_logo(self):
        self.logo = Image(
            source="C:/Users/Sky/Downloads/WhatsApp Image 2024-11-26 at 10.09.48 PM.jpeg",
            size_hint=(0.5, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.75}
        )
        self.layout.add_widget(self.logo)

    def add_get_started_button(self):
        self.get_started_button = MDRaisedButton(
            text='Get Started',
            size_hint=(0.5, 0.08),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            md_bg_color=(0.2, 0.6, 0.2, 1),
            text_color=(1, 1, 1, 1),
            font_size='18sp',
            elevation=0
        )
        self.get_started_button.bind(on_press=self.go_to_next_screen)
        self.layout.add_widget(self.get_started_button)

    def go_to_next_screen(self, instance):
        self.manager.current = 'log_in'





class BloomApp(MDApp):
    dialog = None
    logged_in = False
    current_prediction = None
    current_plant_info = None
    db_path = "C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db"  # Ensure the database is shared with your friend
    image_folder = "C:/Users/layal/OneDrive - University of Jeddah/bloom/product_images"  # Ensure this folder is shared with your friend

   

    
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

    
    def show_login_dialog_or_navigate(self, target_screen):
     """Allow free access to the Camera page but require login for other pages."""
     if target_screen == "camera":
        self.root.current = target_screen  # Allow access to Camera without login
     elif self.logged_in:
        self.root.current = target_screen  # Allow access to other pages if logged in
     else:
        # Show login dialog for other restricted pages
        if not self.dialog:
            self.dialog = MDDialog(
                text="Please login or create an account to access this feature.",
                buttons=[
                    MDFlatButton(
                        text="LOGIN",
                        on_release=lambda x: self.navigate_to("log_in")
                    ),
                    MDFlatButton(
                        text="CANCEL",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.open()

        
    def log_in(self):
     login_username = self.root.get_screen('log_in').ids.login_username.text
     login_password = self.root.get_screen('log_in').ids.login_password.text

     try:
        # Query to check if the user exists
        self.cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", 
                            (login_username, login_password))
        user = self.cursor.fetchone()

        if user:
            self.current_user = {
                "user_id": user[0],
                "username": user[1],
                "email": user[2]
            }
            self.current_user_id = user[0]  # Set the current user ID
            print(f"Logged in user ID: {self.current_user_id}")  # Debugging
            self.logged_in = True  # Mark as logged in

            # Load profile and related data
            self.update_profile()
            self.load_saved_plants()
            self.load_reminders()
            self.load_products()

             # Clear the login fields after successful login
            self.root.get_screen('log_in').ids.login_username.text = ""
            self.root.get_screen('log_in').ids.login_password.text = ""

            # Navigate to the profile screen
            self.root.current = 'home'
        else:
            MDDialog(text="Invalid username or password. Please try again.").open()
     except sqlite3.Error as e:
        print(f"Database error during login: {e}")
        MDDialog(text="An error occurred while logging in. Please try again.").open()

            

    def log_out(self):
     """Log out the user and navigate back to the login screen."""
     self.current_user = None
     self.current_user_id = None
     self.logged_in = False
     self.root.current = 'log_in'  # Navigate back to the login screen
     print("User logged out successfully.")



   

        
    def sign_up(self):
     username = self.root.get_screen('sign_up').ids.username.text
     email = self.root.get_screen('sign_up').ids.email.text
     password = self.root.get_screen('sign_up').ids.password.text
    
    # Regular expression for validating email
     email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
     if not username or not email or not password:
        MDDialog(text="Please fill all fields").open()
     elif not re.match(email_regex, email):  # Check if the email format is valid
        MDDialog(text="Invalid email format. Please enter a valid email address.").open()
     else:
        self.cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
        if self.cursor.fetchone():
            MDDialog(text="Account already exists with this username or email.").open()
        else:
            self.cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))

             # Clear the input fields after successful sign-up
            self.root.get_screen('sign_up').ids.username.text = ""
            self.root.get_screen('sign_up').ids.email.text = ""
            self.root.get_screen('sign_up').ids.password.text = ""
            
            self.conn.commit()
            self.root.current = 'log_in'

    
    def on_start(self):
        self.load_user_profile()
        self.load_saved_plants()
        self.load_reminders()
        self.load_products()
        self.load_products_store()
        self.init_scroll_animation()
        plant_classes = ["Apple", "Blueberry", "Cherry", "Corn", "Grape", "Peach", 
                     "Bell Pepper", "Potato", "Raspberry", "Soybean", "Strawberry", "Tomato"]

        
        reminder_tasks = ["Watering", "Fertilizing", "Pruning", "Checking Soil"]

        
        repeat_options = ["Daily", "Weekly", "Bi-Weekly", "Monthly"]

        self.plant_menu = MDDropdownMenu(
            items=[{"text": plant, "viewclass": "OneLineListItem", "on_release": lambda x=plant: self.set_plant(x)}
                   for plant in plant_classes],
            caller=self.root.get_screen('reminder').ids.plant_name_button,
            width_mult=4,
        )

        self.reminder_task_menu = MDDropdownMenu(
            items=[{"text": task, "viewclass": "OneLineListItem", "on_release": lambda x=task: self.set_task(x)}
                   for task in reminder_tasks],
            caller=self.root.get_screen('reminder').ids.remind_me_about_button,
            width_mult=4,
        )

        self.repeat_menu = MDDropdownMenu(
            items=[{"text": freq, "viewclass": "OneLineListItem", "on_release": lambda x=freq: self.set_repeat(x)}
                   for freq in repeat_options],
            caller=self.root.get_screen('reminder').ids.repeat_frequency_button,
            width_mult=4,
        )



        ################### profil functions#########################

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
     self.load_products_store()

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




    ################# camera functions ##########################

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


##################### navigation bettwen the button and pages #############################
 
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



    ############################################# reminder functions ############

    def set_plant(self, plant_name):
     # Accessing the plant_name_button ID in the reminder screen
     self.root.get_screen('reminder').ids.plant_name_button.text = plant_name
     self.plant_menu.dismiss()
     
    def set_task(self, task_name):
        self.root.get_screen('reminder').ids.remind_me_about_button.text = task_name
        self.reminder_task_menu.dismiss()

    def set_repeat(self, frequency):
        self.root.get_screen('reminder').ids.repeat_frequency_button.text = frequency
        self.repeat_menu.dismiss()
        # Show day/date selection for certain frequencies
        if frequency in ["Weekly", "Bi-Weekly", "Monthly"]:
            self.show_day_selection_dialog(frequency)

    def show_day_selection_dialog(self, frequency):
        day_options = {
            "Weekly": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "Bi-Weekly": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "Monthly": [str(i) for i in range(1, 32)]
        }
        self.day_menu = MDDropdownMenu(
            items=[
                {"text": day, "viewclass": "OneLineListItem", "on_release": lambda x=day: self.set_day(x)}
                for day in day_options[frequency]
            ],
            caller=self.root.get_screen('reminder').ids.repeat_frequency_button,
            width_mult=4,
        )
        self.day_menu.open()

    def set_day(self, day):
        self.root.get_screen('reminder').ids.repeat_frequency_button.text += f" ({day})"
        self.day_menu.dismiss()


        
    def toggle_notification(self, instance, value):
        if value:
            self.root.get_screen('reminder').ids.enable_label.text = "Notifications: On"
        else:
            self.root.get_screen('reminder').ids.enable_label.text = "Notifications: Off"

    def save_reminder(self):
    # Get values from the interface
  
    
     plant_name = self.root.get_screen('reminder').ids.plant_name_button.text
     task = self.root.get_screen('reminder').ids.remind_me_about_button.text
     frequency = self.root.get_screen('reminder').ids.repeat_frequency_button.text
     time = self.root.get_screen('reminder').ids.time_input.text
     notification = 1 if self.root.get_screen('reminder').ids.notification_switch.active else 0

    # Validation messages
     missing_fields = []

     if plant_name == "Select Plant":
        missing_fields.append("Plant Name")
     if task == "Select Task":
        missing_fields.append("Task")
     if frequency == "Select Frequency":
        missing_fields.append("Frequency")
     if not time.strip():
        missing_fields.append("Time")

    # Check if all fields are filled
     if missing_fields:
        MDDialog(
            text=f"Please fill the following fields: {', '.join(missing_fields)}",
            size_hint=(0.8, None),
            height="200dp",
        ).open()
        return

     if self.current_user_id is None:
        MDDialog(text="Error: No user is logged in.").open()
        return

     try:
        # Insert reminder into the database
        self.cursor.execute("""
            INSERT INTO Reminders (plant_name, task, frequency, time, notification, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (plant_name, task, frequency, time, notification, self.current_user_id))
        self.conn.commit()
        

     # Dynamically add the reminder to the UI
        reminder_list = self.root.get_screen('profile').ids.reminder_list  # Profile reminders list
        reminder_text = f"{plant_name} - {task}"
        reminder_list.add_widget(
            OneLineListItem(
                text=reminder_text,
                on_release=lambda x, reminder_name=reminder_text: self.view_reminder_info(reminder_name)
            )
        )


        # Success dialog
        MDDialog(text="Reminder saved successfully!").open()

        # Reset fields
        self.root.get_screen('reminder').ids.plant_name_button.text = "Select Plant"
        self.root.get_screen('reminder').ids.remind_me_about_button.text = "Select Task"
        self.root.get_screen('reminder').ids.repeat_frequency_button.text = "Select Frequency"
        self.root.get_screen('reminder').ids.time_input.text = ""

     except sqlite3.Error as e:
        MDDialog(text=f"Error saving reminder: {e}").open()



######################### E-Store functions #####################################

     # Function to open the file manager
    
  

    
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

     self.load_products()

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




    

    

   

    def navigate_to(self, screen_name):
        if self.dialog:
            self.dialog.dismiss()
        self.root.current = screen_name
  
    def go_to_sign_up(self):
        self.root.current = 'sign_up'

    def go_to_login(self):
        self.root.current = 'log_in'

    def go_to_reminder(self):
        self.root.current = 'reminder'
 
    def go_to_estore(self):
        self.root.current = 'estore'
    

    def go_to_home(self):
        self.root.current = 'home'

    def go_to_profile(self):
        
        self.root.current = 'profile'

    def go_to_camera(self):
     self.root.current = "camera"  # Navigate to Camera without login check
    
    def go_back_to_camera(self):
        self.last_page = None  # Reset last page to indicate it's the home page
        self.root.current = 'camera'

    def on_stop(self):
        self.conn.close()
        super().stop()
        # Delete all images in the 'product_images' folder
        folder_path = "C:/Users/layal/OneDrive - University of Jeddah/bloom/product_images" 
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if file.startswith("product_images") and file.endswith(".png"):
                os.remove(file_path)

    




   


if __name__ == '__main__':
    BloomApp().run()
