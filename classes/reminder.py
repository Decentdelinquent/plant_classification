
import sqlite3
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDSwitch
import tkinter as tk
from tkinter import messagebox

Window.size = (350, 600)

class SetReminder(MDApp):

    # for the current user logged in id 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user_id = None    # Store the logged-in user's ID
    


    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Light"
        
        # Connect to SQLite database
        self.conn = sqlite3.connect(r"C:/Users/layal/OneDrive - University of Jeddah/bloom/bloom_app.db")

        self.cursor = self.conn.cursor()
        # Create reminders table if it doesn't exist
        
        return Builder.load_string(KV)

    def on_start(self):
    
        plant_classes = ["Apple", "Blueberry", "Cherry", "Corn", "Grape", "Peach", 
                     "Bell Pepper", "Potato", "Raspberry", "Soybean", "Strawberry", "Tomato"]

        
        reminder_tasks = ["Watering", "Fertilizing", "Pruning", "Checking Soil"]

        
        repeat_options = ["Daily", "Weekly", "Bi-Weekly", "Monthly"]

        self.plant_menu = MDDropdownMenu(
            items=[{"text": plant, "viewclass": "OneLineListItem", "on_release": lambda x=plant: self.set_plant(x)}
                   for plant in plant_classes],
            caller=self.root.ids.plant_name_button,
            width_mult=4,
        )

        self.reminder_task_menu = MDDropdownMenu(
            items=[{"text": task, "viewclass": "OneLineListItem", "on_release": lambda x=task: self.set_task(x)}
                   for task in reminder_tasks],
            caller=self.root.ids.remind_me_about_button,
            width_mult=4,
        )

        self.repeat_menu = MDDropdownMenu(
            items=[{"text": freq, "viewclass": "OneLineListItem", "on_release": lambda x=freq: self.set_repeat(x)}
                   for freq in repeat_options],
            caller=self.root.ids.repeat_frequency_button,
            width_mult=4,
        )

    def set_plant(self, plant_name):
     # Accessing the plant_name_button ID in the reminder screen
     self.root.ids.plant_name_button.text = plant_name
     self.plant_menu.dismiss()
     
    def set_task(self, task_name):
        self.root.ids.remind_me_about_button.text = task_name
        self.reminder_task_menu.dismiss()

    def set_repeat(self, frequency):
        self.root.ids.repeat_frequency_button.text = frequency
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
            caller=self.root.ids.repeat_frequency_button,
            width_mult=4,
        )
        self.day_menu.open()

    def set_day(self, day):
        self.root.ids.repeat_frequency_button.text += f" ({day})"
        self.day_menu.dismiss()


        
    def toggle_notification(self, instance, value):
        if value:
            self.root.ids.enable_label.text = "Notifications: On"
        else:
            self.root.ids.enable_label.text = "Notifications: Off"

    def save_reminder(self):
    # Get values from the interface
  
    
     plant_name = self.root.ids.plant_name_button.text
     task = self.root.ids.remind_me_about_button.text
     frequency = self.root.ids.repeat_frequency_button.text
     time = self.root.ids.time_input.text
     notification = 1 if self.root.ids.notification_switch.active else 0

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
        reminder_list = self.root.ids.reminder_list  # Profile reminders list
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
        self.root.ids.plant_name_button.text = "Select Plant"
        self.root.ids.remind_me_about_button.text = "Select Task"
        self.root.ids.repeat_frequency_button.text = "Select Frequency"
        self.root.ids.time_input.text = ""

     except sqlite3.Error as e:
        MDDialog(text=f"Error saving reminder: {e}").open()

KV = '''
Screen:
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

SetReminder().run()

