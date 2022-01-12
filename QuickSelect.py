def minimum(A):
    minim = A[0]
    for i in range(1,len(A)):
        if minim > A[i]:
            minim = A[i]
    return minim

A = [random.randint(1, 100) for i in range(10)]

print("Lista considerata :\t" + str(A))
print("Minimo elemento :\t" + str(minimum(A)))

def partition(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def median_helper(A, p, r):
    # assumiamo len(A) dispari, c'è un poco di lavoro in più
    # se len(A) è pari
    middle = len(A)//2
    q = partition(A, p, r)
    if q == middle:
        return A[q]
    elif q < middle:
        return median_helper(A, q+1, r)
    else:
        return median_helper(A, p, q-1)


def median(A):
    return median_helper(A, 0, len(A)-1)


import random
A = [random.randint(1, 100) for i in range(100000)]

median(A)
