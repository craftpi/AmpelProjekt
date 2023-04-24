import time as t
import asyncio
from AmpelAnzeige import *
from Ampel4 import *

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
zf=int(input("Wie gross soll die verzoegerung zwischen Fuss und Verkehrsampel sein  ? : "))
a=int(input("Wie viele Verkehrsampel benoetigst du ? : "))
b=int(input("Wie viele Fussgaengersampel benoetigst du ? : "))

tu =True

while tu == True:
    print("\033[31m"+"Warnung du kannst die Daten spaeter nicht mehr aendern")
    print("Schaltzeit der Ampel: " + str(z),", ","Verzoegerung: " + str(zf),", ", "Anzahl der Verkehrsampel: " + str(a),", ", "Anzahl Fussgaengerampel: " + str(b) )
    fr=input("\033[36m"+"Moechtest du die Eigaben Korigieren [J;N] ? ")
    if fr == "J" :
        z=int(input("Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
        zf=int(input("Wie gross soll die verzoegerung zwischen Fuss und Verkehrsampel sein  ? : "))
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

async def main():
    task1 = asyncio.create_task(vampel())
    task2 = asyncio.create_task(fampel())
    await asyncio.gather(task1, task2)

async def vampel():
    for i in range(0,a):
        await asyncio.sleep(zf)
        red_green(lv[i])
        await asyncio.sleep(z)
        green_red(lv[i])
        await asyncio.sleep(2)

async def fampel():
    for i in range(0,b):
        await asyncio.sleep(zf)
        greenf(lf[i])
        await asyncio.sleep(z)
        redf(lf[i])
        await asyncio.sleep(2)


while True:
    asyncio.run(main())
    