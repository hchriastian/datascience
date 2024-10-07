from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


# Dummy data untuk login (sebagai pengganti database)
users = {
    "user1": "password123",
    "admin": "adminpassword"
}


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Membuat input untuk username
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.add_widget(self.username_input)

        # Membuat input untuk password
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False)
        self.add_widget(self.password_input)

        # Membuat tombol login
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.validate_login)
        self.add_widget(self.login_button)

    def validate_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Validasi login
        if username in users and users[username] == password:
            self.show_popup('Login Berhasil', f'Selamat datang, {username}!')
        else:
            self.show_popup('Login Gagal', 'Username atau password salah.')

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_label = Label(text=message)
        close_button = Button(text='Tutup', size_hint=(1, 0.25))

        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.75, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()


class LoginApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
