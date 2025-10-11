class veiculo:
    def __init__(self, placa, valor, alugado, histórico):
        self.__placa = placa
        self.__valor = valor
        self.__alugado = False
        self.__histórico = histórico

    def get_placa(self):
        return self.__placa
    def set_placa(self, placa):
        self.__placa = placa
    
    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        self.__valor = valor
    
    def get_alugado(self):
        if self.__alugado == False:
            print("O veículo está disponível para aluguel.")
            return True
    def set_alugado(self, alugado):
        self.__alugado = alugado

    def get_histórico(self):
        return self.__histórico
    def set_histórico(self, histórico):
        self.__histórico = histórico
    