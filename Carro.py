
from Veiculo import veiculo


class carro(veiculo):
    def __init__(self, modelo, placa, valor):
        super().__init__(placa, valor)
        self.__modelo = modelo
 
    
    # Getter - Pega o valor
    def get_modelo(self):
        return self.__modelo

    # Setter - Seta um valor
    def set_modelo(self,modelo):
        self.__modelo = modelo

    def Calcular_Aluguel(self, dias):
        return  self.get_valor() * dias
    
    
    
        