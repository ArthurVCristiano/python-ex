cartas = [1,2,3,4,5,6,7]
descarte = "Descartados : "
baralho = len(cartas)

while baralho > 1:

    # descarta o topo
    descarte += str(cartas[0]) + " ; "
    cartas.remove(cartas[0])

    # move o novo topo pro final
    cartas.append(cartas[0])
    cartas.remove(cartas[0])

    baralho = len(cartas)

print(descarte)
print(cartas)