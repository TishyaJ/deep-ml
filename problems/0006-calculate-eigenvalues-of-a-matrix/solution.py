def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	#since it'2 2x2: characterisitc equation is quadratic equation where sum of eigenvalues = trace and product is determinant
	a = matrix[0][0]
	b=matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	det = a*d-b*c 
	trace = a+d 
	# lambda^2 - (trace) lambda + determinant = 0
	# ans = (trace +-(trace^2-4*det)**0.5)/2
	sqrtdet = (trace**2-4*det)**0.5
	ans1 = (trace+sqrtdet)//2
	ans2 = (trace-sqrtdet)//2
	eigenvalues = []
	eigenvalues.append(ans1)
	eigenvalues.append(ans2)
	return eigenvalues