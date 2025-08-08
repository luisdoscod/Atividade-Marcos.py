def numeros_repetidos(lista):
    numeros_unicos = []
    for numero in lista:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)
    return numeros_unicos
lista = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
lista_sem_repetidos = numeros_repetidos(lista)
print(lista_sem_repetidos)