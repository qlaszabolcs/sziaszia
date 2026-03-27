def max_keres(lista, i=0):
    if i == len(lista) - 1:
        return lista[i]

    m = max_keres(lista, i + 1)

    if lista[i] > m:
        return lista[i]
    else:
        return m


lista = list(map(int, input("Adj meg szamokat szokozzel elvalasztva: ").split()))
print(max_keres(lista))