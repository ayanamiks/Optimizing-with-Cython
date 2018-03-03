cpdef int test(int x):
	cdef int b = 0
	cdef int i
	for i in range(x):
		if i % 3 == 0 or i % 5 == 0:
			b += i
	return b
