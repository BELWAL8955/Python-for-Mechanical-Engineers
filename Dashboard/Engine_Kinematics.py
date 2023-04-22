# engine kinematics

# geometric parameters
import math
import matplotlib.pyplot as plt

# inputs
bore = 0.10
stroke = 0.1
con_rod = 0.15
cr = 12
a = stroke/2
R = con_rod/a

# volume parameters
V_s = math.pi*(1/4)*pow(bore, 2)*stroke  # swept volume
V_c = V_s/(cr-1)  # clearence volume

theta = math.radians(85)  # 0 Degree means the crank is at TDC and at 180 it is at BDC
# print(theta)

term1 = 0.5*(cr-1)
term2 = R+1-math.cos(theta)
term3 = pow(R, 2)-pow(math.sin(theta), 2)
term3 = pow(term3, 0.5)

V = (1+term1*(term2-term3))*V_c

#print(V_c+V_s)
#print(V_c)
#print(V)
