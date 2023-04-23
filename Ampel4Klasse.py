from AmpelAnzeige import *

class Ampel(object):
    def __init__(self,name,i):
        n=str(name)+str(i)
        self.name = AmpelAnzeige(n)
        self.window_width = 200
        self.window_height = 400
        self.padding = 50
        self.x = (self.window_width + self.padding) * (i-1)
        self.y = 0
        
    def setgreen(self):
        self.name.setaus()
        self.name.setan([0,0,1])

    def setred(self):
        self.name.setaus()
        self.name.setan([1,0,0])

    def setyellow(self):
        self.name.setaus()
        self.name.setan([0,1,0])
        
    def setredyellow(self):
        self.name.setaus()
        self.name.setan([1,1,0])
    
    def setgeo(self):
       self.name.geometry(f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")
    pass




