#Iterator
'''
25/11/2019
Juan Carlos Rangel
allows you to cycle through its elements through an iterator,
the iterator is an interface that provides the necessary
methods to navigate the elements of the data structure,
'''
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class razas_Orden(Iterator):
    _posicion: int = None
    _reversa: bool = False

    def __init__(self, collection: Casta, reversa: bool = False) -> None:
        self._collection  = collection
        self._reversa = reversa
        self._posicion = -1 if reversa else 0

    def __next__(self):
        try:
            valor = self._collection[self._posicion]
            self._posicion += -1 if self._reversa else 1
        except IndexError:
            raise StopIteration()

        return valor


class Casta(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection
    def __iter__(self) -> razas_Orden:
        
        return razas_Orden(self._collection)

    def get_revez_iterator(self) -> razas_Orden:
        return razas_Orden(self._collection, True)

    def agregar_raza(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    casta  = Casta()
    casta.agregar_raza("Demon")
    casta.agregar_raza("Fairy")
    casta.agregar_raza("Giant")
    casta.agregar_raza("Magician")
    casta.agregar_raza("Human")
    casta.agregar_raza("Android")
    casta.agregar_raza("Beast")

    print("Razas superiores:")
    print("\n".join(casta))
    print("")

    print("Razas superiores inversas:")
    print("\n".join(casta.get_revez_iterator()), end="")

    
