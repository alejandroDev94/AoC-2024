import copy

def addFiles(files,valor,indices):
    if valor not in files:
        files[valor] = []
    files[valor].append(indices)



if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:
        linea_bloque = []
        indice = 0
        control_bloques = 0
        espacios_blanco = []
        bloques_datos = []
        files = {}
        blancos = {}
        linea = archivo.readline().rstrip()


        # Lectura y guardado de datos
        for x, char in enumerate(linea):
            if control_bloques % 2 == 0:
                posicion = len(linea_bloque)
                indices = [(posicion + i) for i in range(int(char)) ]
                bloques_datos.extend(indices)
                #guardamos por key el valor y el value es los puntos donde estan estos
                addFiles(files,indice,indices)
                linea_bloque.extend([(str(indice)) for x in range(int(char))])
                indice += 1
            else:
                posicion = len(linea_bloque)
                indicesBlancos = [(posicion + i) for i in range(int(char)) ]
                #Guardamos la longitud como key y el values es los puntos en blanco consecutivos que hay
                addFiles(blancos,len(indicesBlancos),indicesBlancos)
                espacios_blanco.extend(indicesBlancos)
                linea_bloque.extend(("." * int(char)))
            control_bloques += 1

        #ordenacion
        bloques_datos = list(reversed(bloques_datos))
        print((linea_bloque))
        linea_bloque_parte2 = copy.deepcopy(linea_bloque)
        for x in range(len(espacios_blanco)):
            espacio = espacios_blanco[x]
            if espacio > bloques_datos[x]:
                break
            linea_bloque[espacio], linea_bloque[bloques_datos[x]] = linea_bloque[bloques_datos[x]], linea_bloque[espacio]
        # print("".join(linea_bloque))

        sumatorio = 0
        for x,caracter in enumerate(linea_bloque):
            if caracter == '.':
                break
            sumatorio += x * int(caracter)
        print("Ejercicio 1",sumatorio)


        #Ejercicio 2
        files = dict(reversed(list(files.items())))
        print(files)
        for clave,valor in files.items():
            #Si la longitud de los files es lo mismo que la longiturd e los puntos blancos
            for claveB,keyB in blancos.items():
                if claveB == (len(valor)):
                    elemento = keyB.remove(0)
                    for x,val in enumerate(elemento):
                        files[val], files[valor[x]] = files[valor[x]], files[val]

        print("files ",files)




