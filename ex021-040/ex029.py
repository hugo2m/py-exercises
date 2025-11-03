km = int(input('Qual é a velocidade atual do carro? '))
if km > 80:
    print('Você está acima do limite de velocidade e foi multado!')
    multa = (km - 80)*7
    print(f'Você deve pagar uma multa de: {multa :.2f} reais!')
print('Você está dentro do limite, tenha um bom dia! Dirija com segurança!')