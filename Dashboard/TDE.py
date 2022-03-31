import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# a funtion that returns dz/dt
def mode1(theta, t, b, g, l, m):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = -(b/m)*theta2 - (g/l)*math.sin(theta1)
    dtheta_dt = [dtheta1_dt, dtheta2_dt]
    return dtheta_dt

b = 0.05 # damping coefficient if incresed the pendulum will die swinging faster
g = 9.81
l= 1 #length of pendulem
m =0.1 # mass

    # intitial condition
theta_0 = (0,5)#for displacement stationary and giving velocity 5m/s

# time points

t = np.linspace(0, 10, 150) #time array using numpy array

# solve ODE #solving ode without scipay it will not work
theta = odeint(mode1, theta_0, t, args = (b, g, l, m))

#plot resuts
plt.plot(t,theta[:,0],'b-',label=r'$\frac{d\theta_1}{dt}=\theta2$') #displacement values
plt.plot(t,theta[:,1],'r--',label=r'$\frac{d\theta2}{dt}=-\frac{b}{m}\theta_2-\frac{g}{l}sin\theta_1$') #velocity values
plt.ylabel('Plot')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
