def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista) #sum é a funcao que soma os elementos e o len conta quantos elementos tem a lista

lista =  [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
media = calcular_media(lista)
print(f"A média dos números na lista é: {media:.2f}")