def test(x):
	y = [1,2]
	while y[len(y) - 1] + y[len(y) - 2] < x:
		y.append(y[len(y) - 1] + y[len(y) - 2])

	i = 1
	b = 0
	while len(y)-i != 0:
		if y[len(y)-i] % 2 == 0:
			b += y[len(y)-i]
		i +=1
	return b	
