from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.webview import WebView

class TivifyApp(App):
    def build(self):
        layout = BoxLayout()
        # WebView carga la web oficial
        wv = WebView(url="https://www.tivify.es/es/registro")
        layout.add_widget(wv)
        return layout

if __name__ == '__main__':
    TivifyApp().run()
  
