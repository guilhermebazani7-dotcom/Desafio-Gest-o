def utilidade(escolha, ws, wb):
    while True:
        if escolha == '1':
            while True:
                Valor_saida = int(input("Valor gasto: "))
                if Valor_saida <= 0:
                    print("Saída invalida")
                    continue
                break

            while True:
                cat = input("Que tipo de transação:")
                if cat == "":
                    print("Saída invalida")
                    continue
                break
            data = input("Data da transação:")

            ws.append([Valor_saida, data, cat])
            wb.save("GerenGast.xlsx")
            break

        elif escolha == '2':
            print("--------------------------------------------------")
            for linha in ws.iter_rows(min_row=2, values_only=True):
                Valor_saida, data, cat = linha
                print(f"No dia {data}, foi feito um gasto de {Valor_saida}, em {cat}")
                continue
            break

        elif escolha == '3':
            print("Salvando... Obrigado por utilizar")
            return "quebra"
            break

        else:
            print("Opção inválida, tente novamente.")

