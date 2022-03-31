# OTTO SIMULATOR
import math
import matplotlib.pyplot as plt

def engine_kinematics(bore, stroke, con_rod, cr, start_crank, end_crank):
    """
    # engine kinematics
    """
    # geometric parameters
    a = stroke/2
    R = con_rod/a

    # volume parameters
    V_s = math.pi*(1/4)*pow(bore, 2)*stroke  # swept volume
    V_c = V_s/(cr-1)  # clearence volume

    sc = math.radians(start_crank)
    ec = math.radians(end_crank)

    num_values = 50
    dtheta = (ec-sc)/(num_values-1)

    V = []
    for i in range(0, num_values):
        theta = sc + i*dtheta
        #print(theta)
    # 0 Degree means the crank is at TDC and at 180 it is at BDC
    # print(theta)
        term1 = 0.5 * (cr - 1)
        term2 = R+1-math.cos(theta)
        term3 = pow(R, 2)-pow(math.sin(theta), 2)
        term3 = pow(term3, 0.5)

        V.append((1+term1*(term2-term3))*V_c)
        #print(V)
    return V # value will be returned

#inputs
p1 = 101325
t1 = 500
gamma = 1.4
t3 = 2300
# geometric paramter
bore = 0.1
stroke = 0.1
con_rod = 0.15
cr = 12  #if compression ratio is reduced the pressure will also decreased

#volume computation
v_s = (math.pi/4)*pow(bore, 2)*stroke
v_c = v_s/(cr-1)
v1 = v_c + v_s

#state point 2
v2 = v_c

#p2v2*gamma = p1v1*gamma
p2 = p1*pow(v1, gamma)/pow(v2, gamma)
#print(p2)

# p2v2/t2 = p1v1/t1 | rhs = p1v1/t1 |p2v2/t2 = rhs | t2 = p2v2/rhs
rhs = p1*v1/t1
t2 = p2*v2/rhs
#print(t2) # if cr is reduced temprature also drop
V_compression = engine_kinematics(bore, stroke, con_rod, cr, 180, 0)

constant = p1*pow(v1, gamma)

P_compression = []

for v in V_compression:
    P_compression.append(constant/pow(v, gamma))
    print(P_compression)
print(P_compression)
#state point 3
v3 = v2
#p3v3/t3 = p2v2/t2 | rhs =p2v2/t2 | p3 = rhs*t3/v3
rhs =p2*v2/t2
p3 = rhs*t3/v3
# print(p3 > p2)
V_expansion = engine_kinematics(bore, stroke, con_rod, cr, 0,180)

constant = p3*pow(v3, gamma)

P_expansion = []

for v in V_expansion:
    P_expansion.append(constant/pow(v, gamma))


#state point 4
v4 = v1
p4 = p3*pow(v3, gamma)/pow(v4, gamma)

# p4v4/t4 = p3v3/t3

t4 = p4*v4/rhs
#print(t4)
plt.plot([v2, v3], [p2, p3])
plt.plot(V_compression, P_compression)
plt.plot(V_expansion, P_expansion)
plt.plot([v4, v1], [p4, p1])
plt.show()
#print(V) #Answer will be none
