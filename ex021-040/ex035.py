a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print(f'Os segmenos acima PODEM FORMAR triângulo')
else:
    print(f'Os segmenos acima NÃO PODEM FORMAR triângulo')