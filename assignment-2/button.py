from window import *
from point import *
from dialogbox import *
class RadioButtonGroup(Container):
	def __init__(self,parent, title, top_left,w,h):
    	    Container.__init__(self, parent, title, top_left, w,h)
	    self.a=[]
	    
	def btn(self,button):
		self.button=button
		r=RadioButton(self.button)
		self.parent.button=r.lst[button]
		return r.lst[button]

	

class Button(ChildWindow): 
    def __init__(self, parent, title, top_left, w, h):
        if parent is None or not isinstance(parent, Container):
             raise BadArgumentError("Expecting a valid parent window")
        
        Window.__init__(self, parent, title, top_left, w, h)


class RadioButton(Button):
    RADIO_ACTIVE=1
    RADIO_INACTIVE=0
	  
    def __init__(self,button_b,button,top_left,w,h):

	self.button_b=button_b
	self.button=button
   
        if len(self.button_b.a)==0 :
	    self.button_b.a.append((self.button,RadioButton.RADIO_ACTIVE))

        if len(self.button_b.a)!=0 :
	    self.button_b.a.append((self.button,RadioButton.RADIO_INACTIVE))
	pass

    def click(self):
	for i in range(len(self.button_b.a)):
	    if self.button_b.a[i][0] == self.button :
		break 
	
	if self.button_b.a[i][1]==RadioButton.RADIO_ACTIVE:
	    return False
	else:
	    self.button_b.a[i][1]=RadioButton.RADIO_ACTIVE
	
	for i in range(len(button_b.a)):
		if self.button_b.a[0]!=self.button:
			self.button_b.a[i][1]=RadioButton.RADIO_INACTIVE

	return True
	
    def getState(self):
	for i in range(len(self.button_b.a)):
	    if self.button_b.a[i][0] == self.button :
		 
		return self.button_b.a[i][1]


class OK(object):
    def __init__(self):
	pass

    def click():
	self.parent.clicked=WIndow.OKYED


class Cancel(object):
    def __init__(self):
	pass

    def click():
	self.parent.clicked=Window.CANCELED



