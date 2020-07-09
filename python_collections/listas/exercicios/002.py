from array import array


reais = array('f', [])

for i in range(0, 10):
    reais.append(int(input(f"Digite o valor da Posicao {i}: ")))

print(reais)
