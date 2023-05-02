import time as t
import asyncio
from AmpelAnzeige import *
from Ampel4 import *

#--------------------------Funktionen--------------------------#
def green_red_v(a1):
    a1.setgreen()
    t.sleep(1)
    a1.setyellow()
    t.sleep(1)
    a1.setred()

def red_green_v(a1):
    a1.setred()
    t.sleep(1)
    a1.setredyellow()
    t.sleep(1)
    a1.setgreen()

def green_red_f(a1):
    a1.setgreen()
    t.sleep(1)
    a1.setred()

def red_green_f(a1):
    a1.setred()
    t.sleep(1)
    a1.setgreen()

#----------------------Variable Erstellung----------------------#
while True:
    try:
        z=int(input("\033[0m"+"Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
        zf=int(input("Wie gross soll die verzoegerung zwischen Fuss und Verkehrsampel sein  ? : "))
        a=int(input("Wie viele Verkehrsampel benoetigst du ? : "))
        b=int(input("Wie viele Fussgaengerampeln benoetigst du ? : "))
        break
    except :
        print("\033[31m"+"Du hast Vergessen einen Wert Einzugeben")

tu =True

lv=list()
lf=list()

#------------------------Korektur abfrage--------------------------#

while tu == True:
    print("\033[31m"+"Warnung du kannst die Daten spaeter nicht mehr aendern")
    print("Schaltzeit der Ampel: " + str(z),", ","Verzoegerung: " + str(zf),", ", "Anzahl der Verkehrsampel: " + str(a),", ", "Anzahl Fussgaengerampel: " + str(b) )
    fr=input("\033[36m"+"Moechtest du die Eigaben Korigieren [J;N] ? ")
    if fr == "J" :
        try:
            z=int(input("\033[0m"+"Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
            zf=int(input("Wie gross soll die verzoegerung zwischen Fuss und Verkehrsampel sein  ? : "))
            a=int(input("Wie viele Verkehrsampel benoetigst du ? : "))
            b=int(input("Wie viele Fussgaengerampeln benoetigst du ? : "))
            break
        except :
            print("\033[31m"+"Du hast Vergessen einen Wert Einzugeben")
    else:
        tu = False
        print("\033[33m"+"execute ... ")
    

#---------------Variabeln werden den Listen zugeornet---------------#

for i in range (0, b):
    exec(f"a{i} = AmpelFuss('AmpelFuss',i+1)")
    lf.append(locals()[f"a{i}"])

for i in range (0, a):
    exec(f"a{i} = Ampel('Ampel',i+1)")
    lv.append(locals()[f"a{i}"])

#------------------------Fenster ausrichten-------------------------#

for i in range (0, a):
    lv[i].setgeo()

for i in range (0, b):
    lf[i].setgeo()
 
#--------------------------Ampel Animation--------------------------#

#+++ Asyncio wird verwendet um Fuﬂg‰nger und Vehrkehrampel +++# 
#+++ gleichzeitigt zu schalten.                            +++#


for i in range(0,a):
    lv[i].setred()

for i in range(0,a):
    lf[i].setred()
    
t.sleep(z)

async def main():
    task1 = asyncio.create_task(vampel())
    task2 = asyncio.create_task(fampel())
    await asyncio.gather(task1, task2)

async def vampel():
    for i in range(0,a):
        await asyncio.sleep(zf)
        red_green_v(lv[i])
        await asyncio.sleep(z)
        green_red_v(lv[i])
        await asyncio.sleep(2)
        await asyncio.sleep(3)
async def fampel():
    for i in range(0,b):
        red_green_f(lf[i])
        await asyncio.sleep(z+zf)
        green_red_f(lf[i])
        await asyncio.sleep(5)

while True:
    asyncio.run(main())
    