class cliente():
    def __init__(self, nome):
        self.__nome = nome
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome

    def __str__(self):
        return "Cliente com o nome: " + self.getnome()