# A ideia da Alocação Encadeada ou Dinâmica, é permitir que os elementos possam ser armazenados em espaços quaisquer da memória, sem que precisem estar um ao lado do outro como na Alocação Sequencial, e esses espaços serem alocados apenas quando precise armazenar um novo elemento, sema a necessidade de ter uma "reserva". 

# Eis que surge o problema, unir esses espaços, já que não estão um ao lado do outro. Dessa forma, é necessário criar uma estrutura auxiliar chamada de NÓ
    # A ideia de um NÓ é funcionar como um envelope, que tem um espaço para armazenar o dado e outro para armazenar  posição do nó seguinte.
    # Assim temos a grande sacada sobre os Nó's, se tivermos a referência de ao menos 1 elemento, poderemos transitar por todos os outros, já que cada um possui o endereço do próximo
    # Porém, é necessário lembrar que só é posspivel andar pra frente em relação aos Nó's, um nó não sabe a posição do nó anterior, apenas do posterior.


# O código para a construção de um NÓ é bem simples:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # O próximo nó é None
