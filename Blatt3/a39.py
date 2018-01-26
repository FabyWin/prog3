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
    
    def __hash__(self):
        return hash((self.zeitpunkt,self.temp))

class Messreihe():#a40
    liste = []
    pos = 0
    def __init__(self, value=None):
        self.liste = []
        if value is not None:
            for ele in value:
                self.liste.append(Messwerte(ele))
            
    def __len__(self):
        return len(self.liste)
    
    def add(self,value):
        assert(isinstance(value, Messwerte))
        if not isinstance(value,Messwerte):
            for ele in value:
                if isinstance(ele, Messwerte):
                    self.liste.append(ele)
        else:
            self.liste.append(value)
                    
    def __add__(self,value):
        for ele in value.liste:
            if not self.liste.__contains__(ele):
                self.add(ele)               
        return self.liste
    
    def __iter__(self):
        self.pos = -1
        return self
    
    def __next__(self):
        self.pos += 1
        if self.pos >= self.liste.__len__():
            raise StopIteration
        return self.liste[self.pos]
    
    def __getitem__(self,value):
        if isinstance(value, slice):
            return(self.liste[value.start:value.stop:value.step])
        elif isinstance(value,int) and value>0 and value <= self.liste.__len__():
            return self.liste[value-1]
        elif isinstance(value,str):
            tmp = Messreihe()
            for ele in self.liste:
                if value in ele.zeitpunkt:
                    tmp.add(ele)
            return tmp
    def enum(self):
        count = 0
        for ele in self.liste:
            yield count,ele
            count += 1
    
class MessreiheEigenIter(Messreihe):
    def __init__(self,mwl):
        self._mwl = mwl
        self.pos = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.pos +=1
        if self.pos >= len(self._mwl):
            raise StopIteration
        return self._mwl[self.pos]

class MessreiheGenIter(Messreihe):
    def __init__(self,mwl):
        self._mwl = mwl
        
    def erzeugeIterator(self):
        for ele in self._mwl:
            yield ele
            
    def __iter__(self):
        return self.erzeugeIterator()
            
line = [line.strip() for line in open("messwerte.csv")][0:8]
mw = Messwerte(line[0])
mw2 = Messwerte(line[1])

mr = Messreihe(open("messwerte.csv"))
mr2 = Messreihe([line[0]])

mrei = MessreiheEigenIter(mr)
mr4 = Messreihe()
mr3 = Messreihe([line[1],line[7]])
mr2.add(mw2)
mr4.liste = mr2 + mrei
print(mr4.liste)
blub = Messreihe([line[1],line[2],line[3],line[4],line[5],line[6]])
print(blub.liste)
print(blub[1:2])

#Anzahl der Messwerte
print(len([ele for ele in mr.liste]))

#hoechste Temperaturwert/niedirgster Wert
print(max([mw.temp for mw in [ele for ele in mr.liste]]),min([mw.temp for mw in [ele for ele in mr.liste]]))

#Zeitpunkte Temp ueber 33
print([mw for mw in [ele for ele in mr.liste] if mw.temp > 33.0])

#Wie oft ueber26 grad in 2017
print(len([mw for mw in [ele for ele in mr.liste] if mw.temp > 26.0]))

#zum letzten mal temp auf 17
#print(sorted([mw for mw in [ele for ele in mr.liste] if int(mw.temp) == 17],reverse=True))
print(max([mw.zeitpunkt for mw in [ele for ele in mr.liste] if int(mw.temp) == 17]))

#Temperatur Mittelwert der letzten 3 Monate
newTime = max([mw.zeitpunkt for mw in [ele for ele in mr.liste]])

for nr, messwert in blub.enum():
    print(nr,"->",messwert)