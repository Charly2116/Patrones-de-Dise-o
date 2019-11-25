#Iterator
'''
25/11/2019
Juan Carlos Rangel
allows you to cycle through its elements through an iterator,
the iterator is an interface that provides the necessary
methods to navigate the elements of the data structure,
'''


from abc import ABC, abstractmethod

class conta(ABC):
    def count(cont):

        Raza = ['Demon', 'Fairy', 'Giant',
                'Magician', 'Human', 'Android', 'Beast']
    
        itera = zip(range(cont), Raza)
        
        for position, number in itera:
              yield number

#---------------------------------------------------------
class main():
    raza = conta()
    for num in count(4):
        print("{}".format(num))
    
    raza2 = Raza()
    for num in count(7):
        print("{}".format(num))
   
    
