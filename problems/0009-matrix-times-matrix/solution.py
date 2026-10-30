import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
            l = np.array(a)
            r = np.array(b)
            #we want columns no of l to be equal to row no of r 
            if (l.shape[1] != r.shape[0]):
                return -1
            c = np.matmul(l,r)

            return c.tolist()