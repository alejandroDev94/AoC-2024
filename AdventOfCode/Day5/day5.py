
def fitrarRutasValidas(rutasValidas,rutasToCheck,invalid ):
    validas = []

    for ruta in rutasToCheck:
        valido = True
        for i in range(len(ruta)):
            # print("valor ",ruta[i])
            for j in range(i+1,len(ruta)):
                # print(ruta[j])
                if next((x for x in rutasValidas if x[0]+"|"+x[1] == ruta[i]+"|"+ruta[j]) ,None) is None:
                    valido = False
                    break
        if valido is True:
            validas.append(ruta)
        else:
            invalid.append(ruta)

    rutasToCheck[:] = validas
def ordenarRutasInvalidas(rutasValidas,invalid):

    for ruta in invalid:
        for i in range(len(ruta)):
            # print("valor ",ruta[i])
            for j in range(i + 1, len(ruta)):
                # print(ruta[j])
                if next((x for x in rutasValidas if x[0] + "|" + x[1] == ruta[i] + "|" + ruta[j]), None) is None:
                    aux = ruta[i]
                    ruta[i] = ruta[j]
                    ruta[j] = aux



if __name__ == '__main__':
    with open('input5.txt', 'r') as archivo:
        rutasToCheck = []
        rutasChecked = []
        invalid = []
        saving = []
        segundaCadena = False
        for linea in archivo:
            # print(linea.rstrip())
            if linea.rstrip() == "":
                # print("vacio")
                rutasValidas = saving
                saving = []
                segundaCadena = True
            else:
                saving.append(linea.rstrip().split(",") if segundaCadena else linea.rstrip().split("|"))
        rutasToCheck = saving

        #Ejercicio1
        fitrarRutasValidas(rutasValidas,rutasToCheck,invalid)
        media = 0
        for ruta in rutasToCheck:
            media += int(ruta[len(ruta)//2])
        print("Ejercicio 1",media)
        #Ejercicio2
        media2 = 0

        ordenarRutasInvalidas(rutasValidas,invalid)
        for ruta2 in invalid:
            # ruta2 = sorted(ruta2, reverse=True)
            # print(ruta2)
            media2 += int(ruta2[len(ruta2) // 2])
        print("Ejercicio 2", media2)



