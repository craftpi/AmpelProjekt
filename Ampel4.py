import time as t
from AmpelAnzeige import *
from Ampel4Klasse import *

#--------------------------Funktionen--------------------------#
def green_red(a1):
    a1.setgreen()
    t.sleep(1)
    a1.setyellow()
    t.sleep(1)
    a1.setred()

def red_green(a1):
    a1.setred()
    t.sleep(1)
    a1.setredyellow()
    t.sleep(1)
    a1.setgreen()

def greenf(a1):
    a1.setaus()
    a1.setan([0,1])

def redf(a1):
    a1.setaus()
    a1.setan([1,0])

#----------------------Variable Erstellung----------------------#

z=int(input("Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
zf=int(input("Wie Lange ist die Schaltzeit der Fussgaengerampel ? : "))
a=int(input("Wie viele Verkehrsampel benoetigst du ? : "))
b=int(input("Wie viele Fussgaengersampel benoetigst du ? : "))

tu =True
while tu == True:
    if z!=zf:
        print("\033[31m"+"Warnung Die Schaltzeiten von Fussgaengerampeln und Verkehrsampeln sind nicht gleich!")
        fr=input("\033[36m"+"Moechtest du die Eigaben Korigieren [J;N] ? ")
        if fr == "J" :
            z=int(input("\033[32m"+"Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
            zf=int(input("Wie Lange ist die Schaltzeit der Fussgaengerampel ? : "))
        else:
            tu = False
            print("\033[33m"+"execute ... ")
    else:
        tu = False

lv=list()
lf=list()

for i in range (0, b):
    fs="fs"+str(i+1)
    exec(f"a{i} = AmpelFussAnzeige(fs)")
    lf.append(locals()[f"a{i}"])

for i in range (0, a):
    exec(f"a{i} = Ampel('Ampel',i+1)")
    lv.append(locals()[f"a{i}"])

#----------------------Fenster ausrichten----------------------#
for i in range (0, a):
    lv[i].setgeo()
 
for i in range(0, b):
    window_width = 200
    window_height = 400
    padding = 50
    x = (window_width + padding) * i
    y = 400
    #(window_height + padding) * i
    lf[i].geometry(f"{window_width}x{window_height}+{x}+{y}")

#------------------------Ampel Animation------------------------#



for i in range(0,a):
    lv[i].setred()

for i in range(0,a):
    lf[i].setaus()
    lf[i].setan([1,0,0])
    
t.sleep(z)

while True:

    for i in range(0,a):
        greenf(lf[i])
        red_green(lv[i])
        t.sleep(z)
        redf(lf[i])
        green_red(lv[i])
        t.sleep(2)

        