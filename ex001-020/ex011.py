# Cada litro de tinta pode pintar uma área de 2 metros quadrados.
largura = float (input('Largura da parede: '))
altura = float (input('Altura da parede: '))

print(f'Sua parede te a dimensão de {largura} x {altura} e sua área é de {largura*altura :.2f}m².')
print(f'Para pintar essa parede, você precisará de {largura*altura/2 :.2f} litros de tinta.')