from core.professor.professor_repositorio import ProfessorRepository
from core.professor.professor import Professor

class ProfessorService:
    def __init__(self):
        self.repository = ProfessorRepository()


    def listar_professor(self):
        return self.repository.listar()
    
    def adicionar_professor(self, professor):
          if isinstance(professor, Professor):
            return self.repository.adicionar(professor)    
          else:
            return None
    def atualizar_professor(self, professor):
        if isinstance(professor, Professor):
            if professor.id > 0:
                return self.repository.atualizar(professor)
            else:
                return "ID do professor é obrigatorio para a atualização"
        else:
            return None

    def remover_professor(self, professor_id):
        sucesso = self.repository.remover(professor_id)
        if not sucesso:
            return None
        else:
            return {"id":professor_id, "removido": True}
        
    def obter_professor_por_id(self, professor_id):    
        professor = self.repository.obter_por_id(professor_id)
        if not professor:
            return None
        else:
            return professor
        
