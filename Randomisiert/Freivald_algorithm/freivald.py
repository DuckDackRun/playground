import random as r
import math

import plot

def matr(A, m=-1, n=-1):
    if m == -1:
        m = n = int(len(A)**(1/2))
    B = []
    s = 0
    for i in range(n, len(A), n):
        B.append(A[s:i])
        s = i
    B.append(A[s:])
    return B

def inv_matr(A):
    ans=[]
    for i in A:
        ans+=i
    return ans

def sqrt(x):
    return x**(1/2)

def mmul(A, B):
    C = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):#was sollte damals in range(len(A[0]))
                C[i][j] += A[i][k] * B[k][j]
    return C

#@timerget
def freivald(A, B, C):
    # Zeilen/Spaltenanzahl wird bestimmt
    n = len(A)
    # Pr of failure < 1/n
    for _ in range(math.floor(math.log(n, 2))):
        # random matrix
        R = matr([r.randint(1, 2) for _ in range(n)], n, 1)
        b = mmul(C, R) == mmul(A, mmul(B, R))
        if not b:
            return b
    return b


def main2():
    acc = []
    n = 50
    for i in range(2, n):
        A = matr([r.randint(0, 10) for _ in range(int(n**2))])
        B = matr([r.randint(0, 10) for _ in range(int(n**2))])
        C = mmul(A, B)
        acc.append(freivald(A, B, C)[1])
    return acc

def main3():
    acc = []
    n = 50
    for i in range(2, n):
        A = matr([r.randint(0, 1000) for _ in range(int(n**2))])
        B = matr([r.randint(0, 1000) for _ in range(int(n**2))])
        C = mmul(A, B)
        acc.append(freivald(A, B, C)[1])
    return acc

#@plot(funcs=[main2, main3])
def main():
    acc = []
    n = 50
    for i in range(2, n):
        A = matr([r.randint(0, 100) for _ in range(int(n**2))])
        B = matr([r.randint(0, 100) for _ in range(int(n**2))])
        C = mmul(A, B)
        acc.append(freivald(A, B, C)[1])
    return acc



