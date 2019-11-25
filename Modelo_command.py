#Command
'''
Juan Carlos Rangel 
25/11/2019
Command Pattern Design Example
If we have some objects that perform a similar action in different ways,
then we want it to be processed in the correct way depending on the action
assigned to the object
'''

from abc import ABC, abstractmethod

class JOYSTICK(ABC):
    @abstractmethod
    def action(self):
        pass
#--------------------------------------------------
class Play_Videogames(JOYSTICK):
    def __init__(self, JOYSTICK):
        self.joystick = JOYSTICK

    def action(self):
        self.joystick.Play_Videogames()

#--------------------------------------------------
class PauseGame(JOYSTICK):
    def __init__(self, JOYSTICK):
        self.joystick = JOYSTICK

    def action(self):
        self.joystick.PauseGame()

#--------------------------------------------------
class StartGame(JOYSTICK):
    def __init__(self, JOYSTICK):
        self.joystick = JOYSTICK

    def action(self):
        self.joystick.StartGame()
#--------------------------------------------------
      
class CloseGame(JOYSTICK):
    def __init__(self, JOYSTICK):
        self.joystick = JOYSTICK

    def action(self):
        self.joystick.CloseGame()
#--------------------------------------------------
class ActionMenu:
    def Play_Videogames(self):
        print("Loading")
        
    def PauseGame(self):
        print("Menú")
        
    def StartGame(self):
        print("Go")

    def CloseGame(self):
        print("Exit")
#-----------------------------------------------------
class Action:
    def __init__(self):
        self._actions = []

    def requestActions(self, JOYSTICK):
        self._actions.append(JOYSTICK)
        JOYSTICK.action()

#-------------------------------------------------------
class main():
    menu = ActionMenu()
    joystick_PlayGames = Play_Videogames(menu)
    joystick_PauseG = PauseGame(menu)
    joystick_StarG = StartGame(menu)
    joystick_CloseG = CloseGame(menu)

    act = Action()
    act.requestActions(joystick_PlayGames)
    act.requestActions(joystick_PauseG)
    act.requestActions(joystick_StarG)
    act.requestActions(joystick_CloseG)
