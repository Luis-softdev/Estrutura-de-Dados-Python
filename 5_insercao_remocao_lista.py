# Inserir um elemento em uma lista de alocação sequencial pode ser um processo custoso, dependendo da posição de inserção.
# Se inserirmos no início ou no meio da lista, pode ser necessário deslocar os elementos subsequentes para abrir espaço.
# Se inserirmos no final da lista e ainda houver espaço disponível, geralmente não será necessário mover muitos elementos.

#Exemplo de inserção no final

def insert_at_end(arr, value):
    arr.append(value)  # Usamos append() para adicionar ao final da lista

# Uso:
my_array = [1, 2, 3, 4, 5]
insert_at_end(my_array, 6)

print(my_array)  # Imprime a lista atualizada



# Remover um elemento também pode ser um processo custoso, pois pode ser necessário deslocar elementos para preencher a lacuna deixada pela remoção.
# Se removermos do final da lista, a operação geralmente é mais eficiente, pois não será necessário mover muitos elementos.
# Se removermos do início ou do meio, elementos subsequentes precisarão ser deslocados.

def remove_from_end(arr):
    if len(arr) > 0:
        arr.pop()  # Remove o último elemento
    else:
        print("A lista está vazia.")

# Uso:
my_array = [1, 2, 3, 4, 5]
remove_from_end(my_array)

print(my_array)  # Imprime a lista atualizada


#IMPORTANTE: A quantidade de memória que uma lista consome, é aquela que foi lhe foi reservada no momento da sua criação, ou seja, independente se a lista possui 2 ou 3 elementos, se ela foi criada para suportar 10 elementos, é essa quantidade de espaço que ela está consumindo, porque as outras posições de memória não poderão ser ocupadas por outro programa

# Dessa forma, se a sua lista estiver diminuindo de tamanhp, será mais vantajoso criar uma lista com menos posições de memória para que as que não serão usadas possam ficar disponíveis para outras aplicações.