def testing():
    def swap(A,B):
        A[B[1]],A[B[0]]=A[B[0]],A[B[1]]
        return
    #uns interessiert, wie viele Matrizen fälschlicherweise vom Algorithmus als richtig verifiziert werden
    #Wie groß wächst der Fehler des Algorithmus verglichen zur Minimierung/Ähnlichkeits einer Lsgmatrix - wir schauen uns vereinfachthaltshalber nur Fehler auf die C-Matrix an
    #TODO wirken eines Fehlers evtl durch ein !swap von unterschied. Einträgen 0,1 in derselben zeile statt einzelne random flipps 

    zahl_matrizen=10 #für eine bestimmte Länge schauen, anzahl an verschiedenen tests
    MaxMatrix=60
    zahlenbereich=1 #wir können auch beliebige Zahlen nehmen
    #liste von listen, i-Liste enthält selbst Listen, welche Wahrscheinlichkeiten
     
    result=[]
    result_großeFehlerquote=[]
    result_zeilen=[]
    for matrix_len in range(2,MaxMatrix+1):

        #Form von [([matrix_A],[matrix_B]),..]      #wir könnten auch alle permutationen durchgehen
        testmatrizen=[([r.randint(0, zahlenbereich) for _ in range(matrix_len**2)],[r.randint(0, zahlenbereich) for _ in range(matrix_len**2)]) for _ in range(zahl_matrizen)]

        #unabhängig von der Größe
        # von der Form [[(durchschnitt Fehler, lmin, lmax)]]
        fehlerzahl_table_rel_bottomup=[[0,0,2,-1,f"Mit etwa einer Fehleranzahl von {round((i*matrix_len+1)/((matrix_len**2)+1),4)}%"] for i in range((matrix_len+1)//2+1)]
        fehlerzahl_table_rel_topdown=[[0,0,2,-1,f"Mit etwa einer Fehleranzahl von {1-round((i*matrix_len+1)/((matrix_len**2)+1),4)}%"] for i in range((matrix_len+1)//2+1)]#Gegenwahr
        fehlerzahl_table_zeilen=[[0,0,2,-1,f"Mit etwa einer Fehleranzahl von {2*round((i*matrix_len+1)/((matrix_len**2)+1),4)}%"] for i in range((matrix_len+1)//2+1)]
        lmin=2#lokalmin,lokalmax könnten von Interesse sein
        lmax=-1

        for testmatrix in testmatrizen:
            c_lsg=inv_matr(mmul(matr(testmatrix[0]),matr(testmatrix[1])))
        

            res_var=0#hier wird fehleranzahl gesammelt


            # median finden, ein quickselect algorithmus wäre interessant dafür
            # probieren verschiedene Fehlervariationen aus
            #print(testmatrizen)

            #verschiedene fehlerzahlenkombis ausprobieren - von einen bis zur Häflte falsch
            #untersuchen relativen Fehler
            # [[(wahrkeit,lmin,lmax),()],] 
            laufindex=-1
            for fehlerzahl in range(1,(matrix_len**2+2)//2,matrix_len): #gehen in 10% schritten hoch   
                #TODO nur bis matrix_len//2, größer als das kann man über geflipptes C machen und random Bits korrigieren
                laufindex+=1
                versagen=0.0
                versagen_gespiegelt=0.0
                versagen_zeilen=0.0
                #sollten wir die range abhängig der größe der matrix machen? abhängig der einträge zu groß
                sample=5
                mod_lsg=c_lsg # lsg wird in einer liste umtransformiert, unser C
                mod_lsg_2=c_lsg
                mod_lsg_geflippt=[i^1 for i in c_lsg]

                for _ in range(sample):
                    #print(testmatrix)
                    
                    n=fehlerzahl

                    ####################################################################################################################

                    gesehene_position=[]
                    counter=0#misst verschwendete durchläufe
                    while n:
                        position=r.randint(1,matrix_len**2-1)#matrix_len==len(korrekte_lsg)

                        if position in gesehene_position:
                            counter+=1
                            if counter>matrix_len//2:
                                #print(f"früher abgebrochen bei Fehlergröße {fehlerzahl} und Matrixgröße {matrix_len}!")
                                break
                            continue

                        mod_lsg[position]=mod_lsg[position]^1#xor1 / ein bit geflippt, #müssten aufpassen, dass nicht dieselben bits immer, wieder geflippt werden
                        mod_lsg_geflippt[position]=mod_lsg_geflippt[position]^1#dasselbe für 100% falsch und zu richtig geflippt 
                        n-=1
                    #A;B;C - wenn er durchkommt, ist das ein fehler 
                    #print(mod_lsg)
                    #gesehene_position.append(position) #passiert so selten 
                    if freivald(matr(testmatrix[0]),matr(testmatrix[1]),matr(mod_lsg)):
                        
                        versagen+=1
                    if freivald(matr(testmatrix[0]),matr(testmatrix[1]),matr(mod_lsg)):
                        
                        versagen_gespiegelt+=1

                    ####################################################################################################################
                    #fehler durch Vertauschung
                    while n:
                        pos_row=r.randint(0,matrix_len-1)#zeile
                        pair=r.sample(range(0,matrix_len-1),2)#pärchen wird geswapt, liste
                        pair=[pos +pos_row*matrix_len for pos in pair] #in index kodiert
                        if (pos_row,pair) in gesehene_position:
                            counter+=1
                            if counter>matrix_len//2:
                                #print(f"früher abgebrochen bei Fehlergröße {fehlerzahl} und Matrixgröße {matrix_len}!")
                                break
                            continue

                        swap(mod_lsg_2,pair)#xor1 / ein bit geflippt, #müssten aufpassen, dass nicht dieselben bits immer, wieder geflippt werden
                        gesehene_position.append((pair))

                        n-=1
                    
                    if freivald(matr(testmatrix[0]),matr(testmatrix[1]),matr(mod_lsg)):
                        
                        versagen_zeilen+=1


                durchlauf_2=versagen_gespiegelt/sample
                durchlauf=versagen/sample
                durchlauf_3=versagen_zeilen/sample
                #TODO durchschnitt? smarter machen? Eigene interne Fkt schrieben ...
                #versagen/=sample#durchschnittswert
                #print(fehlerzahl_table_rel_bottomup,laufindex)
                fehlerzahl_table_rel_bottomup[laufindex][0]=fehlerzahl_table_rel_bottomup[laufindex][0]+durchlauf #durchschnittliche Fehlerquote aller samples
                fehlerzahl_table_rel_bottomup[laufindex][1]=fehlerzahl_table_rel_bottomup[laufindex][1]+versagen
                if fehlerzahl_table_rel_bottomup[laufindex][2]>durchlauf:
                    fehlerzahl_table_rel_bottomup[laufindex][2]=durchlauf
                if fehlerzahl_table_rel_bottomup[laufindex][3]<durchlauf:
                    fehlerzahl_table_rel_bottomup[laufindex][3]=durchlauf

                fehlerzahl_table_rel_topdown[laufindex][0]=fehlerzahl_table_rel_topdown[laufindex][0]+durchlauf_2 #durchschnittliche Fehlerquote aller samples
                fehlerzahl_table_rel_topdown[laufindex][1]=fehlerzahl_table_rel_topdown[laufindex][1]+versagen_gespiegelt
                if fehlerzahl_table_rel_topdown[laufindex][2]>durchlauf_2:
                    fehlerzahl_table_rel_topdown[laufindex][2]=durchlauf_2
                if fehlerzahl_table_rel_topdown[laufindex][3]<durchlauf_2:
                    fehlerzahl_table_rel_topdown[laufindex][3]=durchlauf_2
                
                fehlerzahl_table_zeilen[laufindex][0]=fehlerzahl_table_zeilen[laufindex][0]+durchlauf_3 #durchschnittliche Fehlerquote aller samples
                fehlerzahl_table_zeilen[laufindex][1]=fehlerzahl_table_zeilen[laufindex][1]+versagen_zeilen
                if fehlerzahl_table_zeilen[laufindex][2]>durchlauf_2:
                    fehlerzahl_table_zeilen[laufindex][2]=durchlauf_2
                if fehlerzahl_table_zeilen[laufindex][3]<durchlauf_2:
                    fehlerzahl_table_zeilen[laufindex][3]=durchlauf_2


            res_var/zahl_matrizen#nehmen den Durchschnitt aller testmatrizen, hoffentlich ist die Zahl nicht zu klein

        for tupel in fehlerzahl_table_rel_bottomup:
            tupel[0]=tupel[0]/zahl_matrizen #wollen den Durchschnitt haben
        
        for tupel in fehlerzahl_table_rel_topdown:
            tupel[0]=tupel[0]/zahl_matrizen #wollen den Durchschnitt haben
        
        for tupel in fehlerzahl_table_zeilen:
            tupel[0]=tupel[0]/zahl_matrizen #wollen den Durchschnitt haben
        #max, min zwischen verschied. Fehlerwerten anschauen
        #TODO plotten
        #x-wert: [fehlerzahl for fehlerzahl in range(1,matrix_len**2+2,matrix_len)]
        #y-wert: ferhlerzahl_table

        result.append((f"Matrixlänge:{matrix_len}",fehlerzahl_table_rel_bottomup))
        result_großeFehlerquote.append((f"Matrixlänge:{matrix_len}",fehlerzahl_table_rel_topdown))
        result_zeilen.append((f"Matrixlänge:{matrix_len}",fehlerzahl_table_zeilen))
        
    

        ######################################################################################################
       
        

        #untersuchen absoluten Fehler
        fehlerzahl_table_rel=[]


    #print(result)
    anzahl_ausbrücje=0
    sum_abs=0
    for subres in result:
        #[relativer Fehler, absoluter Fehler, lmin,lmax]
        #print(subres[0:3])
        #Fehlerquoten gehen komischerweise runter, je größer die Matrix ist
        #fehler sind absolut selten
        for fehlerinstanz in subres[1]:
            if fehlerinstanz[0]>0 or fehlerinstanz[1]>0:
                print(subres)
                for i in subres[1]:
                    sum_abs+=i[1]
                anzahl_ausbrücje+=1
                break
    print("")
    print("")
    bool=True
    for subres in result_großeFehlerquote: 
        #wenn ein Fehler auftritt, dann nur bei Fehleranzahl/Untershceidung bei 1%
        for fehlerinstanz in subres[1]:
            if fehlerinstanz[0]>0 or fehlerinstanz[1]>0:
                print(subres)#lol sehr interessant - gab mal einen fall mit 98% Untershcied der größe 9x9, welcher nicht erkannt wurde  
                bool=False
                break
    if bool:
        print("Aus der Statistik mit höheren Fehlerquoten gab es nicht einen Fehler!")
    print("")
    print("")
    anzahl_ausbrücje_zeiel=0
    sum_abs_zeilen=0
    for subres in result_zeilen:
        #[relativer Fehler, absoluter Fehler, lmin,lmax]
        #print(subres[0:3])
        #Fehlerquoten gehen komischerweise runter, je größer die Matrix ist
        #fehler sind absolut selten
        for fehlerinstanz in subres[1]:
            if fehlerinstanz[0]>0 or fehlerinstanz[1]>0:
                print(subres)
                anzahl_ausbrücje_zeiel+=1
                for i in subres[1]:
                    sum_abs_zeilen+=i[1]
                break

    print(f"Während es bei direkten Fehler {anzahl_ausbrücje} Ausbrüche mit {sum_abs } Fehler insgesamt gab, gab es bei Zeilenweisigen Fehlern {anzahl_ausbrücje_zeiel} Ausbrüche mit {sum_abs_zeilen} absolute Fehler!")
    return result




res=testing()

exit()

#more testing
A = matr([1, 2, 3, 4]) #* 2**10
print("Transform [1,2,3,4] to ",A)
B = matr([45, 23, 42, 234]) #* 2**10
#C = matr([129, 491, 303, 1004])
#C = matr([129, 491, 303, 1005])
C = mmul(A, B)
print(C)
print(C, A, B)
for i in range(10):
    print(freivald(A, B, C))

# main()