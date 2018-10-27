import sympy as sp
import Coordinates
import Metric
import ChristoffelSymbol
import Curvature

#Initializes the Coordinate Information Dictionary and the number of dimensions from the user's input
coords = Coordinates.UsersCoordinates()
dim = len(coords) 

#Initializes a matrix containing just the variables that will be used (i.e. [x0, x1, ..., xn])
coordMatrix = sp.Matrix([sp.Symbol("x0")])
for i in range(0, dim):
    if(i > 0):    
        coordMatrix = coordMatrix.row_insert(i, sp.Matrix([sp.Symbol("x" + str(i))]))

#Calculates the Metric Tensor
metric1 = Metric.MetricTensor(coords)

#Calculates the Christoffel Symbols
cs = ChristoffelSymbol.ChristoffelSymbols(metric1, dim, coordMatrix)

#Prints out the Metric
print("\nMetric:")
sp.pprint(metric1, use_unicode=False)

#Prints out the Christoffel Symbol Matricies
for i in range(0, dim):
    print("\nC-" + str(coordMatrix[i]) + ":")
    sp.pprint(cs[str(i)], use_unicode=False)

#Calculates and prints the Ricci Curvature Tensor
for i in range(0, dim):
    print("\nR-x" + str(i))
    print("-----")
    for j in range(0, dim):
        ricci = Curvature.RicciTensor(metric1, coordMatrix, dim, i, j)
        print(ricci)

#Calculates and prints the Ricci Scalar and Gaussian Curvature
R = Curvature.RicciScalar(metric1, coordMatrix, dim)
print("\nR =", R, "\n")
print("k =", R / 2, "\n")