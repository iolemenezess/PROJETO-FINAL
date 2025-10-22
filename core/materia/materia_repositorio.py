import sqlite3

DB_NAME = "escola.db"

# MateriaRepository: Responsável por acessar e manipular os dados da aplicação.
class MateriaRepository:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def listar(self):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, sigla_curricular, descricao FROM materias;")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "nome": row[1], "sigla_curricular": row[2], "descricao": row[3]} for row in rows]

    def obter_por_id(self, materia_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, sigla_curricular, descricao FROM materias WHERE id = ?;", (materia_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "nome": row[1], "sigla_curricular": row[2], "descricao": row[3]}
        return None

    def adicionar(self, obj_materia):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO materias (nome, sigla_curricular, descricao) VALUES (?, ?, ?);", (obj_materia.nome, obj_materia.sigla_curricular, obj_materia.descricao))
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return {"id": novo_id, "nome": obj_materia.nome, "sigla_curricular": obj_materia.idade, "descricao": obj_materia.descricao}

    def atualizar(self, obj_materia):
        conn = self.conectar()
        cursor = conn.cursor()

        # Buscar aluno antes de atualizar
        cursor.execute("SELECT id, nome, sigla_curricular, descricao FROM materias WHERE id = ?;", (obj_materia.id,))
        row = cursor.fetchone()
        if not row:
            conn.close()
            return None

        cursor.execute(
            "UPDATE materias SET nome = ?, sigla_curricular = ?, descricao = ? WHERE id = ?;",
            (obj_materia.nome, obj_materia.sigla_curricular, obj_materia.descricao, obj_materia.id),
        )
        conn.commit()
        conn.close()
        return {"id": obj_materia.id, "nome": obj_materia.nome, "sigla_curricular": obj_materia.sigla_curricular, "descricao": obj_materia.descricao}

    def remover(self, materia_id):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM materias WHERE id = ?;", (materia_id,))
        conn.commit()
        linhas_afetadas = cursor.rowcount
        conn.close()
        return linhas_afetadas > 0