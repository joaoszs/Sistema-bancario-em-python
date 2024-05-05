menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacao mal sucedida! Voce nao possui saldo suficiente.")

        elif excedeu_limite:
            print("Operacao mal sucedida! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operacao mal sucedida! O limite de saques foi atingido .")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de: R$ {valor:.2f} efetuado com sucesso !\n"
            numero_saques += 1

        else:
            print("Operacao mal sucedida! Informe um valor valido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Nao foi realizada movimentacoes na conta !" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Opcao invalida! por favor selecione uma opcao valida.")