
""""Answer for Question Two"""""
from math import *


def length(vec):
	x1=vec[0][0]
	x2=vec[1][0]
	y1=vec[0][1]
	y2=vec[1][1]
	z1=vec[0][2]
	z2=vec[1][2]
	return ((x1-x2)**2 +(y1-y2)**2 +(z1-z2)**2)**0.5

def normalize(vec):
	 x1=vec[0][0]
	 x2=vec[1][0]
	 y1=vec[0][1]
	 y2=vec[1][1]
	 z1=vec[0][2]
	 z2=vec[1][2]
	 lens=length(vec)
	 return ((0,0,0),(abs((x1-x2)/lens),abs((y1-y2)/lens),abs((z1-z2)/lens)))
def dot_product(vec11,vec12):
	lens1=length(vec11)
	lens2=length(vec12)
	vec1=normalize(vec11)
	vec2=normalize(vec12)
	px=vec1[1][0]*vec2[1][0]*lens1*lens2
	py=vec1[1][1]*vec2[1][1]*lens1*lens2
	pz=vec1[1][2]*vec2[1][2]*lens1*lens2
	return px+py+pz
	
def cross_product(vec11,vec12):
	lens1=length(vec11)
	lens2=length(vec12)
	vec1=normalize(vec11)
	vec2=normalize(vec12)
	i=vec1[1][1]*vec2[1][2]-vec1[1][2]*vec2[1][1]
	j=(vec1[1][2]*vec2[1][0]-vec1[1][0]*vec2[1][2])
	k=vec1[1][0]*vec2[1][1]-vec1[1][1]*vec2[1][0]
	return ((0,0,0),(lens1*lens2*i,lens1*lens2*j,lens1*lens2*k))









	
	
