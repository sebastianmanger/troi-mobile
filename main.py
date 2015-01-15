from datetime import datetime

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import StringProperty


class Header(BoxLayout):
    """
    Some kind of Label/Icon and the selected date. If the date is clicked, open a dialogue to select a date.
    """
    date = StringProperty(datetime.now().strftime('%d. %B %Y'))

    def select_date(self):
        pass


class RecordApp(App):
    """
    The main class. The 'record.kv' file is loaded due to naming conventions.
    """
    def build(self):
        return Header()

if __name__ == '__main__':
    RecordApp().run()
