nomes = [
    {"cadeira": "João", "mesa": "Luis", "porta": "Marcos"},
    {"tv": "Ana", "colher": "Carla", "janela": "Pedro"},
]


def mostrar_nomes(obj):
    lista_nomes = []
    for item in obj:
       for valor in item.values():
        lista_nomes.append(valor)
    return lista_nomes

nomes_extraidos = mostrar_nomes(nomes)
print(nomes_extraidos)