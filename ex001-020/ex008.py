medida = float(input('Informe uma distância em metros: '))
print(f'A medida de {medida} corresponde a:')
print(f'{medida/1000}km \n{medida/100}hm \n{medida/10}dam \n{medida/0.1 :.0f}dm \n{medida/0.01 :.0f}cm \n{medida/0.001 :.0f}mm')