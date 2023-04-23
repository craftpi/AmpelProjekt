# AmpelAnzeige.py
# GUI fuer Verkehrs- und Fussgaengerampeln
# Berufliche Oberschule Erding 2017
# J. Maetzler

import sys


if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *
else:
    # for Python2
    from Tkinter import *

class AmpelAnzeige:
    def __init__(self, name):
        self.name=name
        self.status=[0,0,0]

        # Erzeugung des Fensters
        self.fenster = Tk()
        self.fenster.title(self.name)
        self.fenster.geometry("200x400")
        self.LabelAmpel=Label(self.fenster, text=self.name)
        self.LabelAmpel.pack()

        # Zeichenfläche
        self.canvas = Canvas(master=self.fenster)
        self.canvas.place(x=0, y=20, width=200, height=400)

        # Ampel mit RYG-Lampen und Stange
        self.canvas.create_rectangle(40, 20, 160, 320, fill="gray")
        self.id_rot = self.canvas.create_oval(55, 30, 145, 120, fill="darkgray")
        self.id_gelb = self.canvas.create_oval(55, 125, 145, 215, fill="darkgray")
        self.id_gruen = self.canvas.create_oval(55, 220, 145, 310, fill="darkgray")
        self.canvas.create_rectangle(75, 320, 125, 400, fill="black")

        self.fenster.update()

    def setan(self,liste_ryg=[1,1,1]):
        if liste_ryg[0]==1:
            self.canvas.itemconfigure(self.id_rot, fill="red")
            self.status[0]=1
        if liste_ryg[1]==1:
            self.canvas.itemconfigure(self.id_gelb, fill="yellow")
            self.status[1]=1
        if liste_ryg[2]==1:
            self.canvas.itemconfigure(self.id_gruen, fill="green")
            self.status[2]=1
        self.fenster.update()

    def setaus(self,liste_ryg=[1,1,1]):
        if liste_ryg[0]==1:
            self.canvas.itemconfigure(self.id_rot, fill="darkgray")
            self.status[0]=0
        if liste_ryg[1]==1:
            self.canvas.itemconfigure(self.id_gelb, fill="darkgray")
            self.status[1]=0
        if liste_ryg[2]==1:
            self.canvas.itemconfigure(self.id_gruen, fill="darkgray")
            self.status[2]=0
        self.fenster.update()

    def getstatus(self):
        return self.status
        

    def geometry(self, geostrig):
        self.fenster.geometry(geostrig)
              
class AmpelFussAnzeige:
    def __init__(self, name):
        self.name=name
        self.status=[0,0]

        # Erzeugung des Fensters
        self.fenster = Tk()
        self.fenster.title(self.name)
        self.fenster.geometry("200x400")
        self.LabelAmpel=Label(self.fenster, text=self.name)
        self.LabelAmpel.pack()
        # Zeichenfläche
        self.canvas = Canvas(master=self.fenster)
        self.canvas.place(x=0, y=20, width=200, height=400)

        # Ampelkasten
        self.canvas.create_rectangle(40, 115, 160, 320, fill="gray")
        # Rot-Licht
        self.id_rot = self.canvas.create_oval(55, 125, 145, 215, fill="darkgray")
        # Grün-Licht
        self.id_gruen = self.canvas.create_oval(55, 220, 145, 310, fill="darkgray")
        # Stange
        self.canvas.create_rectangle(75, 320, 125, 400, fill="black")

        self.fenster.update()

    def setan(self,liste_ryg=[1,1]):
        if liste_ryg[0]==1:
            self.canvas.itemconfigure(self.id_rot, fill="red")
            self.status[0]=1
        if liste_ryg[1]==1:
            self.canvas.itemconfigure(self.id_gruen, fill="green")
            self.status[1]=1
        self.fenster.update()

    def setaus(self,liste_ryg=[1,1]):
        if liste_ryg[0]==1:
            self.canvas.itemconfigure(self.id_rot, fill="darkgray")
            self.status[0]=0
        if liste_ryg[1]==1:
            self.canvas.itemconfigure(self.id_gruen, fill="darkgray")
            self.status[1]=0
        self.fenster.update()
    def getstatus(self):
        return self.status
    def geometry(self, geostrig):
        self.fenster.geometry(geostrig)
