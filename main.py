import matplotlib.pyplot as plt
import numpy as np
import math
def calc_y(s,tau):
    y=[]
    t=0
    t0=0
    s0=0
    for i in range(2000):
        if s[i] < s0*np.exp(-1*(t-t0)/tau):
            y.append(s0*np.exp(-1*(t-t0)/tau))
        else:
            y.append(s[i])
            s0=s[i]
            t0=t
        t=t+0.001

    return y
ts=0
tf=2
tstep=0.001
t=np.arange(ts,tf,tstep)
ac=1
u=0.25
fm=1
fc=25
am=1


m=am*np.cos(2*np.pi*fm*t)

c=ac*np.cos(2*np.pi*fc*t)

s=ac*(1+u*m)*c

md=np.abs(ac*(1+u*m))


plt.subplot(711)
plt.plot(t,m)
plt.xlabel("time in sec")
plt.ylabel("m(t)")
plt.title("message signal m(t)")
plt.ylim(-2,2)
plt.subplot(713)
plt.plot(t,c)
plt.xlabel("time in sec")
plt.ylabel("c(t)")
plt.title("carer signal c(t)")
plt.ylim(-2,2)
plt.subplot(715)
plt.plot(t,s)
plt.xlabel("time in sec")
plt.ylabel("s(t)")
plt.title("modulated signal s(t)")
plt.ylim(-2,2)
plt.subplot(717)
plt.plot(t,md)
plt.xlabel("time in sec")
plt.ylabel("D(t)")
plt.title("Demodulated signal D(t)")
plt.ylim(-1,2)
plt.show()
taui=1/fc
tauf=1/fm

taulist =np.arange(taui,tauf,0.01)
y=[]
Dist=[]

for i in range(len(taulist)):
    y=calc_y(s,taulist[i])
    integral=0
    for i in range(2000):
        integral+=np.power(y[i]-md[i],2)
    Dist.append(integral/len(s))


minerror=Dist.index(min(Dist))

taulesseroor=taulist[minerror]

y=calc_y(s,taulesseroor)

plt.plot(taulist,Dist)
plt.annotate('minimum value' +"( Tau ="+str(format(taulesseroor,".2f"))+",Dist ="+str(format(min(Dist),".4f"))+")", xy=(taulesseroor, min(Dist)), xytext=(0.4, 0.02),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.xlabel("Tau values fom a/fc to 1/fm")
plt.ylabel("Distortion")
plt.title("Tau Vis Distortion")
plt.show()
plt.plot(t,y,label="y(t)")
plt.plot(t,s,label="s(t)")
plt.legend()
plt.xlabel("time in sec")
plt.ylabel("S(t) and Y(t)")
plt.title("y(t) with less error comparing with s(t)")
plt.show()
plt.plot(t,y,label="y(t)")
plt.plot(t,md,label="ideal demodulated signal")
plt.legend()
plt.xlabel("time in sec")
plt.ylabel("Md(t) and Y(t)")
plt.title("y(t) comparing with Demodulated signal md ")
plt.show()
plt.plot(t,y)
plt.xlabel("time in sec")
plt.ylabel("Y(t)")
plt.title("non Ideal demodulated signal with best tau value")
plt.show()