# This is a sample Python script.
from tutorial1 import *


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def multiplyInputNTimes(phrase,n:int,py_list=[]):
    if isinstance(phrase,str):
        return (phrase+" ") * n
    return phrase * n;
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')
    print(multiplyInputNTimes("hola",4))
    print(multiplyInputNTimes(2,4))
    tutorial1 = Tutorial1()

    # Suma de valores
    print(tutorial1.sumaDeValores())

    # Max entre valores
    print(tutorial1.maxBetweenValues(5,1,2,3,4))

    # Min entre valores
    print(tutorial1.minBetweenValues(5,1,2,3,4))

    # Abs check is number --> Aquí resuelve None
    print(tutorial1.absNumericValue("a"))

    # Abs check is number --> Aquí resuelve el valor
    print(tutorial1.absNumericValue(1))

    help(round)

    # Print con separadores
    print(1,2,3,4,sep=' < ')


    # Probando funciones como agumentos
    print("Resultado de la funcion " ,call(mult_by_n,4,5))


    # El round de un numero en dos places
    print("Redondeo de solo 2 decimales", round(333.1477,-2))

