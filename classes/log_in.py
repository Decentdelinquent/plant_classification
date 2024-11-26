import sqlite3
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.animation import Animation
from kivymd.uix.behaviors.hover_behavior import HoverBehavior
from kivymd.uix.button import MDFillRoundFlatIconButton

Window.size = (350, 600)

# KV Design Language with Updated Login as First Page, followed by Sign-Up Page
KV = '''
ScreenManager:
    LoginScreen:
    SignUpScreen:

<LoginScreen>:
    name: 'log_in'

    canvas.before:
        Rectangle:
            source: "C:/Users/layal/OneDrive - University of Jeddah/bloom\pictu/sin and log in background.jpg"
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
                source: "C:/Users/layal/OneDrive - University of Jeddah/bloom/pictu/bloom_logo.jpg"
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
            pos_hint: {"center_y": 0.3}  # Adjusted position
            theme_text_color: "Custom"
            markup: True
            font_size: "15sp"
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
            on_ref_press: app.continue_as_guest()


'''

class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass




class Login(MDApp):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user_id = None  # Initialize user ID to None
      
    

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.conn = sqlite3.connect("C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, email TEXT, password TEXT)")
        return Builder.load_string(KV)
        return screen

    def on_start(self):
        # Apply an animation effect to the "Continue as Guest" link
        guest_label = self.root.get_screen('log_in').ids.guest_label
        anim = Animation(opacity=0.5, duration=1) + Animation(opacity=1, duration=1)
        anim.repeat = True  # Repeat the animation to make it loop
        anim.start(guest_label)

    def continue_as_guest(self):
        self.root.current = 'home'  # Directly navigate to the homepage screen
        

    

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

       

            # Navigate to the profile screen
            self.root.current = 'home'
        else:
            MDDialog(text="Invalid username or password. Please try again.").open()
     except sqlite3.Error as e:
        print(f"Database error during login: {e}")
        MDDialog(text="An error occurred while logging in. Please try again.").open()


    def go_to_login(self, *args):
        self.root.current = 'log_in'

    def go_to_sign_up(self, *args):
        self.root.current = 'sign_up'

    def on_stop(self):
        self.conn.close()

Login().run()
