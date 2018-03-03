cpdef int test(float a):
	x = 600851475143
	cdef int i = 2
	cpdef list b = []

	while i < a:
		if int(x / i) == float(x / i):
			x = x / i
			if x == 1:
				break
		else:
			i +=1