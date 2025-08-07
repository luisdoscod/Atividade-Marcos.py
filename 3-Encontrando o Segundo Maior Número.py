def segundor_maior(lista_numeros):
    maior = lista_numeros[0]
    segundo = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior:
            segundo = maior
            maior = numero
        elif numero > segundo and numero != maior:
            segundo = numero

    return segundo

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5,    1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
print(f'o segundo maior número é: {segundor_maior(numeros)}')