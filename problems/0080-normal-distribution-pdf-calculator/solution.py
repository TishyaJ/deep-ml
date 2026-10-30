import math

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
	pi = math.pi
	denom= math.sqrt(2*pi*(std_dev**2))
	z = (x-mean)/std_dev
	power = -1*(z**2)/2
	num = math.exp(power)
	val = num/denom
	return round(val,5)