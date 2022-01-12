class BinHeap(object):
    
    def __init__(self, list_keys):
        self._keys = list_keys
        self.tree_dimension = len(list_keys)
     
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def heapify(self, i):
        L = self.left(i)
        R = self.right(i)
        largest = i
        if L < self.tree_dimension and self._keys[L] > self._keys[largest]:
            largest = L
        if R < self.tree_dimension and self._keys[R] > self._keys[largest]:
            largest = R
        if largest != i:
            tmp = self._keys[i]
            self._keys[i] = self._keys[largest]
            self._keys[largest] = tmp
            self._keys = self.heapify(largest)
        return self._keys
    
    def build_heap(self):
        '''
        poichè tutti gli elementi del sottoarray dopo n/2 + 1 sono foglie dell'albero, ognuna è una heap
        di un solo elemento.
        La procedure build_heap attraversa i restanti nodi dell'albero ed esegue Heapify su ognuno di essi.
        '''
        for i in range(self.tree_dimension//2, -1, -1):
            self.heapify(i)
        return self._keys
    
    def heapsort(self):
        '''
        L'algoritmo comincia costruendo una heap sull'array di input. 
        L'elemento più grande dell'array è posto nella radice quindi può essere posto nella corretta posizione finale. 
        Posso facilmente trasformare la lista rimanente in una Heap, infatti:
        - I figli della radice rimangono heap 
        - L'unico elelmento che può violare la proprietà di ordinamento parziale delle heap è la radice
        Applico Heapify() al primo elemento e lo metto nella posizione corretta. 
        '''
        self._keys = self.build_heap()
        for i in range(self.tree_dimension -1, 0, -1):
            tmp = self._keys[i]
            self._keys[i] = self._keys[0]
            self._keys[0] = tmp
            self.tree_dimension = self.tree_dimension - 1
            self.heapify(0)
        return self._keys
    
    def __repr__(self):
        bt_str = '['

        level = 0
        next_level = 2 ** level
        for i in range(0, self.tree_dimension):
            bt_str += '{}'.format(self._keys[i])
            if i + 1 < self.tree_dimension:
                if next_level == i + 1:
                    bt_str += ']\n['
                else:
                    bt_str += ' '
            if next_level == i + 1:
                level += 1
                next_level += 2 ** level

        return bt_str + ']'
