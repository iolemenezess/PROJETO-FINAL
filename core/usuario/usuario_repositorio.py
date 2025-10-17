import sqlite3
from core.usuario.usuario import Usuario

DB_NAME = "escola.db"

class UsuarioRepository:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def listar(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, usuario, senha, ativo FROM usuarios;")
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": row[0], "usuario": row[1], "senha": row[2], "ativo": bool(row[3])}
            for row in rows
        ]

    def obter_por_id(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, usuario, senha, ativo FROM usuarios WHERE id = ?;", (usuario_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "usuario": row[1], "senha": row[2], "ativo": bool(row[3])}
        return None

    def adicionar(self, obj_usuario: Usuario):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (usuario, senha, ativo) VALUES (?, ?, ?);",
            (obj_usuario.usuario, obj_usuario.senha, int(obj_usuario.ativo)),
        )
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return {"id": novo_id, "usuario": obj_usuario.usuario, "ativo": obj_usuario.ativo}

    def atualizar(self, obj_usuario: Usuario):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuarios SET usuario = ?, senha = ?, ativo = ? WHERE id = ?;",
            (obj_usuario.usuario, obj_usuario.senha, int(obj_usuario.ativo), obj_usuario.id),
        )
        conn.commit()
        linhas = cursor.rowcount
        conn.close()
        return linhas > 0

    def remover(self, usuario_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?;", (usuario_id,))
        conn.commit()
        linhas = cursor.rowcount
        conn.close()
        return linhas > 0
   
    def buscar_usuario_por_usuario_senha(self, usuario, senha):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, usuario, senha, ativo FROM usuarios WHERE usuario = ? AND senha = ? AND ativo = 1;", (usuario, senha))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "usuario": row[1], "senha": row[2], "ativo": bool(row[3])}
        return None