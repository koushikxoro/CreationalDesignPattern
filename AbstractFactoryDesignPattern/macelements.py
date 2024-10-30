from uielements import Button,Textbox
class MacButton(Button):
    def render(self):
        print("This is mac button.")
class MacTextbox(Textbox):
    def render(self):
        print("This is a mac textbox.")