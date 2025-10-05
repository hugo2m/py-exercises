from math import sqrt
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = sqrt (oposto**2 + adjacente**2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')