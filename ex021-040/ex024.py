cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == "SANTO")
# O método split() divide a string em uma lista de palavras, removendo espaços extras.
# O método upper() converte a string para maiúsculas.
# A comparação é feita com "SANTO" em maiúsculas para garantir que a verificação seja case-insensitive.