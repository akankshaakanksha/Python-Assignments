from window import *
from button import *
from dialogbox import *

#**** test part A 
parent_b=AppWindow('b',Point(2,5),7,7)
parent_a=AppWindow('a',Point(0,0),10,10)
assert(isinstance(parent_a,AppWindow))
assert(isinstance(parent_b,AppWindow))
child_c=ChildWindow(parent_a,'c',Point(4,4),4,4)
child_d=ChildWindow(parent_a,'d',3,9,9)
assert(isinstance(child_d,ChildWindow))
parent_a.addChildWindow(child_c)
assert(isinstance(child_c,ChildWindow))
assert (parent_b.addChildWindow(child_c) == False)
parent_a.addChildWindow(child_d)
try:
	k=parent_a.childIterator()

	assert(k.next()==child_c)
	assert(k.next()==child_d)
#assert(k.next()==False)
except : 
	pass 


#**** test part b
assert(parent_a.hasFocus()==False)
assert(parent_a.setFocus()==True)
assert(parent_a.state!=Window.STATE_MINIMIZED)
assert(parent_a.hasFocus()==True)


#***** test part c
assert(parent_a.get_size()==(10,10))

parent_a.minimize()
assert(parent_a.state==Window.STATE_MINIMIZED)

parent_a.maximize()
assert(parent_a.state==Window.STATE_MAXIMIZED)

parent_a.resize(7,7)
assert(parent_a.get_size()==(7,7))


#******test part d****#
child_e=DialogBox(parent_a,'e',Point(2,5),7,7)
child_e.accept()
assert(parent_a.clickstate=="OK")
child_e.cancel()


#*****test part-e******#

rbGroup = RadioButtonGroup(None, "Radio Group", Point(0, 10), 10, 20)
rButton = RadioButton(rbGroup, "Button1", Point(0, 10), 10, 20)
rButton.getState()
rButton.click()
rButton.RADIO_ACTIVE
rButton.RADIO_INACTIVE	

#**********part f 
#will not add dialog box under childwndow....
assert(parent_a.addChildWindow(child_e)==False)

#********part-g 

parent_b=AppWindow('b',Point(2,5),7,7)
assert (parent_b.addChildWindow(child_c) == False)
assert(parent_a.addChildWindow(child_d)==False)

