################################################################
# Fecha: 17 de Noviembre de 2022
# Autor: Miguel Salazar di Colloredo
# Proyecto: Tercer Parcial, Computación Paralela y Distribuida
# Tema: Comparación de rendimiento: Python vs Cython
################################################################  

# Algoritmo Insertion Sort en Python puro

def sort(arreglo):
    n = len(arreglo)
    for i in range(1,n):
        j = i - 1

        while j >= 0 and arreglo[j] > arreglo[j+1]:
            arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
            j -= 1
    return arreglo