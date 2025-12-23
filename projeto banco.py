print("=== BANCO PYTHON ===")
nome = input("Digite seu nome: ")
saldo = float(input(f"Olá {nome}, qual seu saldo atual? R$ "))

deposito = float(input("Quanto você deseja depositar? R$ "))
saldo_final = saldo + deposito

print("-" * 20)
print(f"Relatório Bancário")
print(f"Usuário: {nome}")
print(f"Saldo anterior: R$ {saldo:.2f}")
print(f"Novo saldo: R$ {saldo_final:.2f}")
print("-" * 20)
