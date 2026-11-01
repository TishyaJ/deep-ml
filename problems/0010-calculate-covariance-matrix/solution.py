import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	n_features = len(vectors)
	obs = len(vectors[0]) #observations in each vector
	mean = [np.mean(i) for i in vectors]
	
	cov_matrix = [[0.0]* n_features for _ in range(n_features)]

	
	for i in range(n_features):
		for j in range(n_features):
			num = 0.0
			for k in range(obs):
				num += (vectors[i][k] - float(mean[i])) * (vectors[j][k]-float(mean[j]))
			cov_matrix[i][j] = num/(obs-1)
	return cov_matrix