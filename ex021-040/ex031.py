distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    print(f'O preço da passagem para esta viagem é de R${(distancia*0.5):.2f}')
else:
    print(f'O preço da passagem para esta viagem é de R${(distancia*0.45):.2f}')