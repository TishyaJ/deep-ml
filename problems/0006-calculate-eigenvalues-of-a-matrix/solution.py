
import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	arr = np.array(matrix)
	eigenvalues = np.linalg.eigvals(arr)
	sortedeigvals = sorted([float(i) for i in eigenvalues], reverse = True)
	return sortedeigvals