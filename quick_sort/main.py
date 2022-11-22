################################################################
# Fecha: 17 de Noviembre de 2022
# Autor: Miguel Salazar di Colloredo
# Proyecto: Tercer Parcial, Computación Paralela y Distribuida
# Tema: Comparación de rendimiento: Python vs Cython
################################################################ 

import sys
from utils import generate_nums
import time

import numpy as np
import python_quick_sort as p_sort
try:
    import cython_quick_sort as c_sort
except ModuleNotFoundError:
    print("No se encontró el módulo Cython Insertion Sort")

def main(n):
    values = np.random.random(n)
    ini_time = time.time()
    c_sort.qsort_kernel_cython(values,0,len(values)-1)
    fin_time = time.time()

    time_cython = fin_time - ini_time

    ini_time = time.time()
    p_sort.quick_sort(values, 0,len(values)-1)
    fin_time = time.time()

    time_python = fin_time - ini_time
    
    print(f'{time_cython:.12f},{time_python:.12f}')

if __name__ == '__main__':
    n = int(sys.argv[1])
    main(n)
