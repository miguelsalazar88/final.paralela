import time
import random

def generate_nums(n):
    return [random.randint(-n,n) for _ in range(n)]

def timeit(func=None, *args, **kwargs):
    tiempo1 = time.time()
    resultado = func(*args, **kwargs)
    tiempo2=time.time()

    return (resultado, tiempo2-tiempo1)