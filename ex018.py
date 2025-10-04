from math import sin, cos, tan, radians
graus = float(input('Digite um ângulo qualquer: '))
radianos = radians(graus)
print(f'O ângulo de {graus} tem o SENO de {sin(radianos):.2f}')
print(f'O ângulo de {graus} tem o COSSENO de {cos(radianos):.2f}')
print(f'O ângulo de {graus} tem o TANGENTE de {tan(radianos):.2f}')