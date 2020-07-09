lista_simples_inteiro = [1, 2, 3, 14, 4, 5]
lista_quadrado = []
for i in lista_simples_inteiro:
    lista_quadrado.append(i**2)
print(lista_quadrado)

nova_lista = [i**2 for i in lista_simples_inteiro]
print(nova_lista)
