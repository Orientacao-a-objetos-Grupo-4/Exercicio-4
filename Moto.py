from Veiculo import veiculo
class moto(veiculo):
    def __init__(self, placa, valor, alugado, histórico, calcularAluguel):
        super().__init__(placa, valor, alugado, histórico)
        self.__calcularAluguel = calcularAluguel

    def get_valorAluguel(self):
        return self.__calcularAluguel
    def set_valorAluguel(self, calcularAluguel):
        self.__calcularAluguel = calcularAluguel

    def __str__(self):
        return (f"Placa: {self.get_placa()}\n"
                f"Valor: {self.get_valor()}\n" 
                f"Valor do Aluguel: {self.get_valorAluguel()}\n"
                f"Alugado: {self.get_alugado()}\n"
                f"Histórico: {self.get_histórico()}\n") 