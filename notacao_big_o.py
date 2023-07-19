# O(1) - Tempo de execução constante: O algoritmo leva a mesma quantidade de tempo, independentemente do tamanho da entrada. Por exemplo, acessar um elemento em uma lista por seu índice é uma operação de tempo constante.

def acessa_elemento(lista, indice):
    return lista[indice]


# O(n) - Tempo de execução linear: O tempo de execução cresce linearmente com o tamanho da entrada. Por exemplo, percorrer uma lista para imprimir todos os elementos.

def imprimir_lista(lista):
    for item in lista:
        print(item)

# O(n^2) - Tempo de execução quadrático: O tempo de execução cresce quadraticamente com o tamanho da entrada. Algoritmos de ordenação como o Bubble Sort se enquadram nessa categoria.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# 4 PONTOS IMPORTANTES

#1 A complexidade de um algortimo é uma medida da quantidade de recursos que foram demandados por ele para a sua execução, independente da Linguagem de Programação e Máquina Utilizada
#2 O que mais importa acerca da complexidade de um algortimo, é como que ela cresce com o tamanho da entrada
#3 Nós expressamos a Complexidade de Algoritmos com o BigO, focando no termo dominante da função
#4 Quando um algoritmo pode encerrar de várias maneiras diferentes, fazendo um número diferente de operações, vamos calcular a complexidade do pior caso

