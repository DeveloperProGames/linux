from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class AdMobExampleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Show Ad')
        layout.add_widget(button)
        return layout
if __name__ == '__main__':
    AdMobExampleApp().run()
