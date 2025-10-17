from core.aluno.aluno_repository import AlunoRepository
from core.aluno.aluno import Aluno

class AlunoService:
    def __init__(self):
        self.repository = AlunoRepository()


    def listar_alunos(self):
        return self.repository.listar()
    
    def adicionar_aluno(self, aluno):
          if isinstance(aluno, Aluno):
            return self.repository.adicionar(aluno)    
          else:
            return None
    def atualizar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            if aluno.id > 0:
                return self.repository.atualizar(aluno)
            else:
                return "ID do aluno é obrigatorio para a atualização"
        else:
            return None

    def remover_aluno(self, aluno_id):
        sucesso = self.repository.remover(aluno_id)
        if not sucesso:
            return None
        else:
            return {"id":aluno_id, "removido": True}
        
    def obter_aluno_por_id(self, aluno_id):    
        aluno = self.repository.obter_por_id(aluno_id)
        if not aluno:
            return None
        else:
            return aluno
        
