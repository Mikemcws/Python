import requests

# Passo 1: Pegar o valor do Dólar agora de uma API gratuita
url = "https://economia.awesomeapi.com.br/last/USD-BRL"
resposta = requests.get(url)
dados = resposta.json()

# Passo 2: Extrair apenas o valor numérico (o preço de venda)
cotacao_dolar = float(dados['USDBRL']['bid'])

print("=== CONVERSOR EM TEMPO REAL ===")
print(f"Cotação atual do Dólar: R$ {cotacao_dolar:.2f}")

# Passo 3: Lógica que você já conhece (input e cálculo)
reais = float(input("Quanto você tem na carteira? R$ "))
dolares = reais / cotacao_dolar

print("-" * 30)
print(f"Com R$ {reais:.2f} você pode comprar US$ {dolares:.2f}")
print("-" * 30)
