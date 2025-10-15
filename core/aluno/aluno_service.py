from core.aluno.aluno_repository import AlunoRepository
from core.aluno.aluno import Aluno

class AlunoService:
    def __init__(self):
        self.repository = AlunoRepository


    def listar_alunos(self):
        return self.repository.listar()
    
    def adicionar_aluno(self, aluno):
          if isinstance(aluno, Aluno):
            return self.repository.adicionar(aluno)    
          else:
            return None