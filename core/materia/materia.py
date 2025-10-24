class Materia:
    def __init(self, id=None, nome="", sigla_curricular="", descricao=""):
        self.__id = id
        self.__nome = nome
        self.__sigla_curricular = sigla_curricular
        self.__descricao = descricao


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id


    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def sigla_curricular(self):
        return self.__sigla_curricular
    @sigla_curricular.setter
    def sigla_curricular(self, nova_sigla_curricular):
        self.__sigla_curricular = nova_sigla_curricular

    @property
    def descricao(self):
         return self.__descricao
    @descricao.setter
    def descricao(self, novo_descricao):
        self.__descricao = novo_descricao