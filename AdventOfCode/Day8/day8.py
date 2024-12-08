import copy



if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:
        alto = 0
        ancho = 0
        mapa = []
        dict_posiciones = {

        }
        for y, linea in enumerate(archivo):
            alto += 1
            fila = []
            for x, valor in enumerate((linea.rstrip())):
                # print(valor)
                ancho = len(linea.rstrip())
                fila.append(valor)
                if valor.islower() or valor.isupper() or valor.isdigit():
                    if valor not in dict_posiciones:
                        dict_posiciones[valor] = []
                    dict_posiciones[valor].append([x, y])
            mapa.append(fila)

        diccionario_copia_inmutable = copy.deepcopy(dict_posiciones)
        # usamos set para evitar guardar duplicados
        antinodos = set()
        antinodos2 = set()
        for frequency in dict_posiciones.values():
            while len(frequency) > 0:
                posicion = frequency.pop(0)
                for i in range(len(frequency)):
                    distancia_between_x = posicion[0] - frequency[i][0]
                    distancia_between_y = posicion[1] - frequency[i][1]

                    diagonal = [posicion[0] + ( distancia_between_x ),
                                posicion[1] + ( distancia_between_y )]
                    diagonal_inversa = [frequency[i][0] - (distancia_between_x),
                                        frequency[i][1] - (distancia_between_y)]

                    if 0 <= diagonal[0] < ancho and 0 <= diagonal[1] < alto :
                        mapa[diagonal[1]][diagonal[0]] = "#"
                        antinodos.add((diagonal[0],diagonal[1]))
                        antinodos2.add((diagonal[0], diagonal[1]))
                        x2 = diagonal[0] + distancia_between_x
                        y2 = diagonal[1] + distancia_between_y
                        while 0 <= x2 < ancho and 0 <= y2 < alto:
                            antinodos2.add((x2,y2))
                            mapa[y2][x2] = "#"
                            x2 += distancia_between_x
                            y2 += distancia_between_y



                    if 0 <= diagonal_inversa[0] < ancho and 0 <= diagonal_inversa[1] < alto:
                        mapa[diagonal_inversa[1]][diagonal_inversa[0]] = "#"
                        antinodos.add((diagonal_inversa[0], diagonal_inversa[1]))
                        antinodos2.add((diagonal_inversa[0], diagonal_inversa[1]))
                        x2 = diagonal_inversa[0] - distancia_between_x
                        y2 = diagonal_inversa[1] - distancia_between_y
                        while 0 <= x2 < ancho and 0 <= y2 < alto:
                            antinodos2.add((x2, y2))
                            mapa[y2][x2] = "#"
                            x2 -= distancia_between_x
                            y2 -= distancia_between_y


        for fila in mapa:
            print("".join(map(str, fila)))
        print("Ejercicio1  ", len(antinodos))
        print("Ejercicio2  ", len(antinodos2))
