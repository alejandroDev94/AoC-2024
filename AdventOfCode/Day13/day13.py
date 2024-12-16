import re
def ley_cramer(ax,bx,px,ay,by,py):
    determinante = ax * by - bx * ay
    if determinante == 0:
        return (None,None)

    x = (px * by - bx * py) / determinante
    y = (ax * py - px * ay) / determinante

    if x.is_integer() and y.is_integer():
        return (x,y)
    return (None, None)

if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:

        px, py = 0, 0
        ax, by = 0, 0
        bx, ay = 0, 0
        total_parte1 = 0
        total_parte2 = 0
        for x,linea in enumerate(archivo):
            numeros = list(map(int, re.findall("\d+",linea)))
            if numeros:
                if 'Button A' in linea:
                    ax, ay = numeros[0], numeros[1]
                elif 'Button B' in linea:
                    bx, by = numeros[0], numeros[1]
                else:
                    px, py = numeros[0], numeros[1]
                    a, b = ley_cramer(ax,bx,px,ay,by,py)
                    #Parte1
                    if a is not None and b is not None:
                        if a <= 100 and b <= 100:
                            total_parte1 += int(a*3 +b)
                    #parte2
                    a2, b2 = ley_cramer(ax, bx, 10000000000000+px, ay, by, 10000000000000+py)
                    if a2 is not None and b2 is not None:
                        total_parte2 += int(a2 * 3 + b2)

        print("parte 1",total_parte1)
        print("parte 2",total_parte2)










