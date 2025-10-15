class Aluno:
    def __init__(self, id=0, nome=""):
        self.__id = id
        self.__nome = nome


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