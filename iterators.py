import time

class FiboIter():

    def __init__(self,max: int):
        self.max = max

    
    def __iter__(self):
        self.n1=0
        self.n2=1
        self.counter=0
        return self

        
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1

        elif self.counter == 1:
            self.counter += 1
            return self.n2
        
        else: 
            self.aux = self.n1 + self.n2
            if self.aux > self.max:
                raise StopIteration
            ### Se da un intercambio de datos entre n1, n2, aux
            #self.n1 = self.n2
            #self.n2 = self.aux
            
            self.n1, self.n2 = self.n2, self.aux ### Se hace un swap
            self.counter += 1
            return self.n2
            



if __name__ == "__main__":
    fibonacci = FiboIter(10000000000000000000000000000000000000000000000000000000)

    ### Se utiliza Sugar Syntax para recorrer el iterable
    for element in fibonacci:
        print(element)
