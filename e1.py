#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation as animation
import math

class Problema2:
	def __init__(self, L, z, v):
		self.m= rhob*(L**3)
		self.L= L
		self.z= z
		self.v= v
		
	def a(self, z, v):
		return (((rhob-rholiq)*g*(self.L**3))-( (k/self.m)*(z-zo) )- (rhorf*v))/self.m


	def movimento(self, t):
		at= self.a(self.z, self.v)
		self.z= self.z + self.v*dt + 0.5*at*(dt**2)
		atem= self.a(self.z, self.v)
		vtem= self.v + 0.5*(at+atem)*dt
		atem= self.a(self.z, vtem)
		self.v= self.v + 0.5*(at+atem)*dt
		self.at= self.a(self.z, self.v)


g=9.81
L=0.1
rhob=8000.0
k=40.0
rholiq=1000
rhorf=2
m=rhob*L**3
zo=0.50
dt=0.001
t= 0

empuxo= Problema2(L, 0.51, 0)

tmax= 100

t= np.arange(0, tmax, dt)
z= np.zeros(t.size)
v= np.zeros(t.size)

z[0]= empuxo.z
v[0]= empuxo.v

for i in range(t.size):
	empuxo.movimento(t[i])
	z[i]= empuxo.z
	v[i]= empuxo.v
	
plt.figure(figsize=(6,5), dpi=96)
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()


plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade')
#plt.ylabel(r'Posi\c{c}\~{a}o (m) e Velocidade (m/s)')

plt.title(r'Posi\c{c}\~{a}o x Tempo ', fontsize=12)
plt.grid()
#plt.plot(t,v,'g-', linewidth=2)
plt.plot(t,z,'b-', linewidth=2)

plt.legend(loc='upper right')
plt.savefig("aguax.pdf", dpi=96)


plt.show()			
	
