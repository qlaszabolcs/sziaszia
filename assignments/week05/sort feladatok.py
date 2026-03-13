def bubble_sort(szamok):

    for i in range(len(szamok)):
        for j in range(len(szamok)-1):
          if szamok[j] > szamok[j+1]:
              szamok[j], szamok[j+1] = szamok[j+1], szamok[j]

    print(szamok)


szamok= [9 , 4 , 6 , 91]
bubble_sort(szamok)

def selection_sort(numbers):

    length = len(numbers)

    for i in range(length):
        smallest = i

        for j in range(i + 1, length):
            if numbers[j] < numbers[smallest]:
                smallest = j

        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

    print(numbers)

numbers= [22, 91 ,14 , 46]
selection_sort(numbers)

def insertion_sort(lista):

    for index in range(1, len(lista)):
        aktualis = lista[index]
        pozicio = index - 1

        while pozicio >= 0 and lista[pozicio] > aktualis:
            lista[pozicio + 1] = lista[pozicio]
            pozicio -= 1

        lista[pozicio + 1] = aktualis

    print(lista)

lista= [12, 82 , 45 , 94]
insertion_sort(lista)