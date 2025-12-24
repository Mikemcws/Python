import requests

# 1. Busca a cotação real (como você já aprendeu)
url = "https://economia.awesomeapi.com.br/last/USD-BRL"
dados = requests.get(url).json()
cotacao = float(dados['USDBRL']['bid'])

print(f"--- DÓLAR AGORA: R$ {cotacao:.2f} ---")

# 2. O seu critério de "grana"
preco_limite = float(input("Até quanto você aceita pagar pelo Dólar? R$ "))

# 3. A Lógica de Decisão (O coração do projeto)
if cotacao <= preco_limite:
    print("\n✅ OPORTUNIDADE: O preço está abaixo do seu limite!")
    print(f"Compre agora! Você está economizando R$ {preco_limite - cotacao:.2f} por dólar.")
else:
    print("\n❌ CILADA: O preço está muito alto!")
    print(f"Aguarde. O dólar está R$ {cotacao - preco_limite:.2f} acima do que você quer pagar.")