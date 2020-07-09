lista_simples_inteiro = [1, 2, 3, 14, 4, 5]
lista_simples_string = ["Ola", "Mundo"]
lista_simples_mesclada = [1, 2, 3, "Ola", "Mundo", True, 1.5]
nested_list = [[1, 2], ["Ola", "mundo"]]
print(lista_simples_inteiro)
print(nested_list)

# Len() - Retorna o tamanho de uma lista
print(len(lista_simples_inteiro))
print(len(nested_list))

# Append() - insere elementos no final de uma lista
lista_simples_inteiro.append(6)
print(lista_simples_inteiro)

# Insert() - insere elementos em uma dada posicao da lista
lista_simples_inteiro.insert(6, 7)
print(lista_simples_inteiro)

# Remove() - remove um dado elemento de uma lista
lista_simples_inteiro.remove(5)
print(lista_simples_inteiro)

# Index() - retorna a posicao de um determinado elemento
index = lista_simples_inteiro.index(3)
print(index)

# Count() - retorna a quantidade de um mesmo elemento na lista
count = lista_simples_inteiro.count(2)
print(count)

# Sort() - organiza os elemento de uma lista (Ordenacao)
lista_simples_inteiro.sort(reverse=True)
print(lista_simples_inteiro)
