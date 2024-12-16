



def parte_uno(valor):
    """Resuelve una región conectada con el mismo valor y encuentra su perímetro."""
    key = kaart[valor]  # Valor de la celda inicial
    queue = [valor]  # Cola para recorrer la región
    perimeter = set()  # Celdas que forman el perímetro
    visited = set()  # Celdas visitadas en esta función

    for row, col in queue:
        visited.add((row, col))

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Si la celda vecina está dentro del mapa y tiene el mismo valor
            if (new_row, new_col) in kaart and (new_row, new_col) not in visited and kaart[
                (new_row, new_col)] == key:
                seen.add((new_row, new_col))
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))
            else:
                # Agregar al perímetro si no es una celda de la región
                if (new_row, new_col) in visited:
                    continue
                perimeter.add((new_row, new_col, dr, dc))

    return queue, perimeter


def encontrar_perimetro(celdas_perimetro):
    """Cuenta el número de segmentos únicos en el perímetro."""
    visited = set()
    perimeter_count = 0

    for cell in celdas_perimetro:
        if cell in visited:
            continue

        perimeter_count += 1
        row, col, ddr, ddc = cell
        queue = [(row, col)]
        visited.add((row, col, ddr, ddc))

        for r, c in queue:
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc

                if (new_row, new_col, ddr, ddc) in celdas_perimetro and (
                new_row, new_col, ddr, ddc) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col, ddr, ddc))

    return perimeter_count


if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:

        # Inicializar el mapa como un diccionario
        kaart = {}
        for row_index, line in enumerate(archivo):
            for col_index, value in enumerate(line.strip()):
                kaart[(row_index, col_index)] = value

        # Conjunto para rastrear las celdas ya visitadas
        seen = set()

        # Direcciones para moverse en 4 direcciones (arriba, abajo, izquierda, derecha)
        directions = ((1, 0), (-1, 0), (0, -1), (0, 1))

        # Inicializar los contadores de los resultados
        part1 = 0
        part2 = 0

        # Iterar sobre cada celda del mapa
        for position in kaart:
            row, col = position
            if (row, col) in seen:
                continue

            # Resolver la región y su perímetro
            region, perimeter = parte_uno((row, col))
            part1 += len(region) * len(perimeter)

            # Calcular el número de cercas en el perímetro
            fences = encontrar_perimetro(perimeter)
            part2 += len(region) * fences

        # Imprimir los resultados
        print(part1)
        print(part2)







