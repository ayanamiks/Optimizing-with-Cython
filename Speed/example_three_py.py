def test(a):	
	x = 600851475143
	i = 2
	b = []

	while i < a:
		if int(x / i) == float(x / i):
			x = x / i
			if x == 1:
				break
		else:
			i +=1