#der Vorteil an Bitset -> const. Operation um Wert im Set zu finden
#Nachteil: nicht vergelcihsbasiert, Rang etc. lässt sich schwer finden
class BitSet:

  def __init__(self, maxW):
     self.maxWert = maxW
     self.Größe = 1+maxW//64
     self.A = [0]*self.Größe
  
  def contains(self, i):
     if i>self.maxWert or i<0:
        return False
     k = i//64
     shift = i%64
     return (self.A[k]>>shift) & 1 == 1

#Rückgabe ist, ob Funktion erfolgt ist
  def add(self,i):
    if i>self.maxWert or i<0:
        
        
        altwert=self.maxWert
        self.maxWert =i
        self.Größe = 1+i//64
        self.A=self.A+[0]*(self.Größe-altwert)
        self.add(i)
        #klappt relativ gut?
        return 
    k=i//64
    shift =i%64
    self.A[k] |= (1<<shift)
    return 
#self-Liste ist selbst größer als fremdes bitset, Rückgabe ob Funktion erfolgt ist
  def union(self,bitset):
    
    if bitset.maxWert>self.maxWert:
        #self vergößern
        altwert=self.maxWert
        self.maxWert =bitset.maxWert
        self.Größe = bitset.Größe
        self.A=self.A+[0]*(self.Größe-altwert)
    
    for i in range(bitset.Größe):
        self.A[i]=self.A[i] | bitset.A[i]

    return
     
     
  def isempty(self):
    return self.A == [0]*self.Größe #klappt das?
# Tests

a1 = BitSet(500)
a2 = BitSet(300)

a2.add(300)
a2.add(7)
a2.add(5)
a2.add(3)
a2.add(1)
try:
    a2.add(301)
except AssertionError:
    print("Add Error")
print (a1.isempty(),a2.isempty())
try:
    a1.union(a2)
    print(1)
except AssertionError:
    print("Union Error")
a1.union(a2)
print(a2.A,a1.A)
print (a1.isempty(),a2.isempty(), a1.contains(301), a1.contains(300),a2.contains(300),a2.contains(7),a2.contains(301))


