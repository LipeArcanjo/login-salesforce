# Lista para armazenar os usuários cadastrados
usuarios = []

# Função para exibir o menu
def exibir_menu():
    print("Menu:")
    print("---------------------------------")
    print("1. Cadastrar-se")
    print("2. Login")
    print("3. Alterar Acessibilidades Cadastradas")
    print("4. Visualizar Acessibilidades Cadastradas")

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    global nome_usuario
    nome_usuario = input("Digite o Nome de Usuário: ")
    global senha
    senha = input("Digite a Senha: ")
    nome_completo = input("Digite o Nome Completo: ")
    email = input("Digite o Endereço de E-mail: ")

    suporte_acessibilidade = input("Deseja suporte para acessibilidade? (Sim/Não): ")

    if suporte_acessibilidade.lower() == "sim":
        opcoes_acessibilidade = ["Daltonismo", "Idoso", "Mobilidade Reduzida", "Deficiente Visual", "Deficiente Auditivo", "Dislexia"]
        acessibilidade = obter_acessibilidade(opcoes_acessibilidade)
    else:
        acessibilidade = "Nenhuma"

    usuarios.append({
        "Nome de Usuário": nome_usuario,
        "Senha": senha,
        "Nome Completo": nome_completo,
        "Endereço de E-mail": email,
        "Acessibilidade": acessibilidade
    })

    print("Cadastro realizado com sucesso!")

# Função para obter as opções de acessibilidade
def obter_acessibilidade(opcoes_acessibilidade):
    print("Opções de Acessibilidade:")
    for i, opcao in enumerate(opcoes_acessibilidade, 1):
        print(f"{i}. {opcao}")

    acessibilidade = []
    escolha_acessibilidade = int(input("Escolha a opção de acessibilidade (1-6) ou 0 para sair: "))

    while escolha_acessibilidade != 0:
        acessibilidade.append(opcoes_acessibilidade[escolha_acessibilidade - 1])
        escolha_acessibilidade = int(input("Você gostaria de adicionar outra acessibilidade? (1-6) ou 0 para sair: "))
        if (escolha_acessibilidade < 0 or escolha_acessibilidade > 6):
            print("Opção inválida. Acessibilidade não configurada.")
            escolha_acessibilidade = int(input("Escolha uma opção de acessibilidade válida (1-6): "))

    return acessibilidade

# Função para alterar as acessibilidades cadastradas
def alterar_acessibilidades():
    nome_usuario = input("Digite o Nome de Usuário para alterar as acessibilidades: ")

    for usuario in usuarios:
        if usuario["Nome de Usuário"] == nome_usuario:
            opcoes_acessibilidade = ["Daltonismo", "Idoso", "Mobilidade Reduzida", "Deficiente Visual", "Deficiente Auditivo", "Dislexia"]
            acessibilidade = obter_acessibilidade(opcoes_acessibilidade)
            usuario["Acessibilidade"] = acessibilidade
            print("Acessibilidades alteradas com sucesso!")
            return

    print(f"Usuário '{nome_usuario}' não encontrado.")

# Função para visualizar as acessibilidades cadastradas
def visualizar_acessibilidades():
    nome_usuario = input("Digite o Nome de Usuário para visualizar as acessibilidades: ")

    for usuario in usuarios:
        if usuario["Nome de Usuário"] == nome_usuario:
            print(f"Acessibilidades de '{nome_usuario}': {usuario['Acessibilidade']}")
            return

    print(f"Usuário '{nome_usuario}' não encontrado.")

# Função para realizar o login
def realizar_login():
    nome_usuario_login = input("Digite o Nome de Usuário: ")
    senha_login = input("Digite a sua senha: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if nome_usuario == nome_usuario_login and senha == senha_login:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print(f"Bem-vindo, {usuario_encontrado['Nome Completo']}!")
        if usuario_encontrado['Acessibilidade'] != "Nenhuma":
            print(f"Suporte de acessibilidade: {usuario_encontrado['Acessibilidade']}")
    else:
        print("Nome de Usuário ou Senha incorretos. Tente novamente.")
        realizar_login()