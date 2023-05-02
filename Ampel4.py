from AmpelAnzeige import *

#---------------------Verkehrs Ampel Klasse---------------------#

class Ampel(object):
    def __init__(self,name,i):
        n=str(name)+str(i)
        self.name = AmpelAnzeige(n)
       # self.rootscreenwidth= Tk().winfo_screenwidth()
        #self.rootscreenhight= Tk().winfo_screenheight()
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

    def geoupscalle(self):
        self.tk.winfo_screenwidth
        self.tk.winfo_screenheight

#---------------------Fussgänger Ampel Klasse---------------------#

class AmpelFuss(object):
    def __init__(self,name,i):
        n=str(name)+str(i)
        self.name = AmpelFussAnzeige(n)
        self.window_width = 200
        self.window_height = 400
        self.padding = 50
        self.x = (self.window_width + self.padding) * (i-1)
        self.y = 400
        
    def setgreen(self):
        self.name.setaus()
        self.name.setan([0,1])

    def setred(self):
        self.name.setaus()
        self.name.setan([1,0])
    
    def setgeo(self):
       self.name.geometry(f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")






