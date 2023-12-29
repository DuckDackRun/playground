
import random as r
import collections as c 

class node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.n=None##n für nächster
        self.u=None#bedeutet down

    def set_n(self,n):
        self.n=n
    
    def set_u(self,n):
        self.u=n

    def get_n(self):#nutzlos
        return self.n
    
    def get_u(self):
        return self.u

class Skiplist:
    def __init__(self):
        self.tail=node(float('inf'),"Ich bin der Anfang")
        self.head=node(float('-inf'),"Ich bin das Ende")
        self.head.set_n(self.tail)

        #und ich bin der Creator

    #Vorbedingung: (Schlüssel,Wert)-Paar, optionale Höhe - dabei darf bei Angabe der Höhe nicht das Paar zuvor existieren
    #zudem darf es kein Schlüssel mit 0 existieren !!! dieser kann fälschlicherweise als None interpretiert werden
    #Nachbedingung: skillist enthält das eingefügte Paar 
    #height 0 heißt random höhe, höhe 1 heißt unterste ebene
    def insert(self,key,value,height=0)->int:
        def topdownfull(cur,value)->int:#die funktion ändert alle Werte der unteren Knoten zu value
            cur.value=value
            counter=1
            while cur.u:
                counter+=1
                cur=cur.u
                cur.value=value
            return counter
            
        counter=0
        buff=c.deque()#stack angelegt#das ist dumm, eine [] macht dasselbe
        cur=self.head
        while True:#solange bis ganz unten 
            while cur.n.key<=key:#solange bis cur.n>key ist
                counter+=1
                cur=cur.n
            counter+=1
            if cur.key==key:
                counter+=topdownfull(cur,value)
                return counter #nur einmal, alle 
            
            counter+=1
            if not cur.u:
                break    
            buff.append(cur) #wir müssen diesen schnittknoten speichern, werden ihn später durch stack rekursiv wieder besuchen
            cur=cur.u
        
        #falls nicht durch if-state ==key abgefangen, existiert kein Knoten für Schlüssel -> neu einfügen        
        tmp=cur.n
        new=node(key,value)#new unterste Knoten
        cur.n=new
        cur.n.set_n(tmp)

        #hier noch random hochgehen
        if height:
            height=height-1
            for i in height:
                newnew=node(key,value)
                counter+=1
                if buff:#falls Knoten existiert, der vor value ist
                    knoten=buff.pop()
                    tmp=knoten.n
                    newnew.set_n(tmp)
                    newnew.set_u(new)
                    knoten.set_n(newnew)
                else:
                    neuerAnfang=node(float('-inf'),"Ich bin der Anfang")
                    neuesEnde=node(float('inf'),"Ich bin das Ende")

                    alterhead=self.head
                    altestail=self.tail

                    self.head=neuerAnfang
                    self.head.set_u(alterhead)
                    self.head.set_n(newnew)

                    newnew.set_u(new)
                    newnew.set_n(neuesEnde)

                    self.tail=neuesEnde
                    self.tail.set_u(altestail)
                new=newnew

        else:
            while r.randint(0,1):#würfeln, ob Knoten hochgeht 
                newnew=node(key,value)
                counter+=2#wegen rand und buff
                if buff:#falls Knoten existiert, der vor value ist
                    knoten=buff.pop()
                    tmp=knoten.n
                    newnew.set_n(tmp)
                    newnew.set_u(new)
                    knoten.set_n(newnew)
                    
                else:
                    neuerAnfang=node(float('-inf'),None)
                    neuesEnde=node(float('inf'),None)

                    alterhead=self.head
                    altestail=self.tail

                    self.head=neuerAnfang
                    self.head.set_u(alterhead)
                    self.head.set_n(newnew)

                    newnew.set_u(new)
                    newnew.set_n(neuesEnde)

                    self.tail=neuesEnde
                    self.tail.set_u(altestail)

                new=newnew

        return counter     

    def delete(self,key)->(bool,int):#topdown
        counter=1#für ersten whileschleifenvergleich
        gesehen=False
        cur=self.head
        ebene=0
        while True:#solange bis ganz unten
            #print(cur.key)
            ebene+=1

            if not cur.n.key:
                '''
                print(f"sussusamongus {cur.key}")
                print(key)
                print("Ebene: ",ebene)
                print("Sein nachabr lautet",cur.n.key)
                if cur.u:
                    print("noch suser",cur.u.key)'''

            while cur.n.key<key:#solange bis cur.n>=key ist, cur.n kann key sein
                counter+=1
                '''
                if not cur.n.key:
                    print("suse",cur.key)
                    if cur.u:
                        print("untersues",cur.u.key)'''#ich kann nicht debuggen weil ich doof bin


        
                cur=cur.n
                #print(cur.key)
            counter+=1
            if cur.n.key==key:#hier abgefragt - gelöscht
                #print("Gekillt in Ebene", ebene)#sehr lustig
                counter+=3
                #abfrage, ob wir oberste ebene löschen können
                if cur.u and cur.key==float('-inf') and cur.n.n.key==float('inf'):
                    print("SUperkill:",ebene,"- Key:",key)
                    self.head=cur.u

                    cur.n.n.set_u(None)
                    cur.n.set_n(None)
                    cur.n.set_u(None)
                    cur.set_n(None)
                    #print(self.head.key)
                    cur=cur.u#wir wollen beim nächsten direkt den -inf besuchen
                    continue

                tmp=cur.n.n#muss existieren wegen inf
                #print(cur.n.n.key)
                #für garbagecollector
                cur.n.set_n(None)
                cur.n.set_u(None)
                
                cur.set_n(tmp)
                gesehen=True 
                print("in Ebene noch",key)
            
            counter+=1
            if not cur.u:
                break
            cur=cur.u
            
        
        return (gesehen,counter)
        
    #Vorbedingung: ein valider key zum vergleichen, Nachbedingung: nothing, Rückgabe: Anzahl Vergleiche
    def get(self,key)->int:
        counter=1
        cur=self.head
        while True:#solange bis ganz unten
            #print(cur.key)
            #print(cur.n)
            while cur.n.key<=key:#solange bis cur.n>key ist
                counter+=1
                cur=cur.n

            counter+=1
            if cur.key==key:#dann kann cur.key == key sein
                #print(f"Der Wert lautet {cur.value} vom Schlüssel {cur.key}.")
                return (cur.key,cur.value,counter) 
            
            counter+=2
            if not cur.u:
                break
            
            cur=cur.u
            
        #print(f"Ein Wert zum Schlüssel existiert nicht, der Nachfolger mit dem Schlüssel {cur.n.key} lautet: {cur.n.value}")
        return (cur.n.key,cur.n.value,counter)
        

