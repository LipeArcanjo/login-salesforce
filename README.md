# Projeto de login da AcessoTotal - Salesforce

## Integrantes do Projeto

- Felipe Arcanjo (RM: 554018)
- Gustavo Vieira (RM: 553471)
- Gabriel de Matos (RM: 553889)

Este é um programa de login desenvolvido em Python com integração ao banco de dados Oracle e uma API Flask para interação com o front-end.

## Funcionalidades Principais

1. **Cadastro de Usuário**: Permite que novos usuários se cadastrem fornecendo nome de usuário, senha, nome completo, endereço de e-mail e opções de acessibilidade.

2. **Login**: Usuários podem fazer login com seu nome de usuário e senha.

3. **Alteração de Cadastro**: Usuários podem alterar informações específicas de seu cadastro, como senha, nome completo e endereço de e-mail.

4. **Alteração de Acessibilidades Cadastradas**: Usuários podem alterar as acessibilidades que foram cadastradas durante o registro.

5. **Visualização de Acessibilidades Cadastradas**: Usuários podem visualizar as acessibilidades que estão cadastradas em sua conta.

6. **Exclusão de Usuário**: Usuários podem excluir sua própria conta do sistema.

7. **Visualização de Usuários Cadastrados**: Administradores ou usuários com permissão podem visualizar todos os usuários cadastrados no sistema.

8. **Visualização de Usuários por Acessibilidade**: Permite visualizar usuários cadastrados com tipos específicos de acessibilidades.

## Utilização

Para executar o programa, siga estas etapas:

1. Certifique-se de ter o Python instalado em seu ambiente.
2. Instale os requisitos do projeto executando `pip install {nome da biblioteca}`.
3. Execute o arquivo `main.py` no seu ambiente Python.
4. O programa apresentará um menu com opções numeradas que correspondem às funcionalidades mencionadas acima.

## Observações

- O banco de dados Oracle é utilizado para armazenar os dados dos usuários.
- A API Flask fornece endpoints para integração com o front-end, permitindo o registro e login de usuários.
- As opções de acessibilidade disponíveis incluem Daltonismo, Idoso, Mobilidade Reduzida, Deficiente Visual, Deficiente Auditivo e Dislexia.
