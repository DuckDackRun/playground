#TODO md file erstellen abstract https://tmc.web.engr.illinois.edu/heap_ianfest.pdf
# - fiboheaps sind theoretisch gut, praktisch zu kompliziert (Hilfsarbeit) und werden von einfacheren heaps outperformt
# TODO mit Implementierung auseinandersetzen

class FibonacciHeap:
    #interne nodeklasse
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.parent = self.child = self.left = self.right = None
            self.degree = 0
            self.mark = False
    
    def __init__(self):
        self.head=self.Node()
        self.min=None
        self.len=0
        self.root_list=self.min_node = None

    # maintain total node count in full fibonacci heap
    total_nodes = 0

    # return min node in O(1) time
    def find_min(self):
        return self.min_node

    def insert(self,key,value):
        pass

    def find_min(self,key,value):
        pass 

    def extract_min(self):
        pass

    def lower_key(self,key,k):
        pass


def testinsert():
    pass


if __name__=="__main__":
    testinsert