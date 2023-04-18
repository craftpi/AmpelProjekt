import time
from AmpelAnzeige import *

z=int(input("Wie Lange ist die Schaltzeit ? : "))
a=int(input("Wie viele Ampel benoetigst du ? : "))

l=list()

for i in range (0, a):
    exec(f"a{i} = AmpelAnzeige(i+1)")
    l.append(locals()[f"a{i}"])
    #l.append()


for i in range(0, a):
    am=l[i]
    am.setan([0,1,0])
a1=AmpelAnzeige("ret")
a1.setan([1,0,0])




mainloop()