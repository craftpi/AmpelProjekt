import time as t
import asyncio
from AmpelAnzeige import *

#--------------------------Funktionen--------------------------#

def green(a1):
    a1.setan([1,1,0])
    t.sleep(1)
    a1.setaus()
    a1.setan([0,0,1])

def red(a1):
    a1.setaus()
    a1.setan([0,1,0])
    t.sleep(1)
    a1.setaus()
    a1.setan([1,0,0])

def greenf(a1):
    a1.setaus()
    a1.setan([0,1])

def redf(a1):
    a1.setaus()
    a1.setan([1,0])

#----------------------Variable Erstellung----------------------#

tu = True

while True:                                                                                                                                         # fängt Fehler ab fals eingabe nicht vorgenommen wird
    try:
        z=int(input("Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
        zf=int(input("Wie Lange ist die Schaltzeit der Fussgaengerampel ? : "))
        a=int(input("Wie viele Verkehrsampel benoetigst du ? : "))
        b=int(input("Wie viele Fussgaengersampel benoetigst du ? : ")) 
        break
    except :
        print("\033[31m"+"Du hast Vergessen einen Wert Einzugeben")

while tu == True:                                                                                                                                  # fängt Fehler ab fals eingabe nicht vorgenommen wird und überprüft ob z = zf
    if z!=zf:
        print("\033[31m"+"Warnung Die Schaltzeiten von Fussgaengerampeln und Verkehrsampeln sind nicht gleich!")
    print("\033[31m"+"du kannst die Daten spaeter nicht mehr aendern !")
    print("Schaltzeit der Verkehrsampel: " + str(z),", ","Schaltzeit der Fussgaengerampel: " + str(zf),", ", "Anzahl der Verkehrsampel: " + str(a),", ", "Anzahl Fussgaengerampel: " + str(b) )
    fr=input("\033[36m"+"Moechtest du die Eigaben Korigieren [J;N] ? ")
    if fr == "J" :
        z=int(input("Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
        zf=int(input("Wie Lange ist die Schaltzeit der Fussgaengerampel ? : "))
        a=int(input("Wie viele Verkehrsampel benoetigst du ? : "))
        b=int(input("Wie viele Fussgaengersampel benoetigst du ? : "))
    else:
        tu = False
        print("\033[33m"+"execute ... ")

lv=list()
lf=list()

for i in range (0, b):
    fs="fs"+str(i+1)
    exec(f"a{i} = AmpelFussAnzeige(fs)")
    lf.append(locals()[f"a{i}"])

for i in range (0, a):
    exec(f"a{i} = AmpelAnzeige(i+1)")
    lv.append(locals()[f"a{i}"])

#---------------------Fenster nebeneinander---------------------#

for i in range(0, a):
    window_width = 200
    window_height = 400
    padding = 50
    x = (window_width + padding) * i
    y = 0
    lv[i].geometry(f"{window_width}x{window_height}+{x}+{y}")

for i in range(0, b):
    window_width = 200
    window_height = 400
    padding = 50
    x = (window_width + padding) * i
    y = 400
    lf[i].geometry(f"{window_width}x{window_height}+{x}+{y}")

#------------------------Ampel Animation------------------------#
#++++ Asyncio wird verwendet um Fußgänger und Vehrkehrampel ++++# 
#++++ gleichzeitigt zu schalten.                            ++++#


for i in range(0,a):
    lv[i].setaus()
    lv[i].setan([1,0,0])

for i in range(0,a):
    lf[i].setaus()
    lf[i].setan([1,0,0])

t.sleep(2)

async def main():
    task1 = asyncio.create_task(vampel())
    task2 = asyncio.create_task(fampel())
    await asyncio.gather(task1, task2)

async def vampel():
    for i in range(0,a):
        await asyncio.sleep(2)
        green(lv[i])
        await asyncio.sleep(z)
        red(lv[i])
        await asyncio.sleep(1)

async def fampel():
    for i in range(0,b):
        greenf(lf[i])
        await asyncio.sleep(zf+2)
        redf(lf[i])
        await asyncio.sleep(3)

while True:
    asyncio.run(main())
    

