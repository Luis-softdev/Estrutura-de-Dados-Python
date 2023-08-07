# Busca linear em lista de alocação sequencial

def busca(lista, elem):
    """Retorna o íncide do elemento se ele estiver na lista ou None, caso o contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None    

lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = 14

indice = busca(lista_estranha, elemento)

if indice is not None:
    print("O índice do elemento {} é {}".format(elemento,indice))
else: 
    print("O elemento {} não se encontra na lista".format(elemento))



# SOBRE A COMPLEXIDADE DESSE ALGORITMO

# A quantidade de operações que realizamos nesse algoritmo de busca, depende de qual elemento estamos procurando, mais especificamente, da posição desse elemento.

# O pior caso nesse algoritmo seria num cenário em que o elemento procurado não está na lista, já que ele teria que percorrer todos os elementos até o último para chegar nessa conclusão.  

# Podemos afirmar então que a complexidade desse algoritmo é LINEAR [O(n)] com o tamanho da entrada, ou seja, depende de quantos elementos a lista tem e qual estamos procurando.

# Se não tivermos mais nenhuma informação sobre uma lista, essa é a melhor opção, porém, se a lista estiver ORDENADA, podemos aplicar um Algoritmo de BUSCA BINÁRIA, que é muito mais eficiente.

# O algoritmo de busca binária divide a lista pela metade tomando como base o elemento que está no meio, a partir dele, ele verifica se o elemento procurado é maior, igual ou menor àquele que está como base, podendo excluir metade da lista no caso do número procurado ser menor ou maior, aprimorando e acelerando a busca. A complexidade desse algoritmo é [O log N]

