#desconto em desconto

preco = float(input('Digite o preço do produto'))
desconto = float(input('Dê o percentual de desconto:'))
desconto = desconto / 100

precoComDesconto = preco - (preco * desconto)

print(f'O preço do produto com desconto é de: {precoComDesconto}')