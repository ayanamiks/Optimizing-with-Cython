def test(x):
	b = 0
	for i in range(x):
		if i % 3 == 0 or i % 5 == 0:
			b += i
	return b
