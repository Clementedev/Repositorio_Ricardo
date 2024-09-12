menu = """Selecione a opção desejada:

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

"""
saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
extrato = ""

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        deposito = float(input("Digite o valor:\n"))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito feito no valor de: {deposito:.2f}\n"
            print("Deposito feito com sucesso!")
        else:
            print("Falha! Digite um valor válido!")
    
    elif opcao == "2":
        saque = float(input("Digite o valor que deseja sacar:"))
        
        if saque <= saldo:
            if saque <= 500:
                if numero_saques < limite_saques:
                    numero_saques += 1
                    saldo -= saque
                    extrato += f"Saque feito no valor de: {saque:.2f}\n"
                    print("Saque efetuado com sucesso!")
                else:
                    print("Você atingiu o número de saques diários!")
            else:
                print("Você atingiu o valor limite para saque!")
        else:
            print("Você não tem saldo suficiente!")
    elif opcao == "3":
        print("######### EXTRATO BANCÁRIO######### \n")
        print(f"{extrato}\n")
        print(f"Seu saldo atual em conta é: {saldo:.2f}\n")
    
    elif opcao == "4":
        break
    
    else:
        print("Opção inválida. Tente novamente!")