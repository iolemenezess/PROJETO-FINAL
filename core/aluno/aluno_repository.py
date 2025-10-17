import sqlite3

DB_NAME = "escola.db"

# AlunoRepository: Responsável por acessar e manipular os dados da aplicação.
class AlunoRepository:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def listar(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, idade, cpf FROM alunos;")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "nome": row[1], "idade": row[2], "cpf": row[3]} for row in rows]

    def obter_por_id(self, aluno_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, idade, cpf FROM alunos WHERE id = ?;", (aluno_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "nome": row[1], "idade": row[2], "cpf": row[3]}
        return None

    def adicionar(self, obj_aluno):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alunos (nome, idade, cpf) VALUES (?, ?, ?);", (obj_aluno.nome, obj_aluno.idade, obj_aluno.cpf))
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return {"id": novo_id, "nome": obj_aluno.nome, "idade": obj_aluno.idade, "cpf": obj_aluno.cpf}

    def atualizar(self, obj_aluno):
        conn = self.conectar()
        cursor = conn.cursor()

        # Buscar aluno antes de atualizar
        cursor.execute("SELECT id, nome, idade, cpf FROM alunos WHERE id = ?;", (obj_aluno.id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None

        cursor.execute(
            "UPDATE alunos SET nome = ?, idade = ?, cpf = ? WHERE id = ?;",
            (obj_aluno.nome, obj_aluno.idade, obj_aluno.cpf, obj_aluno.id),
        )
        conn.commit()
        conn.close()
        return {"id": obj_aluno.id, "nome": obj_aluno.nome, "idade": obj_aluno.idade, "cpf": obj_aluno.cpf}

    def remover(self, aluno_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE id = ?;", (aluno_id,))
        conn.commit()
        linhas_afetadas = cursor.rowcount
        conn.close()
        return linhas_afetadas > 0