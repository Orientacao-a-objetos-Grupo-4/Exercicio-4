from Veiculo import veiculo
class moto(veiculo):
    def __init__(self, placa, valor):
        super().__init__(placa, valor)

    def calcularAluguel(self, dias):
        valorAluguel = self.get_valor() * dias 
        if dias >= 30:
            valorAluguel *= 1.10
        else:
            valorAluguel *= 1.20
        return valorAluguel
