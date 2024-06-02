menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
extrato = ""
saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Não há saldo suficiente.")
        elif excedeu_limite:
            print("O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Número de saques diário atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor informado é inválido.")

    elif opcao == "e":
        print("\nExtrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")

    elif opcao == "q":
        break
    else:
        print("Opção inválida, por favor selecione novamente.")
