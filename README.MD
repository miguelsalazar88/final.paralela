README.MD

Para el desarrollo de esta práctica experimental se escribieron, en dos lenguajes de programación (Python y Cython), cuatro pequeños programas que implementan dos algoritmos de ordenamiento de números en un arreglo de dimensión N. Esto con el fin de efectuar una comparación de rendimiento entre los dos lenguajes.

Archivos:

- insertion_sort

  1. cython_insertion_sort.pyx
  2. python_insertion_sort.py
  3. Makefile
  4. setup.py
  5. utils.py
  6. main.py
  7. lanzador.pl

- quick_sort:

  1. cython_quick_sort.pyx
  2. python_quick_sort.py
  3. Makefile
  4. setup.py
  5. utils.py
  6. main.py
  7. lanzador.pl

Instrucciones de uso:

Nota: Resulta importante dar permisos de ejecución, lectura y escritura a los archivos lanzador.pl contenidos en cada uno de los ficheros, mediante el comando:

sudo chmod 777 lanzador.pl

En una ventana de Terminal ubicada en las carpetas principales de cada algoritmo, crear el objeto compartido para el uso de Cython mediante el siguiente comando:

make all

Acto seguido, ejecutar el archivo lanzador mediante el siguiente comando:

perl lanzador.pl
