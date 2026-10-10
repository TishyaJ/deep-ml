import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    #rows-> cols and cols->rows
    arr = np.array(a)
    #transpose = np.transpose(arr)
    #transpose = arr.T
    transpose = np.swapaxes(arr, 0, 1)
    result = transpose.tolist()
    return result