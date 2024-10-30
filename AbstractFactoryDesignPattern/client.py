from windowsfactory import WindowsFactory
from macfactory import MacFactory
if __name__=="__main__":
    winfactory=WindowsFactory()
    macfactory=MacFactory()
    winfactory.create_button().render()
    macfactory.create_textbox().render()