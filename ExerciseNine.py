import math
a= 9.81
v = 44
deg = 80
theta = (deg * (math.pi/180))
x = 0.5
hB = 1

leftside = (hB + (x * (math.tan(theta))))

topright = (a * (x**2))

bottomright = (2 * ((v*(math.cos(theta))))**2)

rightside = topright / bottomright

answer= leftside - rightside
print(answer)