#hey, dori - falls du Verbesserungsvorschläge hast, nur raus damit       

def traversal(skiplist):#verwandelt skiplist in eine liste von listen ()
    cur=skiplist.head
    ans=[]
    start=cur
    while True:
        lvl=[]
        cur=start

        if cur.u:
            start=cur.u
        
        while True:
            lvl.append(cur.key)
            if not cur.n:
                ans.append(lvl)
                break 
            cur=cur.n
        
        if not cur.u:
            break
        cur=cur.u
    return ans

def verliste(cur):
    ans=[]

    while True:   
        if not cur.u:
            break
        cur=cur.u

    while True:
        ans.append(cur.key)
        if not cur.n:
            break 
        cur=cur.n

    return ans




############ testing b) ####################
'''
#grob testing - sieht erstmal gut aus
u=skiplist()
for i in range(1,50):
    u.insert(i,"Erlöst mich")
list=traversal(u)
print(list)
for i in range(1,49):
    u.delete(i)
    print("")
    print(traversal(u))

    ##sehr cool, beobachte den Killcount
'''


def gen(n):
  li= [(r.random()*10000000//1,r.random()*10000000//1) for _ in range(n)]
  return li

def check(li):
    for i in range(len(li)-1):
        if li[0]>li[1]:
            return True
    return False

#hab mir noch nicht pypy geholt - mein Interpreter oder so ist nicht so leistungsstark
def testinsert_mio():
    for _ in range(1):
        u=Skiplist()
        count_in=0
        count_del=0
        count_get=0
        anzahl=1000 #20000000 ist zu viel für meinen armen rechner
        li=gen(anzahl)

        for pair in li:
            count_in+=u.insert(pair[0],pair[1])

        sample=[]
        num=2000
        for _ in range(num):
            pair=u.get(r.random()*10000000//1)
            sample.append(pair[0])
            count_get+=pair[2]
        print(count_get/num)#vergleiche zu get sind logorithmisch
        
        i=500
        j=1675
        while i and j:
            if sample[j]!=float('inf') and sample[j]!=float('-inf'):#samplewerte sind zufällig, die letzte bedingung ist irgendwie mal aufgekreuzt
                #print(sample[j])
                u.delete(sample[j])
                #TODO löschcounter fehlt,delete
                i-=1
                j-=1
            j-=1


             

    final=verliste(u.head)#die traversal fkt gibt mehr her
    if check(final):
        print("Skipliste hat Fehler")
    else:
        print("Super, alles fein!")
        #print(li)
    '''
    print(traversal(u.head))
    for pair in li:
        u.get(pair[0])
    '''
    return

def find_durchschnitt_höhe(zahl=1000):
    def height(list):
        node=list.head
        h=1#unterste Höhe ist 1 wie beim Übungsblatt
        while True:
            if not node.u:
                break
            node=node.u
            h+=1
        return h

    test=[2,4,8,15,32,64,128,256,11,12,13,14,24,25,26,27]
    schnitt=0
    for i in range(zahl):
        u=Skiplist()
        for i in test:
            u.insert(i,1)
        schnitt+=height(u)
    return schnitt/zahl

#laufzeit    
testinsert_mio()#hat einmal erfolgreich funktioniert
#print(find_durchschnitt_höhe()) #bei 4 elems ist höhe zwischen 3,4,  8elems 4, 16, 5 hmm
#Bester Wert für Wahrscheinlichkeitspara? - am besten ist 1? Je höher, desto wahrscheinlicher
