if __name__ == '__main__':
    with open('input.txt','r') as archivo:
        izquierda = []
        derecha = []
        for linea in archivo:
            numeros = linea.strip().split()
            izquierda.append(int(numeros[0]))
            derecha.append(int(numeros[1]))
    #Ejercicio 1
    resultado = sum(abs(x - y) for x, y in zip(sorted(izquierda), sorted(derecha)))
    print("Resultado de la suma:", resultado)
    #Ejercicio 2
    resultado = 0
    for numero in izquierda:
        resultado += numero * derecha.count(numero)
    print("Resultado de la suma:", resultado)
