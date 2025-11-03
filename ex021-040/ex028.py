from random import randint
num = randint(0,5)
usuario = int(input('Digite um número entre 0 e 5: '))
if usuario == num:
    print('Parabens" Você acertou!')
else:
    print(f'Você errou! O número era {num}')