#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys

g=9.81
m=10.0
k=800
mi=0.5
angulo=0.707106781
N=7.07

t=[0.0]
x=[10.0]
v=[0.0]
a=[0.0]
e=[0.0]

Fel=-k*x[-1]
P=m*g*angulo
fat=mi*N

dt=0.01


while (t[-1] <= 300) :
	

	t.append(t[-1]+dt)
	x.append(x[-1] + v[-1]*dt + 0.5*a[-1]*dt**2)
	a.append((Fel+P-fat)/m)
	v.append(v[-1] + (0.5)*(a[-2] + a[-1])*dt)


plt.figure(figsize=(6,5), dpi=96)
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()


plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade')

plt.title(r'Velocidade x Tempo ', fontsize=12)
plt.grid()
#plt.plot(t, x, 'g-', linewidth=1, label='Posi\c{c}\~ao')
#plt.plot(t, v, 'b-', linewidth=1, label='Velocidade')
plt.savefig("a.pdf", dpi=96)

plt.legend(loc='upper right')
plt.savefig("a.pdf", dpi=96)


plt.show()	

