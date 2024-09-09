menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
=>'''

SAQUE_MAX = 500
NUM_SAQUES_MAX = 3

saldo = 0
extrato = ""
numero_saques = 0

while True:
    
    operacao = input(menu)
    
    if operacao == "d": #Depositar
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${round(valor_deposito, 2)}\n"
        else:
            print("Erro: O valor não é um depósito válido")
    
    if operacao == "s": #Saque
        valor_saque = float(input("Informe o valor do saque: "))
        
        if valor_saque > 0:
            
            if valor_saque > saldo:
                print(f"Erro: O valor do saque é maior do que seu valor em conta (R$ {round(saldo, 2)})")                
            elif valor_saque > SAQUE_MAX:
                print(f"Erro: O valor do saque é maior do que o máximo permitido pela operação (R$ {round(SAQUE_MAX, 2)})")                
            elif numero_saques >= NUM_SAQUES_MAX:
                print(f"Erro: Você já realizou seus {NUM_SAQUES_MAX} diários, tente novamente amanhã")                
            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque de R$ {round(valor_saque, 2)}\n"
        else:
            print("Erro: Valor do saque não é válido.")
    
    if operacao == "e": #Imprimir extrato
        print("-------------------------")
        print("\n \t EXTRATO")
        print("Nenhuma operação realizada." if not extrato else extrato)
        print(f"\n    Saldo: R$ {round(saldo, 2)}")
        print("-------------------------")        
    
    if operacao == "q":
        break

