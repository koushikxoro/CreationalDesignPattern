from windowselements import WindowsButton, WindowsTextBox
from guifactory import GUIFactory
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    def create_textbox(self):
        return WindowsTextBox()
