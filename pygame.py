import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt 
import pygame
import sys
from pygame.locals import *

G=6.67*10**(-11)
AU=1
GmS=4*math.pi**2
dt=0.001

class Planeta:
	def __init__(self,m,x, y, vx,vy):
		self.m=m
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.r=np.sqrt(x**2+y**2) 
		self.E= 0.5*self.m*((vx**2)+(vy**2))-GmS*self.m/self.r

		
	def a(self,p):
		r=np.sqrt(self.x**2+self.y**2)
		return -((GmS)/r**3)*p
				
	def movimento(self):
		ax = self.a(self.x)
		self.x=self.x+self.vx*dt+0.5*ax*dt**2
		self.vx=self.vx+ax*dt
		ay=self.a(self.y)
		self.y=self.y+self.vy*dt+0.5*ay*dt**2
		self.vy=self.vy+ay*dt
		self.E=0.5*self.m*((self.vx**2)+(self.vy**2))-GmS*self.m/self.r
		

p1 = Planeta(14.536,4,0,0,np.pi) 
p2 = Planeta(1,1,0,0,2*np.pi)

pygame.init()
screen = pygame.display.set_mode((600,600))
myfont = pygame.font.Font(None,60)

space = pygame.image.load("space.png").convert()
sun = pygame.image.load("sun.png").convert_alpha()
terra = pygame.image.load("planeta.png").convert_alpha()
urano = pygame.image.load("t.png").convert_alpha()

pygame.display.set_caption("O Sol o Urano e a Terra") 

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	terra = pygame.transform.scale(terra,(15,15))
	urano = pygame.transform.scale(urano,(30,30))
	sun = pygame.transform.scale(sun,(60,60))
	screen.blit(space, (0,0))
	screen.blit(sun, ((600-40)/2, (600-40)/2)) 
	
	p1.movimento()
	p2.movimento()
	
	screen.blit(urano, (p1.x*(600-20)/10+ (600-20)/2, p1.y*(600-20)/10+(600-20)/2))
	screen.blit(terra, (p2.x*(600-20)/10+ (600-20)/2, p2.y*(600-20)/10+(600-20)/2))
	
	pygame.display.update()
	
