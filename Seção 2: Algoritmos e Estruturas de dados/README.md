## Estrutura de Dados

Estruturas de dados servem para organizar os dados de um problema de modo que eles possam ser processados mais eficientemente.

### Pilha (= stack)

São estruturas de dados do tipo LIFO (last-in first-out), onde:

* O último elemento a ser inserido (push):

![](https://github.com/Kianelc/curso-python/blob/master/Se%C3%A7%C3%A3o%202:%20Algoritmos%20e%20Estruturas%20de%20dados/images/pilha_insert.png)

* Será o primeiro a ser retirado (pop):

![](https://github.com/Kianelc/curso-python/blob/master/Se%C3%A7%C3%A3o%202:%20Algoritmos%20e%20Estruturas%20de%20dados/images/pilha_remove.png)

### Fila (= Queue)

São estruturas de dados do tipo FIFO (first-in first-out), onde:

* O primeiro elemento a ser inserido, será o primeiro a ser retirado, ou seja, adiciona-se itens no fim e remove-se do início:

![](https://github.com/Kianelc/curso-python/blob/master/Se%C3%A7%C3%A3o%202:%20Algoritmos%20e%20Estruturas%20de%20dados/images/fila.png)

### Deque (= DoubleEndedQUEue)

Um deque é uma especialização de uma fila, ou seja, é uma fila com duas saídas.

* Inserções e exclusões de elementos podem ocorrer em qualquer extremidade da lista:

![](https://github.com/Kianelc/curso-python/blob/master/Se%C3%A7%C3%A3o%202:%20Algoritmos%20e%20Estruturas%20de%20dados/images/deque.png)

* Collections Deque:

Link da documentação do deque: [https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)

### Vetores

Um  vetor,  ou arranjo (= array), é uma estrutura de dados que armazena uma sequência de objetos, todos do mesmo tipo, em posições consecutivas da memória RAM (= random access memory) do computador.  

![](https://github.com/Kianelc/curso-python/blob/master/Se%C3%A7%C3%A3o%202:%20Algoritmos%20e%20Estruturas%20de%20dados/images/vetores.png)

### Matrizes

São estruturas bi-dimensionais utilizadas para armazenar dados de um mesmo tipo.

![](https://github.com/Kianelc/curso-python/blob/master/Se%C3%A7%C3%A3o%202:%20Algoritmos%20e%20Estruturas%20de%20dados/images/matriz.png)

Uma matriz pode ser considerada como um vetor de vetores, assim, o nome da matriz. Quando os dois índices são fornecidos, então acessamos um elemento da matriz.