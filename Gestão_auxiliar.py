def utilidade(escolha):
    if escolha == '1':
        Valor_saida = input("Valor gasto: ")
        data = input("Data da transação:")
        cat = input("Que tipo de transação:")
        ws.append([Valor_saida, data, cat])
        wb.save("GerenGast.xlsx")

    elif escolha == '2':
        print("--------------------------------------------------")
        for linha in ws.iter_rows(min_row=2, values_only=True):
            Valor_saida, data, cat = linha
            print(f"No dia {data}, foi feito um gasto de {Valor_saida}, em {cat}")
            continue

    elif escolha == '3':
        print("Salvando... Obrigado por utilizar")
        break

    else:
        print("Opção inválida, tente novamente.")