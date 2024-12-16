
def partir_por_la_mitad(valor):
    longitud = len(valor)
    mitad = longitud // 2  # División entera para obtener la posición del medio
    return valor[:mitad], valor[mitad:]


if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:

        saltos = 75
        array = []
        for linea in archivo:
            array.extend(linea.rstrip().split())
        for i in range(saltos):
            delay = 0
            for x in range(len(array)):
                if array[x + delay] == '0':
                    array[x + delay] = '1'
                #Si es par
                elif int(len(array[x + delay])) % 2 == 0:
                    p1,p2 = partir_por_la_mitad(array[x + delay])
                    array[x + delay] = str(int(p1))
                    array.insert(x + delay + 1,str(int(p2)))
                    delay += 1
                else:
                    array[x + delay] = str(int(array[x + delay]) * 2024)
            # print(array)
        print(len(array))





