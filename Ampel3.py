import time as t
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

z=int(input("Wie Lange ist die Schaltzeit der Verkehrsampel ? : "))
zf=int(input("Wie Lange ist die Schaltzeit der Fussgaengerampel ? : "))
a=int(input("Wie viele Verkehrsampel benoetigst du ? : "))
b=int(input("Wie viele Fussgaengersampel benoetigst du ? : "))

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
    #(window_height + padding) * i
    lv[i].geometry(f"{window_width}x{window_height}+{x}+{y}")

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
    lv[i].setaus()
    lv[i].setan([1,0,0])

for i in range(0,a):
    lf[i].setaus()
    lf[i].setan([1,0,0])

t.sleep(2)

while True:

    for i in range(0,a):
        green(lv[i])
        greenf(lf[i])
        t.sleep(z)
        red(lv[i])
        redf(lf[i])



