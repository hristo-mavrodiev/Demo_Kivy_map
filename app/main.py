from kivy.uix.bubble import Bubble
from kivy.garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.popup import Popup
from kivy.uix.bubble import Bubble
from kivy.uix.boxlayout import BoxLayout
from tr_proj import transform_epsg


class EPSGConvertor(App):
    def build(self):

        layout = BoxLayout(orientation='vertical')
        self.mapview = MapView(zoom=7, lat=42.6394, lon=25.057)

        bubble = Bubble(orientation="horizontal", padding=5)
        text = str(transform_epsg('epsg:4326', 'epsg:3857', 42.6394, 25.057))
        label = Label(text=text, markup=True, halign="center")
        bubble.add_widget(label)
        marker = MapMarkerPopup(id="first", lat=42.6394,
                                lon=25.057, popup_size=('550dp', '100dp'))
        marker.add_widget(bubble)
        self.mapview.add_marker(marker)

        b = BoxLayout(orientation='horizontal',
                      height='52dp', size_hint_y=None)
        b.add_widget(Button(text="Zoom in", on_press=lambda a: setattr(
            self.mapview, 'zoom', self.mapview.zoom + 1)))
        b.add_widget(Button(text="Zoom out", on_press=lambda a: setattr(
            self.mapview, 'zoom', self.mapview.zoom - 1)))

        layout.add_widget(self.mapview)
        layout.add_widget(b)
        return layout


if __name__ == "__main__":
    EPSGConvertor().run()
