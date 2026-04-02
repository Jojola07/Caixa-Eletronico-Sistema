# SISTEMA DE CAIXA ELETRONICO
import datetime, os, time

arquivoSaldo = 'saldo.txt'

def carregar_saldo():
    if not arquivoSaldo in os.listdir():
        with open(arquivoSaldo, 'w') as f:
            f.write('0')
    else:
        with open(arquivoSaldo, 'r') as f:
            return float(f.read())

def salvar_transacao(tipo, valor):
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

def mostrar_historico():
    if 'historico.txt' in os.listdir():
        with open('historico.txt', 'r') as f:
            print("Carregando histórico de transações...")
            time.sleep(1)
            print("\n=== HISTÓRICO DE TRANSAÇÕES ===")
            print(f.read())
    else:
        print("Nenhuma transação realizada ainda.")

def menu():
    while True:
        print("\n=== CAIXA ELETRÔNICO ===")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Ver histórico de transações")
        print("5. Sair")
        time.sleep(1)
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            saldo = carregar_saldo()
            print("Carregando saldo...")
            time.sleep(1)
            print("\n=== SALDO ATUAL ===")
            print(f"Saldo atual: R${saldo:.2f}")
            time.sleep(1)
        elif escolha == '2':
            valor = float(input("Digite o valor a depositar: "))
            salvar_transacao('deposito', valor)
            print("Depósito realizado com sucesso!")
            time.sleep(1)
        elif escolha == '3':
            valor = float(input("Digite o valor a sacar: "))
            print("Verificando saldo...")
            time.sleep(1)
            saldo_atual = carregar_saldo()
            if valor > saldo_atual:
                print("Saldo insuficiente!")
                time.sleep(1)
            else:
                salvar_transacao('saque', valor)
                print("Saque realizado com sucesso!")
                time.sleep(1)
        elif escolha == '4':
            mostrar_historico()
            time.sleep(1)
        elif escolha == '5':
            print("Obrigado por usar o caixa eletrônico!")
            time.sleep(1)
            break
        else:
            print("Opção inválida, tente novamente.")

menu()