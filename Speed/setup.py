from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('example_cy.pyx'))
setup(ext_modules = cythonize('example_two_cy.pyx'))
setup(ext_modules = cythonize('example_three_cy.pyx'))


