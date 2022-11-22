from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("cython_quick_sort.pyx"))
setup(ext_modules = exts)