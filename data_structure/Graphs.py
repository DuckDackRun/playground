from ShinTree import node

class Adjazenzmatrix:
    a=[]
    def __init__(self):
        self.matrix=[]
        self.list=[]
        self.n=0

    def insert(self,node,list):
        for list in self.list:
            list.append(0)

        self.n+=1
        self.list.append(node)
        
        for (i,k) in list:
            if i==node:
                j=self.list.index(k)
                self.list[i][j]=1#in zeile i, erreicht i j
                continue
            if k==node:
                h=self.list.index(i)
                self.list[h][k]=1#in zeile h, erreicht h k

        
