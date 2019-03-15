from math import ceil
from math import sin
from math import cos
from math import pi
import numpy as np

def matrixToList(matrix2Convert):
    '''
    funct converts a 2d matrix to a 2d list
    '''

    listReturn = []
    for i in range(len(matrix2Convert)): # handles collums (neccesary to deal with points)
        listReturn.append([])
        for j in range(2): #handles rows
            listReturn[i].append(matrix2Convert.item(j, i)) #gets item row j collumn i

    return listReturn




def rotate(shape, angle):
    '''
    funct rotates a shape made of points by angle
    shape is a 2d array of points where shape[0][j] is x
    and shape[1][j] is y. each point is the relative displacement.
    angles should be in radians
    '''
    
    # nVerticies = ceil(len(shape[0]) / 2)    # this handles even numbered pointed 
    #                                         # shapes as well as odd numbered shapes, it
    #                                         # represents the number of rotations i.e. the 
    #                                         # number of verticies (for odd numberes a 
    #                                         # single point is included in this)
    # points2Rotate = []
    # verticies2Rotate = []

    # #removes the first point if there is an odd number of points (for matrix multiplication)
    # if(len(shape[0]) % 2 != 0):
    #     points2Rotate.append([[shape[0][0]],[shape[1][0]]])
    #     del shape[0][0]
    #     del shape[1][0]

    # #split shape up into single verticies (sides)
    # for i in range(0, len(shape[0]) - 1, 2):
    #     verticies2Rotate.append([[shape[0][i], shape[0][i + 1]], [shape[1][i], shape[1][i + 1]]])

    # #find the rotation matrix for a point and a vertex
    pointRotMatrix = np.matrix([[round(cos(angle), 10)],[round(sin(angle), 10)]])
    vertexRotMatrix = np.matrix([[round(cos(angle), 10), round(-sin(angle), 10)], [round(sin(angle), 10), round(cos(angle), 10)]])
    print(vertexRotMatrix*np.matrix(shape))
    # #get the rotated points and verticies and add them to a list
    # shapeRot = [[],[]]

    # for i in range(len(points2Rotate)):
    #     pointRot = matrixToList(np.matrix(points2Rotate[i])*pointRotMatrix)
    #     shapeRot[0] = shapeRot[0] + pointRot[0]
    #     shapeRot[1] = shapeRot[1] + pointRot[1]

    # for i in range(len(verticies2Rotate)):
    #     print(np.matrix(verticies2Rotate[i])*vertexRotMatrix)
    #     vertexRot = matrixToList(np.matrix(verticies2Rotate[i])*vertexRotMatrix)
    #     shapeRot[0] = shapeRot[0] + vertexRot[0]
    #     shapeRot[1] = shapeRot[1] + vertexRot[1]


    return shapeRot

# shape = [[-0.5, 0.5, 0.5, -0.5],[-0.5, -0.5, 0.5, 0.5]] #square
shape = [[0.25, 0.5, 0.25, -0.25, -0.5, -0.25], [-0.433, 0, 0.433, 0.433, 0, -0.433]] #hexagon
# shape = [[0.25, 0.5, 0.7, 0.3,-0.5,0.1],[-0.5,-0.2,0,1,0,-0.5]]
rotated = rotate(shape, pi/4)
# print(rotated)

##############
#SERVER STUFF#
##############
import requests

requestAddress = "http://localhost:80/baseShape"
data = {'x': shape[0], 'y': shape[1]}
requests.post(requestAddress, data)

requestAddress = "http://localhost:80/processRotation"
data = {'x': rotated[0], 'y': rotated[1]}
requests.post(requestAddress, data)
