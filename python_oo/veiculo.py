import abc, interface_veiculo


class Veiculo(interface_veiculo.InterfaceVeiculo, abc.ABC):
    """Essa e a classe Carro, usada para instanciar novos carros em nosso programa"""

    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0

    def __del__(self):
        print("O objecto foi removido da memoria :)")

    @property
    def cor(self):
        return self._cor

    def pintar(self, cor):
        self._cor = cor

    def abastecer(self, qtd_combustivel):
        """O metodo abastecer recebe como parametro a quantidade de combustivel e incrementa no
        atributo qtd_combustivel do nosso objecto"""
        self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            print("O veiculo ja esta ligado!")
        else:
            self.__is_ligado = True
            print("O veiculo foi ligado!")

    def desligar(self):
        if not self.__is_ligado:
            print("O veiculo ja esta desligado")
        else:
            self.__is_ligado = False

    def acelerar(self, velocidade=10):
        if self.__is_ligado:
            self.__velocidade += velocidade
        else:
            print("O carro precisa estar ligado para acelerar")