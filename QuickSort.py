#!/usr/bin/env python
# coding: utf-8

# ## QUICKSORT
# 
# Metodo basato sul paradigma di _divide et impera_.
# Implementeremo:
# - La funzione _partition_ che risistema il sottoarray A[p,...,r] in loco.
# - La funzione _quicksort_ per l'ordinamento 
# 

# In[41]:


A = [1, 2, 38, 7, 4, 7, 88, 130, 0]
A2 = [1, 2, 38, 7, 4, 7, 88, 130, 0]


# In[42]:


def partition(A, p, r):
    '''
    Funzione che partiziona l'insieme. 
    Ripartisce gli elementi del vettore rispetto al valore a dell'ultima componente. 
    Restituisce un indice i che gode delle seguenti proprietà :
    - A[i] assume il valore a
    - A[p, i-1] contiene i valori minori o uguali a a 
    - A[i+1, r] contiene i valori maggiori o uguali a a 
    '''
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


# Cosa ci aspettiamo di ottenere applicando la funzione partition? Indoviniamo!
# Come ci aspettiamo che sia A dopo l'applicazione della funzione? 

# In[43]:


# partition(A, 0, len(A)-1)
# A


# In[45]:


# partition(A2, 1, 5)
# A2


# In[2]:


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A


# In[8]:


A = [1, 2, 38, 7, 4, 7, 88, 74, 32, 89, 56, 6, 31, 100, 130, 0]


# In[5]:


quicksort(A, 0, len(A)-1)

