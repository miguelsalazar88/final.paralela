################################################################
# Fecha: 17 de Noviembre de 2022
# Autor: Miguel Salazar di Colloredo
# Proyecto: Tercer Parcial, Computación Paralela y Distribuida
# Tema: Comparación de rendimiento: Python vs Cython
################################################################ 

# Crédito: Cliburn Chan, Janice McCarthy
# Disponible en: 
# https://people.duke.edu/~ccc14/cspy/18E_Benchmarks.html#Quicksort

def quick_sort(a, lo, hi):
    i = lo
    j = hi
    while i < hi:
        pivot = a[(lo+hi) // 2]
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if lo < j:
            quick_sort(a, lo, j)
        lo = i
        j = hi
    return a