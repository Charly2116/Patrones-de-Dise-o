#Memento
'''
Juan Carlo Rangel
25/11/2019
It allows you to capture the status of an object at a specific
time in order to return to this state at any time.
'''
from __future__ import annotations
from abc import ABC, abstractmethod


class MartialArtist:
    pass

class Inicio():
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Estado inicial: {self._state} \n")
        print("Ranma se moja con agua Fria:")
    
    def aguaFria(self) -> None:
        print("Se convierte en mujer.")
        self._state = "Se convierte en hombre"

    def estado(self) -> MartialArtist:
        return Temperatura(self._state)

    def perder(self, martialArtist: MartialArtist) -> None:
        self._state = martialArtist.get_state()
        print(f"Volviendo a la normalidad: {self._state}")
        
#-------------------------------------------------------------

class cambio(MartialArtist):
    pass

class Temperatura(cambio):
    def __init__(self, state: str) -> None:
        self._state = state

    def get_state(self) -> str:
        return self._state

#--------------------------------------------------------------
class Normal():

    def __init__(self, inicio: Inicio) -> None:
        self._Normalidad = []
        self._inicio = inicio

    def backup(self) -> None:
        self._Normalidad.append(self._inicio.estado())

    def undo(self) -> None:
        if not len(self._Normalidad):
            return

        martialArtist = self._Normalidad.pop()
        try:
            self._inicio.perder(martialArtist)
        except Exception:
            self.undo()

if __name__ == "__main__":
    inicio = Inicio("Ranma es un hombre")
    normal = Normal(inicio)
    inicio.aguaFria()
    print("\nRanma se moja con agua Caliente\n")
    normal.backup()
    normal.undo()
    
    
