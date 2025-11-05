salario = float(input("Qual é o salário do funcionário? R$"))
if salario > 1250:
    print(f'Quem ganhava {salario} passa a ganhar R${salario * 1.1 :.2f} agora.')
else:
    print(f'Quem ganhaga {salario} passa a ganhar R${salario * 1.15 :.2f} agora')