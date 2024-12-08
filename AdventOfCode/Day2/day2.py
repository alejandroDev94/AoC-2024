
def nuclear_fussion_variaciones(lista):
    for i in range(len(lista)):
            lista_saneada = lista[:i] + lista[i+1:]
            if nuclear_fusion(lista_saneada):
                return 1
    return 0


def es_creciente(lista):
    return all(lista[i] < lista[i+1] and abs(lista[i]-lista[i+1]) < 4 for i in range(len(lista)-1))

def es_decreciente(lista):
    return all(lista[i] > lista[i+1] and abs(lista[i]-lista[i+1]) < 4 for i in range(len(lista)-1))

def nuclear_fusion(lista):
    if es_creciente(lista):
        return 1
    elif es_decreciente(lista):
        return 1
    else:
        #print("Para este caso no hay ninguno ", lista)
        return 0

if __name__ == '__main__':
    with open('input.txt','r') as archivo:
        safe = 0
        safe2 = 0
        for linea in archivo:
            fila = [int(x) for x in linea.strip().split()]
        # Ejercicio 1
            safe += nuclear_fusion(fila)
        # Ejercicio 2
            safe2 += nuclear_fussion_variaciones(fila)
        print(safe)
        print(safe2)

