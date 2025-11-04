valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

#Organizando o maior número:
maior = valor1
if valor2 >= maior and valor2 >= valor3:
    maior = valor2
if valor3 >= maior and valor3 >= valor2:
    maior = valor3

#Organizando o menor número:
menor = valor1
if valor2 <= menor and valor2 <= valor3:
    menor = valor2
if valor3 <= menor and valor2 <= valor2:
    menor = valor3
#Prints:
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')