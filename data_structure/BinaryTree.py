import collections as c
from itertools import permutations

#Dieses Programm dient zum Ausrechnen des Entscheidungsbaum vom Selectionsort
class node:
    def __init__(self):
        self.value=None
        self.left=None
        self.right=None

    def set_v(self,value):
        self.value=value

    def set_left(self,value):
        self.left=value

    def set_right(self,value):
        self.right=value

#eine klassiche und einfache Datenstruktur sind binäre Bäume
class BinaryTree:
    def __init__(self):
        self.root=node()

    #list with distinct values
    def insert(self,list):

        cur=self.root
        ans=[]
        index_list=[i for i in range(len(list))] #alle existierenden Elems
        n=len(list)
        cur_mindex=0
        while n:
            cur_mindex=index_list[0]
            for i in range(1,n): #benötige n-1 Vergleiche für min
                if list[cur_mindex]>list[index_list[i]]:
                    if not cur.right:    
                        cur.right=node()

                    cur=cur.right
                    cur.set_v(f"{cur_mindex} hat gewonnen")
                    cur_mindex=index_list[i]
                    
                else:
                    if not cur.left:
                        cur.left=node()
                    
                    cur=cur.left
                    cur.set_v(f"{cur_mindex} hat gewonnen")
                    
            ans.append(list[cur_mindex])
            index_list.remove(cur_mindex) #index entfernt
            n-=1

    def num_leafs(self):
        ans=0
        q=c.deque()
        q.append(self.root)
        while q:
            for _ in range(len(q)):
                node=q.popleft()

                if node.left:
                    q.append(node.left)
                else:
                    ans+=1
                
                if node.right:
                    q.append(node.right)
                else:
                    ans+=1
        return ans

def faku(n):
    if n<=1:
        return 1
    return n*faku(n-1)

def testinsert():
    u=BinaryTree()
    anzahl=4

    for i in permutations([i for i in range(1,anzahl+1)]):
        u.insert(i)
    print("Eine Vermutung lautet: ",u.num_leafs())#-faku(anzahl))

if __name__=="__main__":
    print("")
    testinsert()
    




