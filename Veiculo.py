class veiculo:
    # Apenas placa e valor são obrigatórios na inicialização
    def __init__(self, placa, valor, alugado=False):
        self.__placa = placa
        self.__valor = valor
        self.__alugado = alugado  
        self.__historico = [] 

    # --- GETTERS (gets) ---
    def get_placa(self):
        return self.__placa

    def get_valor(self):
        return self.__valor

    def get_alugado(self):
        return self.__alugado

    def get_historico(self):
        return self.__historico[:]

    # --- SETTERS (sets) ---
    def set_placa(self, nova_placa):
        if len(nova_placa) > 6:
            self.__placa = nova_placa
        else:
            print("Placa inválida.")

    def set_valor(self, novo_valor):
        if novo_valor >= 0:
            self.__valor = novo_valor
        else:
            print("Valor inválido.")
            
    def set_alugado(self, estado):
        self.__alugado = estado

    def add_registro_historico(self, registro):
        self.__historico.append(registro)
        print("Registro adicionado ao histórico.")

    def remove_registro_historico(self, indice):
        try:
            removido = self.__historico.pop(indice)
            print(f"Registro removido: {removido}")
            return removido
        except IndexError:
            print("Índice inválido no histórico.")
            return None

    # --- Métodos de Negócio (Alugar/Devolver ajustados) ---
    def alugar(self, cliente, dias):
        if self.get_alugado():
            print("Veículo indisponível para aluguel.")
        else:
            self.set_alugado(True)
            registro = (cliente, self.get_placa(), dias, "Alugado")
            self.add_registro_historico(registro)
            print(f"Veículo alugado para {cliente} por {dias} dias.")

    def devolvido(self):
        if not self.get_alugado():
            print("Veículo já está disponível.")
        else:
            self.set_alugado(False)
            registro = (self.get_placa(), "Devolvido")
            self.add_registro_historico(registro)
            print("Veículo devolvido e agora está disponível.")

    # --- Método Especial __str__ ---
    def __str__(self):
        status = "Alugado" if self.get_alugado() else "Disponível"
        return (f"Veículo [Placa: {self.get_placa()}, Valor Diário: R${self.get_valor():.2f}, "
                f"Status: {status}, Histórico de {len(self.get_historico())} eventos]")
