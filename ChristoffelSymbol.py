import sympy as sp
import Coordinates
import Metric

#Function to calculate ChristoffelSymbol(a, bc) using C(a, bc) = (1/2)*g^ad*(gdc,b + gab,c + gbc,d)
def CalculateComponents(g, coordMatrix, dims, a, b, c):
    
    #Initialize the component(cs)
    cs = 0
    
    #Loop to sum over the possible values of d (0 -> (# of dimensions - 1))
    for i in range(0, dims):
        
        #Get the coordinates from the coordinate matrix so they can be used for derivatives
        a1 = coordMatrix[a]
        b1 = coordMatrix[b]
        c1 = coordMatrix[c]
        d1 = coordMatrix[i]
        
        #Get all of the necessary components of the metric
        d = i
        gad = g[a, d]
        gdc = g[d, c]
        gab = g[a, b]
        gbc = g[b, c]
        
        #Compute the i value of the component and add it in
        if(gad != 0):
            cs += (1 / 2) * (1 / gad) * (sp.diff(gdc, b1) + sp.diff(gab, c1) - sp.diff(gbc, d1))   
    return cs

#Function that creates a dictionary containing all the matricies representing the christoffel symbols C(x0, ..), C(x1, ..), ..., C(xn, ..)
def ChristoffelSymbols(g, dimensions, coordMatrix):
    
    #Initializes the christoffel symbol component(cs), the metric, the number of dimensions and the dictionary
    cs = 0
    metric = g
    dims = dimensions
    coords = coordMatrix
    csDict = {
    }
    
    #Sets the metric as a placeholder matrix in place of the Christoffol Symbol Matricies since the metric is the correct shape (same number of dimensions)
    for i in range(0, dims):
        csDict[str(i)] = metric
    
    #This loop creates the Christoffel Matricies and inserts them into the dictionary
    for i in range(0, dims):
        #Initializes a, which will become the ith Christoffel Matrix
        a = sp.Matrix([0])
        for x in range(0, dims-1):
            a = a.row_insert(x+1, sp.Matrix([0]))
        a1 = a
        for x in range(0, dims-1):
            a = a.col_insert(x+1, a1)
        
        #This loop calculates the C(i, jk) component and enters it into a[j, k] (ended up adding b as a buffer variable due to a weird bug) then the final matrix is entered into the dictionary
        for j in range(0, dims):
            for k in range (0, dims):
                cs = CalculateComponents(metric, coordMatrix, dims, i, j, k)
                a[j, k] = cs
                b = a
        csDict[str(i)] = b
    return csDict