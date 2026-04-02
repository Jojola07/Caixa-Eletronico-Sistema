# SISTEMA DE CAIXA ELETRONICO
import datetime, os

arquivoSaldo = 'saldo.txt'

def carregar_saldo()
    if not arquivoSaldo in os.listdir():
        with open(arquivoSaldo, 'w') as f:
            f.write('0')
    else:
        with open(arquivoSaldo, 'r') as f:
            return float(f.read())

def salvar_transacao(tipo, valor)
    with open(arquivoSaldo, 'r') as f:
        saldo_atual = float(f.read())
    
    if tipo == 'deposito':
        saldo_atual += valor
    elif tipo == 'saque':
        saldo_atual -= valor
    
    with open(arquivoSaldo, 'w') as f:
        f.write(str(saldo_atual))
    
    with open('historico.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()}: {tipo} de R${valor:.2f}\n")

def menu()
    while True:
        print("\n=== CAIXA ELETRÔNICO ===")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            saldo = carregar_saldo()
            print(f"Saldo atual: R${saldo:.2f}")
        elif escolha == '2':
            valor = float(input("Digite o valor a depositar: "))
            salvar_transacao('deposito', valor)
            print("Depósito realizado com sucesso!")
        elif escolha == '3':
            valor = float(input("Digite o valor a sacar: "))
            saldo_atual = carregar_saldo()
            if valor > saldo_atual:
                print("Saldo insuficiente!")
            else:
                salvar_transacao('saque', valor)
                print("Saque realizado com sucesso!")
        elif escolha == '4':
            print("Obrigado por usar o caixa eletrônico!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()