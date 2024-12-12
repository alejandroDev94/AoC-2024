
class Nodo:
    def __init__(self,numero, posicion = []):
        self.posicion = posicion       # posicionNodo
        self.numero = numero
        self.nodoArriba = None
        self.nodoDerecha = None
        self.nodoIzquierda = None
        self.nodoAbajo = None
        self.tiene9 = numero == 9
        self.pasoPorAqui = False


    def nodo_path_valido(self,parte2 = False):
        cont = 0
        # print("posiciones ",self.posicion,self.numero, cont)
        if self.tiene9 is True:
            #Parte 2
            if parte2 is True:
                return 1

            #Parte1
            if self.pasoPorAqui is False:
                self.pasoPorAqui = True
                return 1
            return 0
        if self.nodoIzquierda is not None and self.nodoIzquierda.numero - self.numero == 1:
            cont += self.nodoIzquierda.nodo_path_valido(parte2)
        if self.nodoArriba is not None and self.nodoArriba.numero - self.numero == 1:
            cont += self.nodoArriba.nodo_path_valido(parte2)
        if self.nodoDerecha is not None and self.nodoDerecha.numero - self.numero == 1:
            cont += self.nodoDerecha.nodo_path_valido(parte2)
        if self.nodoAbajo is not None and self.nodoAbajo.numero - self.numero == 1:
            cont += self.nodoAbajo.nodo_path_valido(parte2)
        return cont
    def get_nodo_actual(self):
        return self

    def asociar_nodo_arriba(self,nuevo_nodo):
        self.nodoArriba = nuevo_nodo

    def asociar_nodo_derecha(self,nuevo_nodo):
        self.nodoDerecha = nuevo_nodo

    def asociar_nodo_abajo(self, nuevo_nodo):
        self.nodoAbajo = nuevo_nodo

    def asociar_nodo_izquierda(self,nuevo_nodo):
        self.nodoIzquierda = nuevo_nodo

    def __repr__(self):
        return f"Nodo({self.numero})Posicion({self.posicion})"


if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:

        inicio = 0
        end = 9
        nodosCero = []
        nodos_ini = {}
        nodos_fin = []

        for y, linea in enumerate(archivo):
            for x, valor in enumerate((linea.rstrip())):
                nodo = Nodo(int(valor), [x, y])
                nodos_ini[f"{x},{y}"] = nodo

                # No se requiere chequear mas porque en el bucle for siempre lee de derecha a izquierda y
                # luego siempre baja entonces siempre tendremos arriba ya abajo completados y abajo derecha sin saber

                #Asociar Nodos de la izquierda
                nodoizquierda = nodos_ini.get(f"{x-1},{y}",None)
                if nodoizquierda is not None:
                    nodoizquierda.asociar_nodo_derecha(nodo)
                    nodo.asociar_nodo_izquierda(nodoizquierda)
                # Asociar Nodos de la Arriba
                nodoArriba = nodos_ini.get(f"{x},{y-1}", None)
                if nodoArriba is not None:
                    nodoArriba.asociar_nodo_abajo(nodo)
                    nodo.asociar_nodo_arriba(nodoArriba)

                # Nos guardamos los nodos 0 porque tiene que salir el 0  y asi los nodos van buscando eellos solos
                if valor == '0':
                    nodosCero.append(nodo)
                if valor == '9':
                    nodos_fin.append(nodo)


        # Ejercicio 1
        resultado1 = 0
        for nodox in nodosCero:
            resultado1 += nodox.nodo_path_valido()
            nodos_fin = [setattr(_, 'pasoPorAqui', False) or _ for _ in nodos_fin]
        print("Resultado1 ",resultado1)

        # Ejercicio 2
        resultado2 = 0
        for nodox in nodosCero:
            resultado2 += nodox.nodo_path_valido(True)
            nodos_fin = [setattr(_, 'pasoPorAqui', False) or _ for _ in nodos_fin]
        print("Resultado1 ",resultado2)




