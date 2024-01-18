def menor_distancia(lista1, lista2):
    menor_dist = float('inf')

    for elem1 in lista1:
        for elem2 in lista2:
            distancia = abs(elem1 - elem2)
            if distancia < menor_dist:
                menor_dist = distancia

    return menor_dist

lista1 = [120, 200, 23, 12, 90, 25, 37, 35, 551, 45]
lista2 = [260, 600, 100, 150, 180, 285, 327, 389, 2, 50]


resultado = menor_distancia(lista1, lista2)

print(f"A menor distância entre as listas é: {resultado}")
