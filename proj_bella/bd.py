import sqlite3

# Conectar ao banco
conexao = sqlite3.connect("adaptedu.db")

# Ativar chaves estrangeiras
conexao.execute("PRAGMA foreign_keys = ON")

# Criar cursor
cursor = conexao.cursor()


# =========================
# TABELA DE TURMAS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS turmas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")


# =========================
# TABELA DE USUÁRIOS
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    turma_id INTEGER,
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
)
""")


# =========================
# INSERIR TURMAS
# =========================

cursor.execute(
    "INSERT OR IGNORE INTO turmas (id, nome) VALUES (?, ?)",
    (1, "Turma A")
)

cursor.execute(
    "INSERT OR IGNORE INTO turmas (id, nome) VALUES (?, ?)",
    (2, "Turma B")
)


# =========================
# INSERIR USUÁRIOS
# =========================

usuarios = [
    ("Isabella", 17, 1),
    ("Ana", 16, 1),
    ("João", 17, 2),
    ("Maria", 16, 2)
]

cursor.executemany("""
INSERT INTO usuarios (nome, idade, turma_id)
VALUES (?, ?, ?)
""", usuarios)


# Salvar
conexao.commit()


# =========================
# LISTAR USUÁRIOS
# =========================

cursor.execute("SELECT * FROM usuarios")

resultado = cursor.fetchall()

print("USUÁRIOS:")

for usuario in resultado:
    print(usuario)


# Fechar
conexao.close()