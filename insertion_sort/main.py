################################################################
# Fecha: 17 de Noviembre de 2022
# Autor: Miguel Salazar di Colloredo
# Proyecto: Tercer Parcial, Computación Paralela y Distribuida
# Tema: Comparación de rendimiento: Python vs Cython
################################################################ 

import sys
from utils import generate_nums, timeit

import python_insertion_sort as p_sort
try:
    import cython_insertion_sort as c_sort
except ModuleNotFoundError:
    print("No se encontró el módulo Cython Insertion Sort")


def main(n):
    values = generate_nums(n)
    resultado_cython, tiempo_cython = timeit(c_sort.sort, values.copy())
    resultado_python, tiempo_python = timeit(p_sort.sort, values.copy())
    print(f'{tiempo_cython:.12f},{tiempo_python:.12f}')

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)



