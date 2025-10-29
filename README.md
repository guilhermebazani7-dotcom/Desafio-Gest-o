# Desafio-Gest-o
💰 Gerenciador Financeiro em Python

Um simples e funcional gerenciador financeiro desenvolvido em Python, utilizando a biblioteca openpyxl para manipulação de planilhas Excel.
O objetivo do projeto é permitir o registro, visualização e organização de gastos de forma automatizada e prática.

📂 Estrutura do Projeto

O projeto está dividido em dois arquivos principais:

Gestão_auxiliar.py → Responsável pelo funcionamento interno do editor Excel (criação, leitura e gravação dos dados financeiros).

Gestão_principal.py → Responsável pela interface de entrada do usuário, capturando as informações e acionando as funções do módulo auxiliar.

⚙️ Funcionalidades

✅ Registrar gastos:
Permite inserir novos gastos em uma tabela Excel com as seguintes colunas:

Descrição

Valor

Data

Tipo (categoria do gasto)

✅ Visualizar registros:
Exibe todos os gastos já cadastrados com suas respectivas classificações.

✅ Salvar e encerrar:
Após o registro dos dados, o programa salva automaticamente as alterações na planilha e pode ser encerrado com segurança.

🧩 Tecnologias Utilizadas

Python 3.x

openpyxl — para manipulação de planilhas Excel
