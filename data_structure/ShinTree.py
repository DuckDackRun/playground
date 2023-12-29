import collections as c
import time

class node:
    def __init__(self):
        self.key=None
        self.value=None
        self.left=None
        self.right=None
    
    def set_key(self,key):
        self.key=key

    def set_value(self,value):
        self.value=value
    
    def set_left(self,child):
        self.left=child

    def set_right(self,child):
        self.right=child

#Kleine Bemerkung zu ShinTrees, sie sind die schnellsten Trees für Abfragen /Bessere digitale Suchbäume/Tries
class ShinTree:
    def __init__(self):
        self.head=node()

    #
    def insert(self,string,value)->bool:
        def full(cur,n,str,value):
            for i in range(n-1,0,-1):
                #print(reverse_str[i])
                cur.key=str[i]
                cur.left=node()
                cur=cur.left
            cur.key=str[0]
            cur.set_value(value)
            return
        counter=1#Anzahl der Vergleiche
        cur=self.head
        n=len(string)
        reverse_str=string[::-1]
        while n:
            counter+=1
            #
            if not cur.left:
                acc=node()
                cur.set_left(acc)
                cur=acc
                full(cur,n,reverse_str,value)#der cur knoten muss selbst überschrieben werdne, weite n, str und endvalue

                break
            
            counter+=1
            cur_char=reverse_str[n-1]
            if cur.left.key == cur_char:#wert gefunden
                #TODO vernachlässigbar?
                #reverse_str.rstrip(reverse_str[-1])#letzte char pop 
                cur=cur.left
                n-=1
                continue

            counter+=1
            #print(cur_char,cur.left.key)#debugging ist hart
            if cur.left.key < cur_char:#Wer
                cur=cur.left

                while cur:
                    counter+=1
                    if not cur.right:
                        cur.right=node()
                        full(cur.right,n,reverse_str,value)
                        n=0#wie komme ich 
                        #print(cur.key)
                        break
                    
                    counter+=1
                    if cur.right.key==cur_char:
                        cur=cur.right
                        n-=1#dfddasddsadffsad
                        break
                
                    counter+=1
                    if cur.right.key>cur_char:
                        #Dann wollen wir einen neuen Knoten initialisieren, da kein rechter Knoten mit revre_str[n-1] existiert
                        tmp=node()
                        tmp.set_right(cur.right)
                        cur.right=tmp
                        full(tmp,n,reverse_str,value)
                        n=0
                        break

                    cur=cur.right
                #cur.right=node()
                #cur.right.set_key(reverse_str[n-1])
                #n-=1
                #TODO hier fehlt evtl was
                continue

            if cur.left.key > cur_char:
                tmp=node()
                tmp.set_key(cur_char)

                tmp.right=cur.left
                cur.left=tmp

                cur=tmp#wollen bei dem cur weitermachen
                #reverse_str.rstrip(cur_char)#letzte char pop
                n-=1
                continue
            
        #Basisfall, falls, cur Knoten existiert
        cur.set_value(value)

    def traversal(self)->list:
        cur=self.head
        res=[]
        tiefe=0
        if not cur.left:
            return ["Leere Hülle"]
        
        cur=cur.left
        q=c.deque()
        q.append(cur)
        print("Beginn")
        while q:

            rus=[]
            for _ in range(len(q)):
                cur=q.popleft()

                ans=[]
                while True:#ganz nach rechts
                    #print(cur.key)
                    
                    if cur.left:#zuerst left dann right
                        q.append(cur.left)
                        ans.append(cur.key)
                    else:
                        ans.append(cur.key+' $')

                    if not cur.right:
                        rus.append(ans)
                        break
                    cur=cur.right

            res.append(rus)
        
        return res

    def get(self,string):
        
        counter=1#Anzahl der Vergleiche
        cur=self.head
        n=len(string)
        reverse_str=string[::-1]
        while n:
            counter+=1
            #
            if not cur.left:
                print(f"Der Schlüssel {string} existiert nicht im Baum!")
                return False
            
            counter+=1
            cur_char=reverse_str[n-1]


            counter+=1
            #print(cur_char,cur.left.key)#debugging ist hart
            if cur.left.key < cur_char:#Wer
                cur=cur.left

                while cur:
                    counter+=1
                    if not cur.right:
                        print(f"Der Schlüssel {string} existiert nicht im Baum!")
                        return False
                    
                    counter+=1
                    if cur.right.key==cur_char:
                        #TODO fehlt das nicht
                        cur=cur.right

                        n-=1#df
                        break

                
                    counter+=1
                    if cur.right.key>cur_char:
                        #Dann wollen wir einen neuen Knoten initialisieren, da kein rechter Knoten mit revre_str[n-1] existiert
                        print(f"Der Schlüssel {string} existiert nicht im Baum!")
                        return (None,counter)

                    cur=cur.right
                #cur.right=node()
                #cur.right.set_key(reverse_str[n-1])
                #n-=1
                #TODO hier fehlt evtl was
                continue

            if cur.left.key > cur_char:
                print(f"Der Schlüssel {string} existiert nicht im Baum!")
                return (None,counter)
            
            #default ist ==
            #if cur.left.key == cur_char:#wert gefunden 
            cur=cur.left
            n-=1
        
        return (cur.value,counter)
                
        

    #bissle kompliziert
    def delete(self,string):
        pass
        #zuerst den Endknoten finden und rückwärts löschen
        #Knoten nur dann löschen, falls keine Kinder und unmarkiert/valuelos
        #Falls Kinder, abbrechen
    



def testinsert():#hura
    u=ShinTree()
    u.insert("Kim",1)
    u.insert("King",2)
    #u.insert("Kang",3)
    u.insert("Jade",6)
    u.insert("Kent",6)
    u.insert("Queen",6)
    u.insert("Lion",6)
    u.insert("Kile",6)
    u.insert("Kind",3)
    
    print("Start Traversal")
    #time.sleep(3)

        
    print(u.traversal())
    #Ergebnis wie von Herrn Dr. Shin: https://www.youtube.com/watch?v=ltNZQYYMTpE

if __name__=="__main__":
    print("")
    testinsert()






