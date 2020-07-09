from array import array

array_1 = array('B', [1, 2, 3, 4, 5, 6])

# print(array_1)
#
# for i in array_1:
#    print(i)

# inserindo elementos no array
array_1.insert(2, 50)

# for i in array_1:
#    print(i)

# Removendo elementos do array
array_1.remove(4)

# for i in array_1:
#    print(i)

# Buscando elementos em um array
print(array_1.index(50))

# Atualizando dados em um array
array_1[2] = 55

array_1.append(6)

for i in array_1:
    print(i)
