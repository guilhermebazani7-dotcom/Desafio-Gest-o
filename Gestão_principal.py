from Gestão_auxiliar import utilidade
from openpyxl import Workbook

wb = Workbook()            #cria o arquivo excel
ws = wb.active             #ativa
ws.title = "Gerenciador de Gastos Pessoal"

ws = wb.active
ws.append(["Saída", "Data", "Categoria"])

wb.save("GerenGast.xlsx")

while True:
    print("Menu:")
    print("1. Adicionar gastos")
    print("2. Listar gastos")
    print("3. Salvar e encerrar")
    escolha = input("Escolha uma opção: ")
    resultado = utilidade(escolha)
    if resultado == "quebra":
        break


