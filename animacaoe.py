#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation as animation
import math

class Problema2:
	def __init__(self, L, x, v):
		self.m= rhob*(L**3)
		self.L= L
		self.x= x
		self.v= v
		
	def a(self, x, v):
		return (((rhob-rholiq)*g*(self.L**3))-( (k/self.m)*(x-xo) )- (rhorf*v))/self.m


	def movimento(self, t):
		at= self.a(self.x, self.v)
		self.x= self.x + self.v*dt + 0.5*at*(dt**2)
		atem= self.a(self.x, self.v)
		vtem= self.v + 0.5*(at+atem)*dt
		atem= self.a(self.x, vtem)
		self.v= self.v + 0.5*(at+atem)*dt
		self.at= self.a(self.x, self.v)


g=9.81
L=0.1
rhob=8000.0
k=40.0
rholiq=1250
rhorf=2
m=rhob*L**3
xo=0.50
dt=0.1
t= 0

empuxo= Problema2(L, 0.51, 0)

tmax= 100

t= np.arange(0, tmax, dt)
x= np.zeros(t.size)
v= np.zeros(t.size)

x[0]= empuxo.x
v[0]= empuxo.v

for i in range(t.size):
	empuxo.movimento(t[i])
	x[i]= empuxo.x
	v[i]= empuxo.v
	


fig = plt.figure()
plt.title('Oscilador com Empuxo', fontsize=12)


XT=fig.add_subplot(331, xlim=(0, tmax), ylim=(min(x)*1.05, max(x)*1.05))
XT.xaxis.grid(True)
XT.yaxis.grid(True)
plt.setp(XT.get_xticklabels(), visible=False)
plt.xlabel('Tempo (s)')
plt.ylabel('Posicao (m)')
line1, = XT.plot([], [], 'y-', lw=2)
plt.legend(loc='upper right')


VT=fig.add_subplot(334, xlim=(0, tmax), ylim=(min(v)*1.05, max(v)*1.05))
VT.xaxis.grid(True)
VT.yaxis.grid(True)
plt.setp(VT.get_xticklabels(), visible=False)
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade(m/s)')
line2, = VT.plot([], [], 'r-', lw=2)
plt.legend(loc='upper right')


VX=fig.add_subplot(122, xlim=(min(x)*1.05, max(x)*1.05), ylim=(min(v)*1.05, max(v)*1.05))
VX.xaxis.grid(True)
VX.yaxis.grid(True)
plt.setp(VX.get_xticklabels(), visible=False)
plt.xlabel('Posicao (m)')
plt.ylabel('Velocidade (m/s)')
line3, = VX.plot([], [], 'g-', lw=1.0)
plt.legend(loc='upper right')


def init():
	line1.set_data([],[])
	line2.set_data([],[])
	line3.set_data([],[])
	return line1, line2, line3,
def animate(i):
	tt= t[:i]
	xx= x[:i]
	vv= v[:i]
	line1.set_data(tt, xx)
	line2.set_data(tt, vv)
	line3.set_data(xx, vv)
	return line1, line2, line3,


anim= animation.FuncAnimation(fig, animate, init_func= init, frames= t.size,
interval= 20, blit= True, repeat= False)


anim.save('emp.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


plt.show()

			
	
