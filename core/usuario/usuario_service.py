from core.usuario.usuario import UsuarioRepository
from core.usuario.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()


    def listar_usuarios(self):
        return self.repository.listar()
    
    def adicionar_usuario(self, usuario):
          if isinstance(usuario, Usuario):
            return self.repository.adicionar(usuario)    
          else:
            return None
    def atualizar_usuario(self, usuario):
        if isinstance(usuario, Usuario):
            if usuario.id > 0:
                return self.repository.atualizar(usuario)
            else:
                return "ID do usuario é obrigatorio para a atualização"
        else:
            return None

    def remover_usuario(self, usuario_id):
        sucesso = self.repository.remover(usuario_id)
        if not sucesso:
            return None
        else:
            return {"id":usuario_id, "removido": True}
        
    def obter_usuario_por_id(self, usuario_id):    
        usuario = self.repository.obter_por_id(usuario_id)
        if not usuario:
            return None
        else:
            return usuario
        
    def obter_usuario_por_usuario_senha(self, usuario, senha):
        return self.repository.buscar_usuario_por_usuario_senha(usuario, senha)    