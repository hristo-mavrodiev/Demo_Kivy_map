from kivy.uix.bubble import Bubble
from kivy.garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.popup import Popup
from kivy.uix.bubble import Bubble


class EPSGConvertor(App):
    def build(self):

        layout = BoxLayout(orientation='vertical')
        self.mapview = MapView(zoom=7, lat=42.6394, lon=25.057)

        bubble = Bubble(orientation="horizontal", padding=5)
        text = "[b]Sample text here[/b]"
        label = Label(text=text, markup=True, halign="center")
        bubble.add_widget(label)
        marker = MapMarkerPopup(id="first", lat=42.6394,
                                lon=25.057, popup_size=('150dp', '100dp'))
        marker.add_widget(bubble)
        self.mapview.add_marker(marker)

        b = BoxLayout(orientation='horizontal',
                      height='52dp', size_hint_y=None)
        b.add_widget(Button(text="Zoom in", on_press=lambda a: setattr(
            self.mapview, 'zoom', self.mapview.zoom + 1)))
        b.add_widget(Button(text="Zoom out", on_press=lambda a: setattr(
            self.mapview, 'zoom', self.mapview.zoom - 1)))

        layout.add_widget(b)
        layout.add_widget(self.mapview)
        return layout


if __name__ == "__main__":
    EPSGConvertor().run()
