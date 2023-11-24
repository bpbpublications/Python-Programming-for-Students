# Demonstarte the kivy Application Lifecycle

#    import  the  necessary  modules
import  kivy
from  kivy.app  import  App
from  kivy.uix.label  import  Label
#    we  create  a  class  to  represent  the  application  window.
#    The  class  inherits  from  the  App  class  to  use  all  its  functions.    Here  the  method  build()  is  implemented  to  describe  components  placed  on  the  screen.Here  we  return  a  Label  with  caption  "This  is  a  label"
class  DemoApp(App):
        def  build(self):
                return  Label(text="This  is  a  Label")
#  To  run  the  application  we  need  to  call  run()  method  with  newly  created  class
if  __name__  ==  "__main__":
        DemoApp().run()
#  A  Python  programme  uses  the  condition  if  __name__  ==  '__main__'  to  only  run  the  code_inside  the  if  statement  when  the  program  is  run  directly  by  the  Python  interpreter.  The  code  inside  the  if  statement  is  not  executed  when  the  file's  code  is  imported  as  a  module.
