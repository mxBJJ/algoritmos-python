from random import randint


def parOuImpar(lista):
    lista_teste = []
    for item in lista:
        if item % 2 == 0:
            lista_teste.append(True)
        else:
            lista_teste.append(False)

    return lista_teste


lista_gerada = [randint(0, 100) for x in range(randint(10, 100))]
print("="*110)
print(lista_gerada)
print("="*110)
print("\n"*3)
print("="*110)
print(parOuImpar(lista_gerada))
print("="*110)
