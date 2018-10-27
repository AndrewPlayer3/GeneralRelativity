import sympy as sp
import Coordinates
import Metric
import ChristoffelSymbol as CS
from ChristoffelSymbol import CalculateComponents as CCs

#Calculates the R(a, bcd) component of the Riemann Tensor using C(a, bd),c - C(a, bc),c + (C(i, bd)*C(a, ic) - C(i, bc)*C(a, id))
def RiemannTensorComponents(metric, coordMatrix, dims, a, b, c, d):
    
    #Initialize C(a, bd) and C(a, bc)
    csabd = CCs(metric, coordMatrix, dims, a, b, d)
    csabc = CCs(metric, coordMatrix, dims, a, b, c)
    
    #Initializes the csuMatrix(the C(i, bd)*C(a, ic) - C(i, bc)*C(a, id) part of the component) and component variables
    csuMatrix = 0
    component = 0
    
    #Sums C(i, bd)*C(a, ic) - C(i, bc)*C(a, id) over i where i is each of the dimensions
    for i in range(0, dims):
        csuMatrix += (CCs(metric, coordMatrix, dims, i, b, d)*CCs(metric, coordMatrix, dims, a, i, c)) - (CCs(metric, coordMatrix, dims, i, b, c) * CCs(metric, coordMatrix, dims, a, i, d))
    
    #Computes the final value of the component
    component = (sp.diff(csabd, coordMatrix[c]) - sp.diff(csabc, coordMatrix[d])) + csuMatrix
    
    return component

#Calculates the R(u, v) component of the Ricci Tensor
def RicciTensor(metric, coordMatrix, dim, u, v):
    
    #Initialize the component
    ricci = 0
    
    #Computes it using the above funtion with the R(i, uiv) = R(u, v) identity
    for i in range(0, dim):
        ricci += RiemannTensorComponents(metric, coordMatrix, dim, i, u, i, v)
    
    return ricci

#Calculates the Ricci Scalar
def RicciScalar(metric, coordMatrix, dims):
    
    #Initialize the Ricci Scalar
    R = 0
    
    #Computes the trace of g^uv*Ruv by summing over the components of their diagonals
    for i in range(0, dims):    
        if(metric[i, i] != 0):
            guv = 1 / metric[i, i]
            Ruv = RicciTensor(metric, coordMatrix, dims, i, i)
            R += guv * Ruv
    
    return R

#-----------No Longer Working-----------#
def FirstFundementalForm(metric):
    fff = metric
    return fff
def SecondFundementalFormVector(paraCoords):
    M = CoordSys3D('M')
    u = sp.Symbol("u")
    v = sp.Symbol("v")
    a = paraCoords["x0"] * M.i
    b = paraCoords["x1"] * M.j
    c = paraCoords["x2"] * M.k
    r = a + b + c
    n1 = sp.diff(r, u)
    n2 = sp.diff(r, v)
    n0 = n1.cross(n2)
    print(sp.simplify(n0))
    print(sp.simplify(sp.sqrt(n0.dot(n0))))
    n = n0/(sp.sqrt(n0.dot(n0)))
    l = sp.diff(n1, u)
    print(sp.simplify(l))
    L = sp.simplify(l.dot(n))
    m = sp.diff(n1, v)
    M = sp.simplify(m.dot(n))
    nN = sp.diff(n2, v)
    N = nN.dot(n)
    second = sp.Matrix([[L, M], [M, N]])
    return second
def SecondFundementalForm(paraCoords):
    u = sp.Symbol("x1")
    v = sp.Symbol("x2")
    x1 = sp.Symbol("x1")
    x2 = sp.Symbol("x2")
    y = paraCoords["x0"]
    u = paraCoords["x1"]
    i = paraCoords["x2"]
    a = y
    b = u
    c = i
    print(a, b, c)
    r = sp.Matrix([a, b, c])
    n1 = sp.diff(r, u)
    n2 = sp.diff(r, v)
    n0 = sp.simplify(n1.cross(n2))
    n = sp.simplify(n0 / (n0.norm()))
    l = sp.diff(r, u, u)
    L = sp.simplify(n.dot(l))
    m = sp.diff(r, u, v)
    M = sp.simplify(n.dot(m))
    nN = sp.diff(r, v, v)
    N = sp.simplify(n.dot(nN))
    second = sp.Matrix([[L, M], [M, N]])
    return second
def GaussianCurvature(firstFund, secondFund):
    E = firstFund[0, 0]
    F = firstFund[0, 1]
    G = firstFund[1, 1]
    e = secondFund[0, 0]
    f = secondFund[0, 1]
    g = secondFund[1, 1]
    Gaussian = (e*g - f*f)/(E*G - F*F)  
    return sp.simplify(Gaussian)