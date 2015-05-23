from window import *
from point import Point


class DialogBox(Container):
    STATE_CANCEL=0
    STATE_ACCEPT=1
    def __init__(self, parent, title, top_left, w, h):
    	assert(parent is not None)
    	assert(isinstance(parent, (AppWindow)))
        assert(isinstance(top_left, Point))

        Container.__init__(self, parent, title, top_left, w, h)
	self.state=None

    def accept(self):
    	self.state=DialogBox.STATE_ACCEPT

    def cancel(self):
   	self.state=DialogBox.STATE_CANCEL
	
    def getState(self):
	return self.state
