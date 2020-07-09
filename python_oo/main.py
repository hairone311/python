import carro, moto, veiculo, pessoa

uno_vermelho = carro.Carro("Vermelho", "Flex", 1.0, 4)
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
uno_vermelho.acelerar(20)
uno_vermelho.pintar("preto")
print(uno_vermelho.cor)
print(f"A quantidade de combustivel do Uno Vermelho e: ")

moto_vermelha = moto.Moto("Vermelha", "Gasolina", 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)

pessoa = pessoa.Pessoa("Joao")

if isinstance(pessoa, veiculo.Veiculo):
    print("A classe e um veiculo")
else:
    print("A classe nao e um veiculo")