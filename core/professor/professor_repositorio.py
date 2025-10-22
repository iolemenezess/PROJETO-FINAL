import sqlite3

DB_NAME = "escola.db"

# AlunoRepository: Responsável por acessar e manipular os dados da aplicação.
class ProfessorRepository:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def listar(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, idade, formacao FROM professores;")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "nome": row[1], "idade": row[2], "formacao": row[3]} for row in rows]

    def obter_por_id(self, prof_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, idade, formacao FROM professores WHERE id = ?;", (prof_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "nome": row[1], "idade": row[2], "formacao": row[3]}
        return None

    def adicionar(self, obj_professor):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO professores (nome, idade, formacao) VALUES (?, ?, ?);", (obj_professor.nome, obj_professor.idade, obj_professor.formacao))
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return {"id": novo_id, "nome": obj_professor.nome, "idade": obj_professor.idade, "cpf": obj_professor.formacao}

    def atualizar(self, obj_professor):
        conn = self.conectar()
        cursor = conn.cursor()

        # Buscar aluno antes de atualizar
        cursor.execute("SELECT id, nome, idade, formacao FROM professores WHERE id = ?;", (obj_professor.id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None

        cursor.execute(
            "UPDATE professores SET nome = ?, idade = ?, formacao = ? WHERE id = ?;",
            (obj_professor.nome, obj_professor.idade, obj_professor.formacao, obj_professor.id),
        )
        conn.commit()
        conn.close()
        return {"id": obj_professor.id, "nome": obj_professor.nome, "idade": obj_professor.idade, "formacao": obj_professor.formacao}

    def remover(self, prof_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM professores WHERE id = ?;", (prof_id,))
        conn.commit()
        linhas_afetadas = cursor.rowcount
        conn.close()
        return linhas_afetadas > 0