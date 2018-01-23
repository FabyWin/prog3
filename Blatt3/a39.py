'''
Created on 16.01.2018
@author: fwint001
'''
from __builtin__ import str

class Messwerte(): #a39
    zeitpunkt = None
    temp = None
    
    def __init__(self, *value):
        if len(value) == 1:
            liste = value[0].split(",")
            self.zeitpunkt = liste[0][1:-1]
            self.temp = float(liste[1])
        else:
            self.zeitpunkt = value[0][1:-1]
            self.temp = float(value[1])
            
    def __repr__(self):
        return "Messwerte(\"'{0}'\", {1})".format(self.zeitpunkt, self.temp)
    
    def __eq__(self, other):
        return self.zeitpunkt == other.zeitpunkt and self.temp == other.temp
    
    def __lt__(self, other):
        return self.zeitpunkt < other.zeitpunkt
    
    def __gt__(self, other):
        return self.zeitpunkt > other.zeitpunkt

class Messreihe():#a40
    liste = []
    def __init__(self, value=None):
        self.liste = []
        if value is not None:
            for ele in value:
                self.liste.append(Messwerte(ele))
            
    def __len__(self):
        return len(self.liste)
    
    def add(self,value):
            for ele in value:
                if isinstance(ele, Messwerte):
                    self.liste.append(ele)
            
line = [line.strip() for line in open("messwerte.csv")][0:3]
mw = Messwerte(line[0])
mw2 = Messwerte(line[1])

mr = Messreihe(open("messwerte.csv"))
print(line[0] + "\n")
mr2 = Messreihe([line[0]])

print(mr2.liste)

mr3 = Messreihe([line[1],line[2]])
mr4 = Messreihe()
#mr4 = mr2 + mr3

#print(len(mr))

mr.add([Messwerte(line[0]),Messwerte(line[1])])

print(mr.liste[-2:])

print(mw.zeitpunkt)
liste = []
liste.append(mw)
liste.append(mw2)
print(liste)
print(sorted(liste,reverse=True))