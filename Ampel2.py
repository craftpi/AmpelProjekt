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

#----------------------Variable Erstellung----------------------#
while True: 
    try:
        z=int(input("\033[0m"+"Wie Lange ist die Schaltzeit ? : "))
        a=int(input("Wie viele Ampel benoetigst du ? : "))
        break
    except:
       print("\033[31m"+"Du hast Vergessen einen Wert Einzugeben")

l=list()

for i in range (0, a):
    exec(f"a{i} = AmpelAnzeige(i+1)")
    l.append(locals()[f"a{i}"])

#---------------------Fenster nebeneinander---------------------#

for i in range(0, a):
    window_width = 200
    window_height = 400
    padding = 50
    x = (window_width + padding) * i
    y = 0
    l[i].geometry(f"{window_width}x{window_height}+{x}+{y}")

#------------------------Ampel Animation------------------------#

for i in range(0,a):
    l[i].setaus()
    l[i].setan([1,0,0])

t.sleep(2)

while True:

    for i in range(0,a):
        green(l[i])
        t.sleep(z)
        red(l[i])



