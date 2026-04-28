import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="oficina",
    user="postgres",
    password="1234"
)

cursor = conn.cursor()

def login():
    user = input("Usuário: ")
    senha = input("Senha: ")
    if user == "admin" and senha == "123":
        menu()
    else:
        print("Login inválido!")

def cadastrar_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    cursor.execute("INSERT INTO clientes (nome, telefone) VALUES (%s, %s)", (nome, telefone))
    conn.commit()

def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    for row in cursor.fetchall():
        print(row)

def atualizar_cliente():
    id_cliente = input("ID: ")
    telefone = input("Novo telefone: ")
    cursor.execute("UPDATE clientes SET telefone = %s WHERE id_cliente = %s", (telefone, id_cliente))
    conn.commit()

def deletar_cliente():
    id_cliente = input("ID: ")
    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
    conn.commit()

def consulta_join():
    cursor.execute("""
    SELECT c.nome, v.modelo, o.descricao, o.valor
    FROM ordens_servico o
    INNER JOIN veiculos v ON o.id_veiculo = v.id_veiculo
    INNER JOIN clientes c ON v.id_cliente = c.id_cliente
    """)
    for row in cursor.fetchall():
        print(row)

def menu():
    while True:
        print("1-Cadastrar 2-Listar 3-Atualizar 4-Deletar 5-Join 0-Sair")
        op = input("Escolha: ")
        if op == "1":
            cadastrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            atualizar_cliente()
        elif op == "4":
            deletar_cliente()
        elif op == "5":
            consulta_join()
        elif op == "0":
            break

login()
