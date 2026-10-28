def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode=='row':
		return [sum(i)/len(i) for i in matrix]
	elif mode =='column':
		return [
			sum(matrix[i][j] for i in range(len(matrix))) / len(matrix) for j in range(len(matrix[0]))
		]
	return []
