from collections import deque

direcciones = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # (x,y)

def calculo_ruta(_map):
    queue = deque()
    start = (len(_map) - 2, 1, (0, 1), 0)  # x, y, direccion, score
    _map[len(_map) - 2][1] = 0 # donde esta la S le ponemos el primer valor a 0 para ir completando el mapa
    queue.append(start)

    while queue:
        current = queue.popleft()
        x_actual = current[0]
        y_actual = current[1]
        direccion_actual = current[2]
        puntuacion_actual = current[3]

        direciones_puntuacion = [
            (direccion_actual, puntuacion_actual + 1),
            (izquierda(direccion_actual), puntuacion_actual + 1001),
            (derecha(direccion_actual), puntuacion_actual + 1001)
        ]

        for direccion, puntuacion in direciones_puntuacion:
            x, y = x_actual + direccion[0], y_actual + direccion[1]
            if _map[x][y] == "#":
                continue

            if _map[x][y] in [".", "E"] or (isinstance(_map[x][y], int) and _map[x][y] > puntuacion):
                _map[x][y] = puntuacion
                queue.append((x, y, direccion, puntuacion))

    return _map[1][len(_map[1]) - 2] # Si llega al final sale del while porque no tiene ya ningun valor al entrar en el
                                        # for y devolvemos la suma que se fue haciendo anteriormente

def derecha(direccion_actual):
    return direcciones[(direcciones.index(direccion_actual) + 1 + len(direcciones)) % len(direcciones)]


def izquierda(cur_dir):
    return direcciones[(direcciones.index(cur_dir) - 1 + len(direcciones)) % len(direcciones)]




if __name__ == "__main__":

    with open("input.txt", 'r') as file:
        _map = [list(line.strip()) for line in file if line.strip()]
        resultado = calculo_ruta(_map)
        print(resultado)


