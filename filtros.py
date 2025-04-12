
import sqlite3

# Connect to the database
conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

# Menu de opções
print("\nFiltro de Logs de Acesso")
print("1. Logins com falha")
print("2. Acessos de um usuário específico")
print("3. Tentativas de acesso após uma data")
print("4. IPs com mais tentativas")
opcao = input("Escolha uma opção (1-4): ")

if opcao == '1':
    cursor.execute("SELECT * FROM logs_acesso WHERE acao = 'falha_login'")
elif opcao == '2':
    usuario = input("Digite o nome do usuário: ")
    cursor.execute("SELECT * FROM logs_acesso WHERE usuario = ?", (usuario,))
elif opcao == '3':
    data = input("Digite a data no formato YYYY-MM-DD HH:MM:SS: ")
    cursor.execute("SELECT * FROM logs_acesso WHERE data_acesso > ?", (data,))
elif opcao == '4':
    cursor.execute("""
        SELECT ip_origem, COUNT(*) AS tentativas
        FROM logs_acesso
        GROUP BY ip_origem
        ORDER BY tentativas DESC
    """)
else:
    print("Opção inválida.")
    conn.close()
    exit()

# Mostrar os resultados
registros = cursor.fetchall()
print("\nResultados:")
for linha in registros:
    print(linha)

# Fechar conexão
conn.close()
