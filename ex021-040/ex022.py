nome = input('Digite seu nome completo: ')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome tem ao todo (sem espaços): {len(nome) - nome.count(" ")} letras.')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')


