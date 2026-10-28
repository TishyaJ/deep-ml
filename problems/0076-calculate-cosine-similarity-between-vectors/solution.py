import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	a1 = np.array(v1)
	a2 = np.array(v2)
	dotp= np.dot(a1,a2)
	norm1 = np.linalg.norm(a1)
	norm2 = np.linalg.norm(a2)
	ans = float(dotp/(norm1*norm2))
	return ans