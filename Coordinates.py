import sympy as sp

#Gets the Coordinate Information from the User and inputs it into a dictionary
def UsersCoordinates():
    
    #Get the desired number of dimensions from the user and initializes the coordinate dictionary
    dim = input("Number of Dimensions: ")
    dim = int(dim)
    coords = {
        }
    
    #The Variables the user enters must be formatted like x0 and x1 rather than x and y
    print("\nEnter Variables in x0, x1, ..., xn Format(rather than x, y, z...):")
    
    #Loop through each dimension and get its Coordinate Information from the user
    for i in range(0, dim):
       coords["x" + str(i)] = input("x" + str(i) + " = ")
    return coords

#Predefined Coordinate Systems *Not in use*
#-----------------------------------------#
t = sp.Symbol("t")
x = sp.Symbol("x")
y = sp.Symbol("y")
z = sp.Symbol("z")
u = sp.Symbol("u")
v = sp.Symbol("v")
def Cartesian():    
    t1 = t
    x1 = x
    y1 = y
    z1 = z
    coordDict = {
        "x0" : t1,
        "x1" : x1,
        "x2" : y1,
        "x3" : z1
        }
    return coordDict
def TwoSphere():
    t1 = sp.Symbol("t")                                            
    x1 = 1 * sp.cos(z) * sp.sin(y)
    x2 = 1 * sp.cos(y)
    x3 = 1 * sp.sin(z) * sp.sin(y)
    coordDict = {
        "x0" : t1,
        "x1" : x1,
        "x2" : x2,
        "x3" : x3
    }
    return coordDict
def Spherical():
    t1 = sp.Symbol("t")                                            
    x1 = x * sp.cos(z) * sp.sin(y)
    x2 = x * sp.cos(y)
    x3 = x * sp.sin(z) * sp.sin(y)
    coordDict = {
        "x0" : t1,
        "x1" : x1,
        "x2" : x2,
        "x3" : x3
    }
    return coordDict
def ParametricSphere():
    t = sp.Symbol("t")
    u = sp.Symbol("u")
    v = sp.Symbol("v")
    x = sp.cos(v) * sp.sin(u)
    y = sp.cos(u) + 1
    z = sp.sin(v) * sp.sin(u)
    coordMatrix = sp.Matrix([x, y, z])
    return coordMatrix
def Parametric():
    x = input("x(u, v): ")
    y = input("y(u, v): ")
    z = input("z(u, v): ")
    paraSurface = {
        "x0" : x,
        "x1" : y,
        "x2" : z 
        }
    return paraSurface
#-----------------------------------------#