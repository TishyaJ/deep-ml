import math
import numpy as np
def softmax(scores: list[float]) -> list[float]:
    # Your code here
    arr = np.array(scores)
    #normalising with respect to max score:
    norm = np.exp(arr-np.max(arr))
    prob = norm/np.sum(norm)
    return prob.tolist()
    pass