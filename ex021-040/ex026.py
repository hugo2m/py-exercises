frase = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vez(es) na frase. ')
print(f'A primeira letra "A" apareceu na posição {frase.find("A")+1}')
print(f'A última letra "A" apareceu na posição {frase.rfind("A")+1}')