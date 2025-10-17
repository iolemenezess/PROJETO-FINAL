class Aluno:
    def __init__(self, id=0, nome="", idade=0, cpf=""):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id ):
        self.__id = novo_id   

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf   