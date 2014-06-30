import pygame, math, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)
X_TILES = 20
Y_TILES = 15

#Master "mediator" class to handle all event interactions between the Controller, View, and Model.
class EventManager(object):
    
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listenerDictionary = WeakKeyDictionary()
        self.eventQueue = []
        
    def registerListener(self, listener):
        self.listeners[listener] = 1
        
    def unregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def handleEvent(self, event):

#Model class to check for controller events and update the state of the game
class Model(object):
    
    def __init__(self, eventManager):
        self.eventManager = eventManager
        self.eventManager.registerListener(self)

    class Map(object):
        
        self.mapArray = []
        
        def buildMap(self, xSize, ySize):
            for x in range(0, xSize):
                row = []
                for y in range(0, ySize):
                    row.append(0)
                mapArray.append(row)
    
#Controller class to handle input events from user
class Controller(object):
    
    def __init__(self, eventManager):
        self.eventManager = eventManager
        self.eventManager.registerListener(self)

    def getInput(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                thisEvent = None
                if event.type = KEYDOWN:
                    if event.key = K_RIGHT:
                        thisEvent = playerMoveRequest(0)
                    elif event.key = K_UP:
                        thisEvent = playerMoveRequest(1)
                    elif event.key = K_LEFT:
                        thisEvent = playerMoveRequest(2)
                    elif event.key = K_DOWN:
                        thisEvent = playerMoveRequest(3)
                    elif event.key = K_ESCAPE:
                        thisEvent = pauseMenuRequest()
                if thisEvent:
                    self.eventManager.handleEvent(thisEvent)                  

#View class to update client view in accordance with model
class View(object):
    def __init__(self, eventManager):
        self.eventManager = eventManager
        self.eventManager.registerListener(self)
        
    

def main():
    eventManager = EventManager()
    gameController = Controller(eventManager)
    gameView = View(eventManager)
    gameModel = Model(eventManager)
 
if __name__ == "__main__": # Python calls for __main__ in the __name__...
    main() # ...so we tell it to call main() when that happens
