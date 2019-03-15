import numpy as np
from math import pi, cos, sin

S = np.matrix([[-0.5, 0.5, 0.5, -0.5],[-0.5, -0.5, 0.5, 0.5]])
S1 = np.matrix([[-0.5, 0.5],[-0.5, -0.5]])
S2 = np.matrix([[0.5, -0.5],[0.5, 0.5]])
# print("cos")
# print(cos(90/180 * pi))

# print(T)
#matricies can be sliced like arrays
#the following takes the first two collumns (0,1)
#matricies are accessed as [row, col]
# print(T[:,:2])

singleRotate90 = np.matrix([
    [round(cos(0.5*pi), 3)],
    [round(sin(0.5*pi), 3)]
])

doubleRotate90 = np.matrix([
    [round(cos(0.5*pi), 3),round(-sin(0.5*pi), 3)],
    [round(sin(0.5*pi), 3), round(cos(0.5*pi), 3)]
])

doubleRotate45 = np.matrix([
    [round(cos((pi*45)/180), 3),round(-sin((pi*45)/180), 3)],
    [round(sin((pi*45)/180), 3), round(cos((pi*45)/180), 3)]
])

doubleRotate30 = np.matrix([
    [round(cos((pi*30)/180), 3),round(-sin((pi*30)/180), 3)],
    [round(sin((pi*30)/180), 3), round(cos((pi*30)/180), 3)]
])

# print(doubleRotate45)

# print("first 2 collumns")
# print(S[:,:2]*doubleRotate45)

# print("last 2 collumns")
# print(S[:,2:4]*doubleRotate45)

A = np.matrix([[1,2],[3,4]])
B = np.matrix([[5,6],[7,8]])

print(S1)
print(S2*doubleRotate45)