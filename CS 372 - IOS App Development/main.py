import sqlite3
from kivy.app import App
from kivy.clock import Clock
import time
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
Window.size = (350,600)

# Create database table for users
conn = sqlite3.connect('/users.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                user_id TEXT,
                password TEXT
                )""")
conn.commit()
conn.close()


class WindowManager(ScreenManager):
    pass


class SplashScreen(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_login, 3)

    def switch_to_login(self, *args):
        self.manager.current = "login"


class LoginScreen(Screen):
    user_id = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):
        # Check user_id and password
        print("UID",self.user_id)
        print("PWD",self.password)
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id=? AND password=?", (self.user_id.text, self.password.text))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.user_id.text = ""
            self.password.text = ""
            self.manager.current = "main"
        else:
            self.show_error_dialog("Invalid user ID or password.")

    def show_error_dialog(self, text):
        dialog = MDDialog(
            title="Error",
            text=text,
            size_hint=(0.7, 0.3),
            buttons=[MDFlatButton(text="OK", on_release=lambda *args: dialog.dismiss())],
        )
        dialog.open()


class AccountCreationScreen(Screen):
    new_name = ObjectProperty(None)
    email = ObjectProperty(None)
    new_user_id = ObjectProperty(None)
    new_password = ObjectProperty(None)

    def create_account(self):
        # Check if user_id already exists
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        #cursor.execute("SELECT * FROM users WHERE user_id=?", (self.new_user_id.text,))
        #if len(cursor.fetchall()) > 0:
        #    conn.close()
        #    self.show_error_dialog("User ID already taken. Please choose a different one.")
        #    return

        # Insert new user into database
        cursor.execute("INSERT INTO users (name, email, user_id, password) VALUES (?, ?, ?, ?)",
                       (self.new_name.text, self.email.text, self.new_user_id.text, self.new_password.text))
        conn.commit()
        conn.close()

        # Clear fields after account creation
        self.new_name.text = ""
        self.email.text = ""
        self.new_user_id.text = ""
        self.new_password.text = ""

        self.show_success_dialog("Account created successfully.")

    def show_error_dialog(self, text):
        dialog = MDDialog(
            title="Error",
            text=text,
            size_hint=(0.7, 0.3),
            buttons=[MDFlatButton(text="OK", on_release=lambda *args: dialog.dismiss())],
        )
        dialog.open()

    def show_success_dialog(self, text):
        dialog = MDDialog(
            title="Success",
            text=text,
            size_hint=(0.7, 0.3),
            buttons=[MDFlatButton(text="OK", on_release=lambda *args: dialog.dismiss())],
        )
        dialog.open

#====================
class MainScreen(Screen):
    text_field_text = StringProperty("")
    label_text = StringProperty("")

    def button_on_press(self):
        self.label_text = self.ids.text_field.text

    def logout(self):
        self.manager.current = "login"


kv = """
WindowManager:
    SplashScreen:
    LoginScreen:
    AccountCreationScreen:
    MainScreen:

<SplashScreen>:
    name: "splash"
    Image:
        source: "splash-screen.JPG"
        allow_stretch: True
        keep_ratio: False
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

<AccountCreationScreen>:
    name: "account_creation"

    new_name: name_field
    email: email_field
    new_user_id: new_user_id_field
    new_password: new_password_field

    MDTopAppBar:
        title: "Create Account"
        pos_hint: {"top": 1}

    BoxLayout:
        orientation: "vertical"
        pos_hint: {"center_x": 0.5, "center_y": 0.92}
        MDTextField:
            id: name_field
            hint_text: "Name"
            icon_left: "account"
            icon_left_color: app.theme_cls.primary_color
            size_hint_x: 0.8
            width: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.8}

        MDTextField:
            id: email_field
            hint_text: "Email"
            icon_left: "email"
            icon_left_color: app.theme_cls.primary_color
            size_hint_x: 0.8
            width: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.7}

        MDTextField:
            id: new_user_id_field
            hint_text: "User ID"
            icon_left: "account"
            icon_left_color: app.theme_cls.primary_color
            size_hint_x: 0.8
            width: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.6}

        MDTextField:
            id: new_password_field
            hint_text: "Password"
            icon_left: "lock"
            icon_left_color: app.theme_cls.primary_color
            size_hint_x: 0.8
            width: 0.8
            password: True
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

    MDFlatButton:
        text: "Create Account"
        theme_text_color: "Custom"
        text_color: 0, 0.6, 1, 1
        line_color: 0, 0.6, 1, 1
        pos_hint: {"center_x": 0.3, "center_y": 0.35}
        on_press: root.create_account()

    MDFlatButton:
        text: "Cancel"
        theme_text_color: "Custom"
        text_color: 0, 0.6, 1, 1
        line_color: 0, 0.6, 1, 1
        pos_hint: {"center_x": 0.7, "center_y": 0.35}
        on_press: app.root.current = "login"

<LoginScreen>:
    name: "login"
    user_id: user_id_field
    password: password_field

    MDTopAppBar:
        title: "Login"
        pos_hint: {"top": 1}

    MDFlatButton:
        text: "Login"
        theme_text_color: "Custom"
        text_color: 0, 0.6, 1, 1
        line_color: 0, 0.6, 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        on_press: root.login()

    MDFlatButton:
        text: "Create Account"
        theme_text_color: "Custom"
        text_color: 0, 0.6, 1, 1
        line_color: 0, 0.6, 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        on_press: app.root.current = "account_creation"
        
    BoxLayout:
        orientation: "vertical"
        pos_hint: {"center_x": 0.5, "center_y": 1.12}
        MDTextField:
            id: user_id_field
            hint_text: "User ID"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
        MDTextField:
            id: password_field
            hint_text: "Password"
            size_hint_x: 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.4}


<MainScreen>:
    name: "main"
    text_field_text: text_field.text
   
    Image:
        source: "background.jpg"
        allow_stretch: True
        keep_ratio: False

    MDTopAppBar:
        title: "Logo Creator"
        pos_hint: {"top": 1}

    Image:
        source: "kivy_logo.png"
        size_hint_x: 0.5
        size_hint_y: 0.5
        pos_hint: {"center_x": 0.5, "center_y": 0.7}

    MDLabel:
        id: label
        text: root.label_text
        halign: "center"
        font_style: "H5"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}

    MDTextField:
        id: text_field
        hint_text: "Enter Title"
        size_hint_x: 0.8
        pos_hint: {"center_x": 0.5, "center_y": 0.4}

    MDFlatButton:
        text: "Write Title"
        theme_text_color: "Custom"
        text_color: 0, 0.6, 1, 1
        line_color: 0, 0.6, 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press: root.button_on_press()

    MDFlatButton:
        text: "Logout"
        theme_text_color: "Custom"
        text_color: 0, 0.6, 1, 1
        line_color: 0, 0.6, 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.1}
        on_press: root.logout()
     
"""

class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        self.title = "Logo Creator"
        self.icon = "kivy_logo.png"
        screen_manager = ScreenManager()
        screen_manager.add_widget(SplashScreen())
        screen_manager.add_widget(LoginScreen())
        screen_manager.add_widget(AccountCreationScreen())
        screen_manager.add_widget(MainScreen())
        return Builder.load_string(kv)


if __name__ == "__main__":
    TestApp().run()
