import math
import matplotlib.pyplot as plt

#Input values for physical parameters
g = input("Enter the gravitational acceleration in m/s^2 (1g = 9.81 m/s^2): ")
m = input("Enter the mass of the object in kg: ")
rho = input("Enter the air density in kg/m^3 (STP = 1.25 kg/m^3): ")
cd_or_shape = input("Choose one of the following shapes of the object, or input a custom drag coefficient \n Sphere, Half-Sphere, Cone, Cube, Angled Cube, Long Cylinder, Short-Cylinder, Airfoil, Flat Plate, Bullet: ")
A = input("Enter the cross-sectional area of the object in m^2: ")
v = input("Enter the initial velocity in m/s: ")
a = input("Enter the launch angle in degrees: ")
h = input("Enter the initial height of the object: ")

#Change int to float
g = float(g)
m = float(m)
rho = float(rho)
A = float(A)
v = float(v)
a = float(a)
h = float(h)

#Checks for cd
cd = 0
if isinstance(cd_or_shape, int):
    cd = float(cd_or_shape)
elif isinstance(cd, float):
    cd = cd_or_shape
else:
    if cd_or_shape == "Sphere" or "sphere":
        cd = 0.47
    if cd_or_shape == "Half-Sphere" or "Half Sphere" or "half sphere":
        cd = 0.42
    if cd_or_shape == "Cone" or "cone":
        cd = 0.50
    if cd_or_shape == "Cube" or "cube":
        cd = 1.05
    if cd_or_shape == "Angled Cube" or "angled cube":
        cd = 0.80
    if cd_or_shape == "Long Cylinder" or "long cylinder":
        cd = 0.82
    if cd_or_shape == "Short Cylinder" or "short cylinder":
        cd = 1.15
    if cd_or_shape == "Airfoil" or "airfoil":
        cd = 0.045
    if cd_or_shape == "Bullet" or "bullet":
        cd = 0.295
    if cd_or_shape == "Flat Plate" or "flat plate":
        cd = 1.28


#Physical constants
alpha = rho * cd * A / 2.0
beta = alpha / m

#Initial velocity components
Vx0 = v * math.cos(math.radians(a))
Vy0 = v * math.sin(math.radians(a))

dt = 0.001

X_WD = [0.0]  #X position
Y_WD = [h]  #Y position
Vx_WD = [Vx0]  #X velocity
Vy_WD = [Vy0]  #Y velocity
T = 0

#Simulating motion
i = 0
while Y_WD[i] >= 0:
    speed = math.sqrt(Vx_WD[i]**2 + Vy_WD[i]**2)

    Vx_WD.append(Vx_WD[i] * (1.0 - beta * speed * dt))
    Vy_WD.append(Vy_WD[i] + (-g - beta * Vy_WD[i] * speed) * dt)

    X_WD.append(X_WD[i] + Vx_WD[i] * dt)
    Y_WD.append(Y_WD[i] + Vy_WD[i] * dt)
    
    T += dt
    i += 1


plt.plot(X_WD, Y_WD)
plt.xlim([0, 1.1*max(X_WD)])
plt.ylim([0, 1.1*max(Y_WD)])
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion with Air Drag")
print("Max Height: " + str(round(max(Y_WD),3)) + " m")
print("Range: " + str(round(max(X_WD),3)) + " m")
print("Time of Flight: " + str(round(T,3)) + " s")
plt.show()
