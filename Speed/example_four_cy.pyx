cpdef int test():
	cpdef list q = []
	cdef int i
	cdef int b
	for i in range(100, 1000):
		b = 100
		while b <= 1000:	
			variable = str(i * b)
			if variable == variable[::-1]:
				q.append(int(variable))
				b +=1
			else:
				b +=1		