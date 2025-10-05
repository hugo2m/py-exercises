# Carro custa R$ 60.00 por dia e 0.15 por km rodado
dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
print(f'O total a pagar é de R$:{dias*60 + km*0.15:.2f}')