from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MiApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.boton = Button(text='Presionar')
        self.boton.bind(on_press=self.mostrar_texto)
        layout.add_widget(self.boton)
        return layout

    def mostrar_texto(self, instance):
        self.boton.parent.add_widget(Label(text='¡Funciona!'))

if __name__ == '__main__':
    MiApp().run()