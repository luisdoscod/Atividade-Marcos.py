def contar_ocorrencias(lista, numero):
    contador = 0
    for item in lista:
        if item == numero:
            contador += 1
    return contador

lista = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
numero = 13
resultado = contar_ocorrencias(lista, numero)
print(f"O numero {numero} aparece {resultado} vezes na lista.")