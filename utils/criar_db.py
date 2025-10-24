import sqlite3

# Nome do arquivo do banco
DB_NAME = "escola.db"

# Script SQL para criação das tabelas
CREATE_TABLE_ALUNOS_SQL = """
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT NOT NULL
);
"""

CREATE_TABLE_USUARIOS_SQL = """
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL,
    ativo INTEGER NOT NULL
);
"""

CREATE_TABLE_PROFESSORES_SQL = """
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    formacao TEXT NOT NULL
);
"""

CREATE_TABLE_MATERIAS_SQL = """
CREATE TABLE IF NOT EXISTS materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sigla_curricular TEXT NOT NULL,
    descricao TEXT NOT NULL
);
"""

# Dados iniciais
INSERT_INICIAIS_ALUNOS = """
INSERT INTO alunos (nome, idade, cpf) VALUES
('Paulo', 20, "00000000000"),
('Maria', 22, "00000000000"),
('João', 19, "00000000000");
"""

INSERT_INICIAIS_USUARIO = """
INSERT INTO usuarios (usuario, senha, ativo) VALUES
('senai', 'senai123', 1)
"""

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Criar tabela
    cursor.execute(CREATE_TABLE_ALUNOS_SQL)
    cursor.execute(CREATE_TABLE_USUARIOS_SQL)
    cursor.execute(CREATE_TABLE_PROFESSORES_SQL)
    cursor.execute(CREATE_TABLE_MATERIAS_SQL)

    # Inserir dados iniciais só se tabela estiver vazia: alunos
    cursor.execute("SELECT COUNT(*) FROM alunos;")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute(INSERT_INICIAIS_ALUNOS)
        print(">> Dados iniciais inseridos na tabela ALUMOS.")
    else:
        print(">> Tabela ALUNOS já contém dados, nada foi inserido.")

    conn.commit()

    # Inserir dados iniciais só se tabela estiver vazia: usuarios
    cursor.execute("SELECT COUNT(*) FROM usuarios;")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute(INSERT_INICIAIS_USUARIO)
        print(">> Dados iniciais inseridos na tabela USUARIOS.")
    else:
        print(">> Tabela USUÁRIOS já contém dados, nada foi inserido.")

    conn.commit()
    conn.close()

    print(">> Banco inicializado com sucesso!")

if __name__ == "__main__":
    init_db()