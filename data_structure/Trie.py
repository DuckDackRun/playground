#Tries sind cool, besonders Grundlage für SuffixBäume
#ShinBäume sind jedoch bessere, effizientere Tries
class TrieNode:
    def __init__(self):
        self.kinder = {}#we coult also use array with objects + everyone store char
        self.EndeGelände =False
        self.value =None

class Trie:
    def __init__(self):
        self.root =self.TrieNode()
    
    def insert(self, str, val):
        cur = self.root

        for c in str:
            if c not in cur.kinder:
                cnode=TrieNode()
                cur.kinder[c]=cnode
            cur=cur.kinder[c]
        cur.value=val
        cur.EndeGelände=True

    def search(self, str)->bool:
        cur = self.root

        for c in str:
            if c not in cur.kinder:
                print(f"Wort nicht enthalten")
                return False
            cur=cur.kinder[c]
        if cur.EndeGelände:
            return cur.val
        print(f"Ende nicht enthalten")
        return False
    
    def delete(self, str)->bool:
        #TODO exception: negativer Fall
        cur=self.root
        stack=[cur]

        for c in str:
            if c not in cur.kinder:
                print(f"Wort nicht enthalten")
                return False
            
            cur=cur.kinder[c]
            stack.append(cur)

        if not cur.EndeGelände:
            print("Problem mit String")
            return False
        #next=None
        while stack:
            cur=stack.pop()
            if len(cur.kinder)>1:
                return True
            eliminate=cur
            #eliminate.val=None ... - Werte löschen für GarbageCollector
            
            cur=stack[::-1] #vorgänger von cur
            cur.kinder.remove(eliminate)
        return True
    
    def startsWith(self, prefix)->bool:
        pass# relativ trivial ...

