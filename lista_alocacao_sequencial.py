lista = [94, 7, 3, 12, 56]
len(lista) - 1 #Último elemento válido


# Em Linguagens que as listas devem ter todos os elementos do mesmo tipo, o posicionamento dos elementos são feitos da seguinte forma:

# Cada elemento sera colocado no término imediato do anterior, já todos compartilham do mesmo tamanho em bytes
# Porém, em Python, podemos constuir listas com tipos diferentres (Inteiros e Strings por exemplo), e se um tipo ocupa, por exemplo, 4 bytes e outro ocupa 6 bytes, a lógica para tentar calcular qual será o próximo endereço e realizar o acesso aleatório. 


# Para contornar isso, independente do tipo de dado que formos armazenar em um lista em Python, a linguagem não irá armazenar o valor propriamente dito, mas sim um outro tipo de dado, chamado de PONTEIRO. Consturindo assim uma lista de alocação sequencial com o mesmo tipo, o tipo ponteiro.

    # Os ponteiros servem para armazenar os endereços de memória de outros valores.
    # Isso traz também uma desvantagem de que, ao lidar com ponteiros, estaremos sempre lidando com um intermediário, e não com o valor em si.