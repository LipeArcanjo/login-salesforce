'''
                integrantes:
    ----------------------------------
    |felipe arcanjo    - rm = 554018 |
    |fernanddo gabriel - rm = 554137 |
    |gabriel de matos  - rm = 553889 |
    ----------------------------------

    criaremos um menu de login com as opções de: 1. cadastra-se | 2. login.| esse menu deverá solicitar o: nome de usuário, senha, nome completo e endereço de e-mail. gostaria também que ao final do cadastro, o programa pergunte se o usuário gostaria de ter algum suporte para acessibilidade, if "sim", mostrar uma lista de opções de acessibilidade contendo:  daltonismo, idoso, mobilidade reduzida, deficiente visual, deficiente auditivo e disléxo.
'''

# Imporatando funções necessárias para execução do código.
from login import exibir_menu,cadastrar_usuario,realizar_login,alterar_acessibilidades,visualizar_acessibilidades

# Programa principal
while True:
    exibir_menu()
    escolha = input("Escolha a opção (1/2/3/4): ")

    if escolha == "1":
        cadastrar_usuario()
    elif escolha == "2":
        realizar_login()
    elif escolha == "3":
        alterar_acessibilidades()
    elif escolha == "4":
        visualizar_acessibilidades()
    else:
        print("Opção inválida. Escolha 1 para cadastrar-se, 2 para login, 3 para alterar acessibilidades ou 4 para visualizar acessibilidades.")