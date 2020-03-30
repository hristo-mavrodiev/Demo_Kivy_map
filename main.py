from kivy.garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.app import App

from kivy.uix.label import Label

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout


class EPSGConvertor(App):
    def build(self):

        layout = BoxLayout(orientation='vertical')
        self.mapview = MapView(zoom=7, lat=42.6394, lon=25.057)

        marker = MapMarkerPopup(id="first", lat=42.6394, lon=25.057)
        marker.add_widget(BoxLayout(orientation='horizontal'))
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
