from AmpelAnzeige import *
#import AmpelAnzeige as am

z=int(input("Wie Lange ist die Schaltzeit"))


A1=AmpelAnzeige("Ampel_1")
A1.setan([0,0,1])
A2=AmpelAnzeige("Ampel_2")
A2.setan([1,0,0])

mainloop()