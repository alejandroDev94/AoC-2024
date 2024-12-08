import re

def codificadorMul(lista):
    multiplicador = 0
    for dato in lista:
        try:
            separador = dato[4:-1].split(",")
            multiplicador += int(separador[0]) * int(separador[1])
        except Exception as e:
            print(dato)
            print(f"Ocurrió un error: {e}")

    return multiplicador


if __name__ == '__main__':
    with open('input.txt','r') as archivo:
        res = 0
        res2 = 0
        patron = r"mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)"
        dontdoPatron = r"don't\(\).*?do\(\)"
        for linea in archivo:
        # Ejercicio1
            coincidencias = re.findall(patron,linea)
            res += codificadorMul(coincidencias)
        #Ejercicio2
            linea2 = re.sub(dontdoPatron,'',linea)
            coincidencias2 = re.findall(patron,linea2)
            res2 += codificadorMul(coincidencias2)
        print(res)
        print(res2)

