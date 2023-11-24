# Sample project with solution

# Create  a  simple  mobile  application  using  the Kivy  library  to  demonstrate  the  working  of  a  simple  calculator.  We  can  use  a Python  file  for  defining  application  classes  and  a  KV  file  to  define  widgets  for  the  application  along  with  their  properties.  Also,  create  an  apk  file  for  the  application  to  use  ion an  aAndroid  phone:.

# main.py

from  kivy.app  import  App
from  kivy.uix.gridlayout  import  GridLayout
from  kivy.config  import  Config
import  math
Config.set('graphics',  'resizable',  1)

class  ProjectKivyCalculator(GridLayout):
        #  method  called  when  =  button  (equals)  is  clicked/  pressed
        def  res_calculate(self,  operation):
                if  operation:
                        try:
                                self.display.text  =  str(eval(operation))
                        except  Exception:
                                self.display.text  =  "Error"


#  Now  creating  an  App  class  for  calculator
class  KivyCalculatorApp(App):
        def  build(self):
                myapp  =  ProjectKivyCalculator()
                return  myapp

#  creating  object  and  running  it
demoApp  =  KivyCalculatorApp()
demoApp.run()

# kivycalculator.kv:

#  Create  a  custom  button  to  add  new  buttons
<CustButton@Button>:
  font_size:  40
  background_color:  (0,0.5,0.5,1)

<ProjectKivyCalculator>:
  id:  calculator
  display:  entry
  rows:  6
  padding:  10
  spacing:  10

  #  Text  Input  where  input  will  be  displayed
  BoxLayout:
    TextInput:
      id:  entry
      font_size:  40
      multiline:  False
	
  #  When  buttons  are  pressed  update  the  entry
  BoxLayout:
    spacing:  10
    CustButton:
      text:  "7"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "8"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "9"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "/"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "sin"
      on_press:  entry.text  +=  "math.sin("
    CustButton:
      text:  "("
      on_press:  entry.text  +=  self.text

  BoxLayout:
    spacing:  10
    CustButton:
      text:  "4"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "5"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "6"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "*"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "cos"
      on_press:  entry.text  +=  "math.cos("
    CustButton:
      text:  ")"
      on_press:  entry.text  +=  self.text

  BoxLayout:
    spacing:  10
    CustButton:
      text:  "1"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "2"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "3"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "-"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "tan"
      on_press:  entry.text  +=  "math.tan("
    CustButton:
      text:  "sqrt"
      on_press:  entry.text  +=  "math.sqrt("

  #  When  equals  is  pressed  pass  text  in  the  entry
  #  to  the  calculate  function
  BoxLayout:
    spacing:  10
    CustButton:
      text:  "CLS"
      on_press:  entry.text  =  ""
    CustButton:
      text:  "0"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "="
      on_press:  calculator.res_calculate(entry.text)
    CustButton:
      text:  "+"
      on_press:  entry.text  +=  self.text
    CustButton:
      text:  "log"
      on_press:  entry.text  +=  "math.log("
    CustButton:
      text:  "."
      on_press:  entry.text  +=  self.text

  BoxLayout:
    CustButton:
      font_size:  50
      bold:  True
      text:  "Calculate"
      on_press:  calculator.res_calculate(entry.text)
