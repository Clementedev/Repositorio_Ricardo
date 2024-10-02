
import textwrap

def menu():
    menu = """Selecione a opção desejada:
    [1] DEPOSITAR
    [2] SACAR
    [3] EXTRATO
    [4] NOVO USUÁRIO
    [5] CRIAR CONTA
    [6] SAIR
    """
    return input(menu)

def depositar(saldo, extrato, deposito, /):
    if deposito > 0:
            saldo += deposito
            extrato += f"Depósito feito no valor de: {deposito:.2f}\n"
            print("Deposito feito com sucesso!")
    else:
            print("Falha! Digite um valor válido!")
    return saldo, extrato

def sacar(*, saque, saldo, numero_saques, extrato, limite_saques, limite):
    if saque <= saldo:
        if saque <= limite:
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
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("######### EXTRATO BANCÁRIO######### \n")
    print(f"{extrato}\n")
    print(f"Seu saldo atual em conta é: {saldo:.2f}\n")

def criar_usuario(usuarios):
    cpf = input("Digité o número do seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nJá existe usuário com esse CPF")
        return
    nome = input("\nInforme seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-m-aaaa): ")         
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/uf:) ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario não encontrado, fluxo de criação de conta encerrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
           
def dashboard():
    saldo = 0
    limite = 500
    numero_saques = 0
    limite_saques = 3
    extrato = ""
    usuarios =[]
    contas = []
    AGENCIA = "0001"

    while True:
        
        opcao = menu()
    
        if opcao == "1":
            deposito = float(input("Digite o valor:\n"))
            saldo, extrato = depositar(saldo, extrato, deposito)
    
        elif opcao == "2":
            saque = float(input("Digite o valor que deseja sacar:"))
            saldo, extrato = sacar(saldo=saldo, saque=saque, numero_saques=numero_saques, limite_saques=limite_saques, limite=limite, extrato=extrato)
                
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao == "4":
            criar_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            break
        
        else:
            print("Opção inválida. Tente novamente!")
            
dashboard()