from Veiculo import veiculo
class moto(veiculo):
    def __init__(self, placa, valor, alugado, histórico, cilindradas):
        super().__init__(placa, valor, alugado, histórico)
        self.__cilindradas = cilindradas

    def get_cilindradas(self):
        return self.__cilindradas
    def set_cilindradas(self, cilindradas):
        self.__cilindradas = cilindradas