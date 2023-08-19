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
        valor = float(input("Valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Valor de R${valor} depositado com sucesso.") 

        else:
            print("Por favor informe um valor válido.")

    elif opcao == "s":
        valor = float(input("Valor a ser sacado:"))
    
        sem_saldo = valor > saldo
    
        sem_limite = valor > limite

        sem_saques = numero_saques >= LIMITE_SAQUES

        if sem_saldo:
            print("Operação Falhou. Não possui saldo suficiente.")

        elif sem_limite:
            print("Operação Falhou. O valor excede o limite.")

        elif sem_saques:
            print("Operação Falhou. Número de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R${valor} realizado com sucesso. Retire seu dinheiro.")

        else:
            print("Operação Falhou. Valor inválido.")
       
    elif opcao == "e":
        print("----Extrato----")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("---------------")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema.")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")