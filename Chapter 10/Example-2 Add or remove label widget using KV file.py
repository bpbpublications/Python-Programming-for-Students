# Example  to  add  or  remove  a  label  widget  using  button  widgets  in  a  .kv  file.

# WidgetAddRemove.py:

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class WidgetAddRemove(BoxLayout):
    pass
class KivyDemoApp(App):
    def build(self):
        new_widget = WidgetAddRemove()
        return new_widget

if __name__ == '__main__':
    KivyDemoApp().run()


# kivydemo.kv  

<WidgetAddRemove>:
    lbl_wgt: lbl_wgt.__self__
    Button:
        text: 'Click to Add widget'
        on_press: root.add_widget(lbl_wgt)
    Button:
        text: 'Click to Remove widget'
        on_press: root.remove_widget(lbl_wgt)
    Label:
        id: lbl_wgt
        text: 'Label Widget'
