from point import Point

class BadArgumentError(Exception):
    def __init__(self, cause):
        Exception.__init__(self, cause)



Infocus=''	



childwindow_record=[]


class Window(object):
    STATE_NORMAL    = 0x1
    STATE_MINIMIZED = 0x2
    STATE_MAXIMIZED = 0x4
    FOCUS_FOREGROUND = 0x1
    FOCUS_BACKGROUND = 0x2
    OKYED=0x1
    CANCELED=0x2
#clickstate states the last response of the user
    clicked="OK"    
    def __init__(self, parent, title, top_left, w, h):
    	self.parent = parent
        self.title = title
        self.top_left = top_left
        self.height = h
        self.width = w
        self.state = Window.STATE_NORMAL
	self.button="b1"
	self.clicked=Window.OKYED
	global Inofocus
        Infocus=self.title

    def get_title(self):
        return self.title
    
    def resize(self, w, h):
        self.width = w
        self.height = h

    def get_size(self):
        return (self.width, self.height)

    def get_state(self):
    	return self.state
        
    def __str__(self):
    	return "(Window: (%s), (width: %d, height: %d)" % (self.title, self.width, self.height)


    def setFocus(self):
	if (self.title is Infocus):
	    return False
	global Infocus
	Infocusf=self.title
	self.state = Window.STATE_NORMAL
	return True

    def hasFocus(self):
        if (self.title is Infocus) : 
	    return  True
	else:
            return False
  
    def minimize(self):
        if self.state==Window.STATE_MINIMIZED:
	    return False
	else :
	    self.state=Window.STATE_MINIMIZED
	    return True

    def maximize(self):
        if self.state==Window.STATE_MAXIMIZED:
	    return False
	else :
	    self.setFocus()
	    self.state=Window.STATE_MAXIMIZED
	    return True

       
class Container(Window):
    def __init__(self, parent, title, top_left, w, h):
        Window.__init__(self, parent, title, top_left, w, h)
        self.children = []

        	    
    def addChildWindow(self, childWindow):
	try:
	    if isinstance(childWindow,ChildWindow)==False :
	        raise BadArgumentError("Expecting a valid child window instance")
 
            if isinstance(childWindow, ChildWindow):
	        for i in window_record[:]:
		    if i[0]==childWindow :
			
		        if i[1]==0 :	    
           		    self.children.append(childWindow)
			
		            childwindow_record.append((childWindow,2))
			    break
         	        else: raise BadArgumentError("Existing child window instance")
	    	   
	        self.children.append(childWindow)
	    
	        childwindow_record.append((childWindow,2))
	        
	        return True
	
 
	except BadArgumentError :
	    return False

 
    def childIterator(self) : 
	
	self.list=self.children.__iter__()
	return self.list

    def next(self):
        return self.list.next()

class ChildWindow(Window):
    def __init__(self, parent, title, top_left, w, h):
        if parent is None or not isinstance(parent, Container):
            raise BadArgumentError("Expecting a valid parent window instance")
	    
        Window.__init__(self, parent, title, top_left, w, h)



class AppWindow(Container):
    def __init__(self, title, top_left = Point(0, 0), w=40, h=40):
        Container.__init__(self, None, title, top_left, w, h)
	self.children=[]

    def addChildWindow(self,childWindow):

	try:
	    if isinstance(childWindow,ChildWindow)==True or isinstance(childWindow,Container)==True or isinstance(childWindow,Window)==True   :
	        raise BadArgumentError("Expecting a valid child window instance")
 
            else :
	        for i in window_record[:]:
		    if i[0]==childWindow :
			
		        if i[1]==0 :	    
           		    self.children.append(childWindow)
			
		            childwindow_record.append((childWindow,2))
			    break
         	        else: raise BadArgumentError("Existing child window")
	    
	        self.children.append(childWindow)
	    
	        childwindow_record.append((childWindow,2))
	        
	        return True
	
             
	except BadArgumentError :
	    return False


