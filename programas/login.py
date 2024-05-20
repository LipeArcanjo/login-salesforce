# Imports necessários
import oracledb as orcl
import pandas as pd
import json
# Configurações para exibir todas as colunas e linhas do DataFrame
pd.set_option('display.max_columns', None)  # Exibe todas as colunas
pd.set_option('display.max_rows', None)     # Exibe todas as linhas


# Conexão com o Banco de Dados!
try:
    #String de conexão com o Servidor do BD
    str_conect = orcl.makedsn("oracle.fiap.com.br","1521","ORCL")
    #Efetuar a conexão com o Oracle usando as minhas credenciais
    conect = orcl.connect(user="rm554018",password="170404",dsn=str_conect)

    instrucao_SQL = conect.cursor()
except Exception as erro:
    print("Erro: ",erro)
    conexao = False
else:
    conexao = True

# Função para exibir o menu
def exibir_menu():
    print("Menu:")
    print("---------------------------------")
    print("1. Cadastrar-se")
    print("2. Login")
    print("3. Alterar cadastro")
    print("4. Alterar acessibilidades cadastradas")
    print("5. Visualizar acessibilidades cadastradas")
    print("6. Deletar usuário")
    print("7. Visualizar usuários cadastrados")
    print("8. Visualizar usuários por acessibilidade")

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    try:
        nome_usuario = input("Digite o Nome de Usuário: ")
        senha = input("Digite a Senha: ")
        nome_completo = input("Digite o Nome Completo: ")
        email = input("Digite o Endereço de E-mail: ")

        suporte_acessibilidade = input("Deseja suporte para acessibilidade? (Sim/Não): ")

        if suporte_acessibilidade.lower() == "sim":
            opcoes_acessibilidade = ["Daltonismo", "Idoso", "Mobilidade Reduzida", "Deficiente Visual", "Deficiente Auditivo", "Dislexia"]
            acessibilidade = obter_acessibilidade(opcoes_acessibilidade)
            acessibilidade_str = ', '.join(acessibilidade)  # Convertendo a lista em uma string separada por vírgulas
        else:
            acessibilidade_str = "Nenhuma"

        # Código para inserção
        insercao = """INSERT INTO usuarios (usuarios_nome_usuario, usuarios_nome_completo, usuarios_email, usuarios_senha, usuarios_acessibilidade) 
                      VALUES (:nome_usuario,:nome_completo,:email,:senha, :acessibilidade)"""

        # Executar a inserção no banco de dados
        instrucao_SQL.execute(insercao, {'nome_usuario': nome_usuario, 'senha': senha, 'nome_completo': nome_completo, 'email': email, 'acessibilidade': acessibilidade_str})
        conect.commit()
        print("Dados gravados com sucesso!")
    except ValueError:
        print("Digite dados numéricos")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("\n")


