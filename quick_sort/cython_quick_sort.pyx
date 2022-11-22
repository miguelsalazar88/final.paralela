# cython: language_level=3

import cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef double[:] qsort_kernel_cython(double[:] a, int lo, int hi):
    cdef int i, j
    cdef double pivot

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
            qsort_kernel_cython(a, lo, j)
        lo = i
        j = hi
    return a