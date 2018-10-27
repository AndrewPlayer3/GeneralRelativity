import sympy as sp
import Coordinates

#Calculates the Metric Tensor
def MetricTensor(coords):
    
    #Gets the number of dimensions by looking at the length of the Coordinate Dictionary
    dim = len(coords)
    
    #Initializes the Metrix Tensor
    metric = sp.Matrix([0])
    
    #Inserts the correct number of rows into the Metric Tensor
    for i in range(0, dim - 1):
        metric = metric.row_insert(i + 1, sp.Matrix([0]))
    
    #Inserts the correct number of columns into the Metric Tensor
    metric1 = metric
    for i in range(0, dim - 1):
        metric = metric.col_insert(i, metric1)
    
    #Creates a dim x 1 column-matrix containing all of the variables
    coordMatrix = sp.Matrix([sp.Symbol("x0")])
    for i in range(0, dim):
        if(i > 0):    
            coordMatrix = coordMatrix.row_insert(i, sp.Matrix([sp.Symbol("x" + str(i))]))
    
    #Double Loop to compute each element g[i,j] and insert it into the matrix
    for i in range(0, dim):
        for j in range(0, dim):
            #Initialize the i, j component of the metric tensor
            gij = 0
            
            #This is basically the Kronecker-Delta (g[i, j] is always zero when i != j)
            if(i != j):
                metric[i, j] = 0
            
            if(i == j):
                #Initialize xi and xj, (these are what will be differentiated with respect to)      
                xi = coordMatrix[i] 
                xj = coordMatrix[j]
                
                #This for-loop is the sum over r and s
                for r in range(0, dim):                         
                    #s must equal r just as i must equal j
                    s = r            
                    
                    #Creates string versions of r and s so that their cooresponding Coordinate Information can be pulled from the Coordinate Dictionary
                    rstr = str(r)
                    sstr = str(s)
                    yr = coords["x" + rstr]
                    ys = coords["x" + sstr]                        
                    
                    #Computes the current derivatives and adds them to gij
                    gij += sp.diff(yr, xi) * sp.diff(ys, xj)
                    gij = sp.simplify(gij)
                
                #Inserts gij into g[i, j] once the summation is complete 
                metric[i, j] = gij
    
    return metric