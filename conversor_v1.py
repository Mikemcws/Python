import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
dados = requests.get(url).json()
cotacao = float(dados['USDBRL']['bid'])

print(f"--- DÓLAR AGORA: R$ {cotacao:.2f} ---")


preco_limite = float(input("Até quanto você aceita pagar pelo Dólar? R$ "))


if cotacao <= preco_limite:
    print("\n✅ OPORTUNIDADE: O preço está abaixo do seu limite!")
    print(f"Compre agora! Você está economizando R$ {preco_limite - cotacao:.2f} por dólar.")
else:
    print("\n❌ CILADA: O preço está muito alto!")
    print(f"Aguarde. O dólar está R$ {cotacao - preco_limite:.2f} acima do que você quer pagar.")
