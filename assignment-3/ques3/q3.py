######     ANSWER 3    #########

###########################################   PART-a #########################################################3333333
class Rectangle(object):
	class Point(object):					
		def __init__(self,x,y):
			self.x=x;
			self.y=y;

	def __init__(self,point,w,h):				
		self.point=self.Point(point.x,point.y);
		self.w=w;
		self.h=h;

	def intersect(self,other):			
		x1 = self.point.x
		x2 = other.point.x
		y1 = self.point.x
		y2 = other.point.y
		w1 = self.w
		w2 = other.w
		h1 = self.h
		h2 = other.h
		X = (((x1<=x2) and (x2<=(x1+w1))) or ((x2<=x1) and (x1<=(x2+w2))))
		Y = (((y1<=y2) and (y2<=(y1+h1))) or ((y2<=y1) and (y1<=(y2+h2))))
		if ( X and Y):
			return True
		else:
		 	return False













######################################################## Part-B#############################################
import re
class WordIterator(object):
    def __init__(self,string):
	assert(isinstance(string,str) is True)
        self.words=string.split(" ")
        self.ctr=0
        self.max=len(self.words)


    def __iter__(self):
       return self.words.__iter__()

    def __next__(self):   
        if (self.ctr<self.max):
           self.ctr=self.ctr+1 
           return self.words[self.ctr-1]
        else:
           raise StopIteration()



##############################################      PART -C       ###########################################################

class pointIterator(object):

	def __init__(self,point1,point2,div):
		self.x1,self.y1=point1
		self.x2,self.y2=point2
		self.divisions=div
		self.xdiv=(self.x2-self.x1)/self.divisions
		self.ydiv=(self.y2-self.y1)/self.divisions

	def next(self):
		self.divisions-=1		
		if(self.divisions>=0):

			self.x1+=self.xdiv
			self.y1+=self.ydiv
			
			return self.x1,self.y1


		else :
			raise StopIteration





