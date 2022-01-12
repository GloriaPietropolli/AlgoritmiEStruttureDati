#!/usr/bin/env python
# coding: utf-8

# ### TUTORATO 5 : ALGORITMI DI ORDINAMENTO IN TEMPO LINEARE

# ### COUNTING SORT

# In[86]:


def counting(A, k):
    B = [0] * k # memoria di lavoro temporanea
    C = [0] * len(A)  # mantiene l'output ordinato
    for i in range(0, len(A)):
        # in un array temporaneo di dimensione pari all'intervallo di valori contiamo il numero di occorrenze 
        # di ciascun valore presente nell'array da ordinare 
        B[A[i]] += 1
    for i in range(1, len(B)):
        B[i] = B[i] + B[i-1]
    for i in range(len(A)-1, -1, -1):
        # poniamo ogni elemento di A[j] nella sua corretta posizione ordinata
        C[B[A[i]]-1] = A[i]
        B[A[i]] = B[A[i]] - 1
    return C


# In[87]:


A = [1, 3, 3, 1, 2, 2, 7, 7, 12, 0, 0]


# In[88]:


k = max(A) - min(A) + 1


# In[89]:


counting(A, k)


# ### BUCKET SORT

# In[90]:


def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1
    return A


# In[91]:


def bucket_sort(A):
    B = []
    n = len(A)
    for i in range(0, n):
        B.append([])
    for i in range(0, n):
        bucket = int(A[i] * n) 
        B[bucket].append(A[i])
    for i in range(0, n):
        B[i] = insertion_sort(B[i])
    C = []
    for i in range(0, n):
        C += B[i]
    return C


# In[92]:


A = [0.1, 0.3, 0.3, 0.1, 0.2, 0.2, 0.7, 0.7, 0, 0]


# In[93]:


bucket_sort(A)


# In[ ]:




