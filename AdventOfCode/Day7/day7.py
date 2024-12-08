from itertools import product

global yMax
global xMax

def operacion(val1,operacion,var2):
    if operacion == "|":
        return int(str(val1)+str(var2))
    return eval(f"{val1} {operacion} {var2}")

def transformarOperacionBinaria(grosor,parte2):

    operadores = ['+', '*']
    if parte2 is True:
        operadores = ['+', '*', '|']

    # Generamos todas las combinaciones posibles de operadores
    combinaciones = list(product(operadores, repeat=grosor))

    # Convertimos cada tupla de combinaciones en una cadena
    return [''.join(comb) for comb in combinaciones]

def detectarResultadoValido(result,variables,parte2=False):
    res = 0
    operadores = transformarOperacionBinaria(len(variables)-1,parte2);

    for operador in operadores:
        operador = list(operador)
        for j in range(len(variables)):
            if j == 0:
                res = variables[j]
            else:
                try:
                    res = operacion(res,operador[j-1],variables[j])
                except:
                    print(operadores)
                    print(variables)

            if res == result:
                return res
    return 0


if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:
        contador = 0
        contador2 = 0
        for y, linea in enumerate(archivo):
            [result, variables] = linea.split(":")
            result = int(result)
            variables = [int(x) for x in variables.rstrip().split()]
            # contador += detectarResultadoValido(result,variables)
            contador2 += detectarResultadoValido(result,variables,True)
        print("Ejercicio 1", contador)
        print("Ejercicio 2", contador2)





