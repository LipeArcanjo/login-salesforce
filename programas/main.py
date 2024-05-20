'''
                integrantes:
    ----------------------------------
    |felipe arcanjo    - rm = 554018 |
    |gustavo vieira    - rm = 553471 |
    |gabriel de matos  - rm = 553889 |
    ----------------------------------

    criaremos um menu de login com as opções de: 1. cadastra-se | 2. login.| esse menu deverá solicitar o: nome de usuário, senha, nome completo e endereço de e-mail. gostaria também que ao final do cadastro, o programa pergunte se o usuário gostaria de ter algum suporte para acessibilidade, if "sim", mostrar uma lista de opções de acessibilidade contendo:  daltonismo, idoso, mobilidade reduzida, deficiente visual, deficiente auditivo e disléxo.
'''

# Importando funções necessárias para execução do código.
from login import *

# Programa principal
while conexao:
    try:
        opc = int(input("Escolha a opção: 1 - Acessar o menu | 2 - Sair : "))

        if opc == 1:
            exibir_menu()
            escolha = int(input("Escolha a opção de usuário: "))
            match escolha:
                case 1:
                    cadastrar_usuario()
                case 2:
                    realizar_login()
                case 3:
                    alterar_cadastro()
                case 4:
                    alterar_acessibilidades()
                case 5:
                    visualizar_acessibilidades()
                case 6:
                    deletar_usuario()
                case 7:
                    visualizar_usuarios()
                case 8:
                    visualizar_usuarios_por_acessibilidade()
                case _:
                    print("Opção inválida. Escolha entre 1 e 8.")
        elif opc == 2:
            conexao = False
        else:
            print("Opção inválida. Escolha 1 para o menu de usuário ou 2 para sair.")
    except ValueError:
        print("Por favor, insira um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        print("\n")

print("Até mais!")