# Função para alterar cadastro
def alterar_cadastro():
    try:
        nome_usuario = input("Digite o Nome de Usuário para alterar o cadastro: ")
        print("O que você deseja alterar?")
        print("1. Senha")
        print("2. Nome Completo")
        print("3. Endereço de E-mail")
        print("4. Alterar tudo")
        opcao = int(input("Digite o número da opção: "))

        if opcao == 1:
            nova_senha = input("Digite a nova Senha: ")
            instrucao_SQL.execute(
                "UPDATE usuarios SET usuarios_senha = :nova_senha WHERE usuarios_nome_usuario = :nome_usuario",
                {'nova_senha': nova_senha, 'nome_usuario': nome_usuario})
            conect.commit()
            print("Senha alterada com sucesso!")
        elif opcao == 2:
            novo_nome_completo = input("Digite o novo Nome Completo: ")
            instrucao_SQL.execute(
                "UPDATE usuarios SET usuarios_nome_completo = :novo_nome_completo WHERE usuarios_nome_usuario = :nome_usuario",
                {'novo_nome_completo': novo_nome_completo, 'nome_usuario': nome_usuario})
            conect.commit()
            print("Nome Completo alterado com sucesso!")
        elif opcao == 3:
            novo_email = input("Digite o novo Endereço de E-mail: ")
            instrucao_SQL.execute(
                "UPDATE usuarios SET usuarios_email = :novo_email WHERE usuarios_nome_usuario = :nome_usuario",
                {'novo_email': novo_email, 'nome_usuario': nome_usuario})
            conect.commit()
            print("Endereço de E-mail alterado com sucesso!")
        elif opcao == 4:
            novo_nome_usuario = input("Digite o novo Nome de Usuário: ")
            nova_senha = input("Digite a nova Senha: ")
            novo_nome_completo = input("Digite o novo Nome Completo: ")
            novo_email = input("Digite o novo Endereço de E-mail: ")
            instrucao_SQL.execute("UPDATE usuarios SET usuarios_senha = :nova_senha, usuarios_nome_completo = :novo_nome_completo, usuarios_email = :novo_email WHERE usuarios_nome_usuario = :nome_usuario",{'nova_senha': nova_senha, 'novo_nome_completo': novo_nome_completo , 'novo_email': novo_email ,'nome_usuario': nome_usuario})
            conect.commit()
            print("\nCadastro alterado por completo!")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Digite um número válido para a opção.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("\n")

