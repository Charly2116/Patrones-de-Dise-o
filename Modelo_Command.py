#Command
'''
25/11/2019
Juan Carlos Rangel 
The Command pattern is recognizable by behavioral methods in an
abstract/interface type (sender) which invokes a method
in an implementation of a different 
'''
from __future__ import annotations
from abc import ABC, abstractmethod

class ControlVideo(ABC):

    @abstractmethod
    def loading(self) -> None:
        pass


class AceptarControlVideo(ControlVideo):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def loading(self) -> None:
        print(f"Preparandose para continuar la partida"
              f"({self._payload})")


class GuardarControlVideo(ControlVideo):
    
    def __init__(self, buttonn: Buttonn, a: str, s: str) -> None:

        self._buttonn = buttonn
        self._a = a
        self._s = s

    def loading(self) -> None:

        print("presiona el otro boton para ejecutar los cambios", end="")
        self._buttonn.do_something(self._a)
        self._buttonn.do_something_else(self._s)


class Buttonn:

    def do_something(self, a: str) -> None:
        print(f"\nPresiona el boton para:({a}.)", end="")

    def do_something_else(self, s: str) -> None:
        print(f"\npresiona el otro boton para ({s}.)", end="")


class Accion:

    _on_start = None
    _on_finish = None

    def set_on_start(self, controlVideo: ControlVideo):
        self._on_start = controlVideo

    def set_on_finish(self, controlVideo: ControlVideo):
        self._on_finish = controlVideo

    def do_something_important(self) -> None:

        print("Estas seguro que deseas continuar")
        if isinstance(self._on_start, ControlVideo):
            self._on_start.loading()

        print("Punto de guardado: dese confirmar")

        print("Presiona aceptar para confirmar tu partida")
        if isinstance(self._on_finish, ControlVideo):
            self._on_finish.loading()

if __name__ == "__main__":


    accion = Accion()
    accion.set_on_start(AceptarControlVideo("Bienvenido de nuevo"))
    buttonn = Buttonn()
    accion.set_on_finish(GuardarControlVideo(
        buttonn, "Aceptar", "Guardar"))

    accion.do_something_important()
