# Soft heap

Definition (Variante Chazelle 2000):
Ein Soft heap besteht aus eine Folge von modifizierten Binomialbäumen mit jeweils unterschiedlichem Rank, auch als $soft queues$ bekannt

(sehr große Ähnlchkeit zu Fib-Heaps)

Ein soft queue q ist ein Binomialbaum mit möglich fehlenden Teilbäumen.
Besonders ist die Invariante k< rank(root)/2

Ein Knoten v kann mehrere Elemente speichern

Operations:
-create($\S$): Erzeugt Soft heap
-insert($\S$,x): Fügt Element x zu $\S$ hinzu
-meld($\S,\S'$): Vereint zwei Heaps zu einem (ann. disjoint)
-delete($\S,x$): Entferne x aus $\S$

## Generelles

[Wiki](https://en.wikipedia.org/wiki/Soft_heap)
Vater Chazelle des Soft Heaps und seine Analysen, Sie finden auch eine C-Implementierung der Datenstruktur [Journal](https://www.cs.princeton.edu/~chazelle/pubs/sheap.pdf).
Es existieren jedoch noch einfachere, genau so gute Versionen durch Kaplan, Zwick, Tarjan:
[Paper](https://epubs.siam.org/doi/pdf/10.1137/1.9781611973068.53)
[Paper](https://epubs.siam.org/doi/10.1137/120880185)
Anwendungen:
MST in $O(m\alpha (m,n))$ [Paper](https://dl.acm.org/doi/10.1145/355541.355562)
Selection in $O(n)$
approximatives Sortieren in $O(nlogn)$ Vergleichen
