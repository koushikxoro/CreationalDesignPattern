from macelements import MacButton, MacTextbox
from guifactory import GUIFactory
class MacFactory(GUIFactory):
    def create_button():
        return MacButton()
    def create_textbox(self):
        return MacTextbox()