from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Dashboard(BoxLayout):
    pass

class OwlEyesApp(App):
    def build(self):
        return Dashboard()

if __name__ == "__main__":
    OwlEyesApp().run()
