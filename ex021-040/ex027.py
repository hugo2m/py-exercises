nome = str(input('Digite o nome completo: ')).strip()
aux = nome.split()
print(f'Seu primeiro nome é {aux[0]}')
print(f'Seu último nome é {aux[len(aux)-1]}')