from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("cython_insertion_sort.pyx"))
setup(ext_modules = exts)