# Exemplo para entender o conceito de complexidade

def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho//2
    for i in range(limite):
        aux = lista[i]
        lista[i] = lista[n-i]
        lista[tamanho-i] = aux

# 4 variáveis + N valores ==== Complexidade em Espaço (Memória)
# 2 operações elementares + 3*(N/2) === Complexidade em Tempo (Processamento)

def inverter_lista2(lista):
    nova_lista+[]
    tamanho = len(lista)
    for i in range(tamanho):
        nova_lista.append(lista[tamanho-i])
    return nova_lista


# 2 + N === Complexidade em Tempo (Processamento)
# 3 + 2*N === Complexidade em Espaço (Memória)