# Função para obter as opções de acessibilidade
def obter_acessibilidade(opcoes_acessibilidade):
    try:
        print("Opções de Acessibilidade:")
        for i, opcao in enumerate(opcoes_acessibilidade, 1):
            print(f"{i}. {opcao}")

        acessibilidade = []
        escolha_acessibilidade = int(input("Escolha a opção de acessibilidade (1-6) ou 0 para sair: "))

        while escolha_acessibilidade != 0:
            acessibilidade.append(opcoes_acessibilidade[escolha_acessibilidade - 1])
            escolha_acessibilidade = int(input("Você gostaria de adicionar outra acessibilidade? (1-6) ou 0 para sair: "))
            if escolha_acessibilidade < 0 or escolha_acessibilidade > 6:
                print("Opção inválida. Acessibilidade não configurada.")
                escolha_acessibilidade = int(input("Escolha uma opção de acessibilidade válida (1-6): "))

        return acessibilidade
    except ValueError:
        print("Digite um número válido para a opção.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para alterar as acessibilidades cadastradas
def alterar_acessibilidades():
    try:
        nome_usuario = input("Digite o Nome de Usuário para alterar as acessibilidades: ")

        # Consulta SQL para atualizar as acessibilidades de um usuário
        atualizacao = """UPDATE usuarios SET usuarios_acessibilidade = :acessibilidade WHERE usuarios_nome_usuario = :nome_usuario"""

        suporte_acessibilidade = input("Deseja suporte para acessibilidade? (Sim/Não): ")

        if suporte_acessibilidade.lower() == "sim":
            opcoes_acessibilidade = ["Daltonismo", "Idoso", "Mobilidade Reduzida", "Deficiente Visual", "Deficiente Auditivo", "Dislexia"]
            acessibilidade = obter_acessibilidade(opcoes_acessibilidade)
            acessibilidade_str = ', '.join(acessibilidade)  # Convertendo a lista em uma string separada por vírgulas
        else:
            acessibilidade_str = "Nenhuma"

        # Executar a atualização no banco de dados
        instrucao_SQL.execute(atualizacao, {'acessibilidade': acessibilidade_str, 'nome_usuario': nome_usuario})
        conect.commit()
        print("Acessibilidades alteradas com sucesso!\n")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para visualizar as acessibilidades de um usuário específico e exportar para JSON
def visualizar_acessibilidades():
    try:
        nome_usuario = input("Digite o Nome de Usuário para visualizar as acessibilidades: ")

        # Consulta SQL para selecionar as acessibilidades de um usuário
        selecao = """SELECT usuarios_acessibilidade FROM usuarios WHERE usuarios_nome_usuario = :nome_usuario"""

        # Executar a consulta no banco de dados
        instrucao_SQL.execute(selecao, {'nome_usuario': nome_usuario})
        dados = instrucao_SQL.fetchone()

        if dados:
            acessibilidades = dados[0]
            print(f"Acessibilidades de '{nome_usuario}': {acessibilidades}\n")

            # Exportar os dados para JSON
            exportar_json = input("Deseja exportar os dados para JSON? (s/n): ")
            if exportar_json.lower() == 's':
                with open(f"{nome_usuario}_acessibilidades.json", "w") as json_file:
                    json.dump({'nome_usuario': nome_usuario, 'acessibilidades': acessibilidades}, json_file, ensure_ascii=False, indent=4)
                print(f"Dados exportados para {nome_usuario}_acessibilidades.json")
        else:
            print(f"Usuário '{nome_usuario}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para visualizar usuários com tipos específicos de acessibilidades e exportar para JSON
def visualizar_usuarios_por_acessibilidade():
    try:
        print("Opções de Acessibilidade para Filtrar:")
        opcoes_acessibilidade = ["Daltonismo", "Idoso", "Mobilidade Reduzida", "Deficiente Visual", "Deficiente Auditivo", "Dislexia", "Nenhuma"]
        for i, opcao in enumerate(opcoes_acessibilidade, 1):
            print(f"{i}. {opcao}")

        escolha = int(input("Escolha a opção de acessibilidade para filtrar (1-7): "))
        if escolha < 1 or escolha > 7:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            return

        acessibilidade_escolhida = opcoes_acessibilidade[escolha - 1]

        if acessibilidade_escolhida == "Nenhuma":
            # Consulta SQL para selecionar usuários sem nenhuma acessibilidade
            selecao = """SELECT * FROM usuarios WHERE usuarios_acessibilidade = 'Nenhuma'"""
            instrucao_SQL.execute(selecao)
        else:
            # Consulta SQL para selecionar usuários com a acessibilidade escolhida
            selecao = """SELECT * FROM usuarios WHERE usuarios_acessibilidade LIKE :acessibilidade"""
            instrucao_SQL.execute(selecao, {'acessibilidade': f"%{acessibilidade_escolhida}%"})

        # Capturar todos os registros da consulta
        dados = instrucao_SQL.fetchall()
        lista_dados = sorted(dados)

        dados_df = pd.DataFrame.from_records(lista_dados, columns=['usuarios_nome_usuario', 'usuarios_senha', 'usuarios_nome_completo', 'usuarios_email', 'usuarios_acessibilidade'])

        if dados_df.empty:
            print(f"Não há registros para a acessibilidade '{acessibilidade_escolhida}'.")
        else:
            print(dados_df)
            print("\n")

            # Exportar os dados para JSON
            exportar_json = input("Deseja exportar os dados para JSON? (s/n): ")
            if exportar_json.lower() == 's':
                usuarios_list = dados_df.to_dict(orient='records')
                with open(f"usuarios_com_{acessibilidade_escolhida.lower()}.json", "w") as json_file:
                    json.dump(usuarios_list, json_file, ensure_ascii=False, indent=4)
                print(f"Dados exportados para usuarios_com_{acessibilidade_escolhida.lower()}.json")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("\n")

# Função para visualizar todos os usuários cadastrados e exportar para JSON
def visualizar_usuarios():
    try:
        lista_dados = []

        instrucao_SQL.execute("SELECT * FROM usuarios")

        # Capturar todos os registros da consulta
        dados = instrucao_SQL.fetchall()

        for dado in dados:
            lista_dados.append(dado)

        lista_dados = sorted(lista_dados)

        dados_df = pd.DataFrame.from_records(lista_dados, columns=['usuarios_nome_usuario', 'usuarios_senha', 'usuarios_nome_completo', 'usuarios_email', 'usuarios_acessibilidade'])

        if dados_df.empty:
            print("Não há registros na tabela de usuários")
        else:
            print(dados_df)
            print("\n")

            # Exportar os dados para JSON
            exportar_json = input("Deseja exportar os dados para JSON? (s/n): ")
            if exportar_json.lower() == 's':
                usuarios_list = dados_df.to_dict(orient='records')
                with open("usuarios_cadastrados.json", "w") as json_file:
                    json.dump(usuarios_list, json_file, ensure_ascii=False, indent=4)
                print("Dados exportados para usuarios_cadastrados.json")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("\n")

# Função para apagar um usuário cadastrado
def deletar_usuario():
    try:
        nome_usuario = input("Digite o Nome de Usuário a ser deletado: ")

        # Consulta SQL para deletar um usuário
        deletar = """DELETE FROM usuarios WHERE usuarios_nome_usuario = :nome_usuario"""

        # Executar a deleção no banco de dados
        instrucao_SQL.execute(deletar, {'nome_usuario': nome_usuario})
        conect.commit()
        print(f"Usuário '{nome_usuario}' deletado com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para realizar o login
def realizar_login():
    try:
        nome_usuario_login = input("Digite o Nome de Usuário: ")
        senha_login = input("Digite a sua senha: ")

        # Consulta SQL para realizar o login
        selecao = """SELECT usuarios_nome_completo, usuarios_acessibilidade FROM usuarios WHERE usuarios_nome_usuario = :nome_usuario AND usuarios_senha = :senha"""

        # Executar a consulta no banco de dados
        instrucao_SQL.execute(selecao, {'nome_usuario': nome_usuario_login, 'senha': senha_login})
        dados = instrucao_SQL.fetchone()

        if dados:
            print(f"\nBem-vindo, {dados[0]}!")
            if dados[1] != "Nenhuma":
                print(f"Suporte de acessibilidade: {dados[1]}\n")
        else:
            print("Nome de Usuário ou Senha incorretos. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Funções para integração no Front-End

# Função para o próprio usuário se cadastrar
def cadastro_usuario(nome_usuario, senha, nome_completo, email, acessibilidade_str):
    try:
        if acessibilidade_str.lower() == "nenhuma":
            acessibilidade = ["Nenhuma"]
        else:
            opcoes_acessibilidade = ["Daltonismo", "Idoso", "Mobilidade Reduzida", "Deficiente Visual",
                                     "Deficiente Auditivo", "Dislexia"]
            acessibilidade = acessibilidade_str.split(', ')

        # Converte a lista de acessibilidades em uma string separada por vírgula
        acessibilidade_str = ', '.join(acessibilidade)

        # Instrução PL/SQL:
        insercao = """DECLARE
                        acessibilidade_array VARCHAR2(1000) := :acessibilidade;
                    BEGIN
                        INSERT INTO usuarios (usuarios_nome_usuario, usuarios_senha, usuarios_nome_completo, usuarios_email, usuarios_acessibilidade) 
                        VALUES (:nome_usuario, :senha, :nome_completo, :email, acessibilidade_array);
                    END;"""

        instrucao_SQL.execute(insercao, {'nome_usuario': nome_usuario, 'senha': senha, 'nome_completo': nome_completo,
                                         'email': email, 'acessibilidade': acessibilidade_str})
        conect.commit()
        return "Dados gravados com sucesso!"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Função para realizar o login
def login_usuario(nome_usuario, senha):
    try:
        # Consulta SQL para realizar o login
        selecao = """SELECT usuarios_nome_completo FROM usuarios WHERE usuarios_nome_usuario = :nome_usuario AND usuarios_senha = :senha"""

        # Executar a consulta no banco de dados
        instrucao_SQL.execute(selecao, {'nome_usuario': nome_usuario, 'senha': senha})
        dados = instrucao_SQL.fetchone()

        if dados:
            return {'status': 'success', 'fullname': f'{dados[0]}'}
        else:
            return {'status': 'error', 'message': 'Nome de usuário ou senha incorretos. Tente novamente.'}

    except Exception as e:
        return {'status': 'error', 'message': f'Ocorreu um erro: {e}'}
