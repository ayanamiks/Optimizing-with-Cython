import timeit

problem_one_cy = timeit.timeit('example_cy.test(1001)', setup='import example_cy', number=100)
problem_one_py = timeit.timeit('example_py.test(1001)', setup='import example_py', number=100)

problem_two_cy = timeit.timeit('example_two_cy.test(4000000)', setup='import example_two_cy', number=100)
problem_two_py = timeit.timeit('example_two_py.test(4000000)', setup='import example_two_py', number=100)

problem_three_cy = timeit.timeit('example_three_cy.test(600851475143)', setup='import example_three_cy', number=100)
problem_three_py = timeit.timeit('example_three_py.test(600851475143)', setup='import example_three_py', number=100)





print('problem_one_cy:', problem_one_cy, 'problem_one_py:', problem_one_py, 'Cython в {} быстрее'.format(problem_one_py/problem_one_cy))
print('problem_two_cy:', problem_two_cy, 'problem_two_py:', problem_two_py, 'Cython в {} быстрее'.format(problem_two_py/problem_two_cy))
print('problem_three_cy:', problem_three_cy, 'problem_three_py:', problem_three_py, 'Cython в {} быстрее'.format(problem_three_py/problem_three_cy))


