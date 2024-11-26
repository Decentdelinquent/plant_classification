from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (350, 600)

KV = '''


Screen:
    canvas.before:
        Rectangle:
            source: "C:/Users/layal/OneDrive - University of Jeddah/bloom/pictu/hoe_bacground.jpg"  # Set background image path here
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(10)
        spacing: dp(20)
        pos_hint: {"center_x": 0.5, "center_y": 0.6}  # Center content vertically
        size_hint_y: None
        height: self.minimum_height  # Make the height dynamic based on content

        # Welcome Text
        MDLabel:
            text: "Welcome to Bloom"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0.6, 0, 1  # Green text color
            font_style: "H5"
            bold: True  # Make text bold
            size_hint_y: None
            height: self.texture_size[1]

        # Subtitle Text
        MDLabel:
            text: "Where you can identify your plants, exchange resources with other users, save your plants, and set watering reminders."
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1  # Black text color
            font_style: "Body1"
            size_hint_y: None
            height: self.texture_size[1]

    MDBottomNavigation:
        size_hint_y: 0.15
        panel_color: 0.9, 0.9, 0.9, 1  # Light gray background
        text_color_active: 0.5, 0.5, 0.5, 1  # Neutral gray text color
        selected_color_background: 0, 0, 0, 0  # No background color for selected tab
        unselected_color: 0.5, 0.5, 0.5, 1  # Gray color for unselected icons

        # Home icon
        MDBottomNavigationItem:
            name: "home"
            icon: "home"
            text: "Home"

        # Profile icon
        MDBottomNavigationItem:
            name: "profile"
            icon: "account"
            text: "Profile"
            on_tab_press: app.show_login_dialog_or_navigate("profile")

        # Camera icon
        MDBottomNavigationItem:
            name: "camera"
            icon: "camera"
            text: "Camera"
            on_tab_press: app.show_login_dialog_or_navigate("camera")

        # E-store icon
        MDBottomNavigationItem:
            name: "estore"
            icon: "store"
            text: "E-store"
            on_tab_press: app.show_login_dialog_or_navigate("estore")

        # Reminder icon
        MDBottomNavigationItem:
            name: "reminder"
            icon: "bell-ring"
            text: "Reminder"
            on_tab_press: app.show_login_dialog_or_navigate("reminder")
'''

class Home(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


Home().run()
