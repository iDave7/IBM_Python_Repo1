class Repetidor():    # Construimos un iterador e iterable propio

    def __init__(self, veces, item):
        self.veces = veces
        self.item = item
        self.counter = 0
    
    def __next__(self): # Esto lo convierte en iterador
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido')
        self.counter += 1
        return self.item    

    def __iter__(self): # Esto lo convierte en iterable
        return self


for r in Repetidor(3, 'Python!'):
    print(r, end=' ')