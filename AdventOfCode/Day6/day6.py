from enum import Enum

class Orientacion(Enum):
    NORTE = "^"
    ESTE = ">"
    SUR = "v"
    OESTE = "<"

class Guardia:
    def __init__(self, y, x, orientacion, xAnterior=None, yAnterior=None):
        self.x = x
        self.y = y
        self.contadorDePasos = 0
        self.orientacion = orientacion
        self.hitoricoPosicione = HistoricoPosiciones()
        self.hitoricoPosicione.setNuevoPaso(y, x)
        self.xAnterior = xAnterior
        self.yAnterior = yAnterior
        self._orientaciones = [Orientacion.NORTE, Orientacion.ESTE, Orientacion.SUR, Orientacion.OESTE]

    def actualizar_posicion(self, y, x):
        self.xAnterior = self.x
        self.yAnterior = self.y
        self.x = x
        self.y = y

    def establecer_orientacion(self, orientacion):
        self.orientacion = orientacion

    def girar_90_derecha(self):
        indice_actual = self._orientaciones.index(self.orientacion)
        nuevo_indice = (indice_actual + 1) % len(self._orientaciones)
        self.orientacion = self._orientaciones[nuevo_indice]

    def desplazamiento(self):
        self.xAnterior = self.x
        self.yAnterior = self.y
        if self.orientacion == Orientacion.NORTE:
            self.y = self.y - 1
        if self.orientacion == Orientacion.ESTE:
            self.x = self.x + 1
        if self.orientacion == Orientacion.OESTE:
            self.x = self.x - 1
        if self.orientacion == Orientacion.SUR:
            self.y = self.y + 1
        if self.pasePorAhi() is False:
            self.contadorDePasos += 1
        self.hitoricoPosicione.setNuevoPaso(self.y, self.x)

    def pasePorAhi(self):
        return self.hitoricoPosicione.existePasoPrevio(self.y,self.x) is True

    def getSiguientePaso(self):
        if self.orientacion == Orientacion.NORTE:
            return [self.y - 1,self.x]
        if self.orientacion == Orientacion.ESTE:
            return [self.y, self.x + 1]
        if self.orientacion == Orientacion.OESTE:
            return [self.y,self.x - 1]
        if self.orientacion == Orientacion.SUR:
            return [self.y + 1,self.x]

    def obtener_estado(self):
        return {
            "posicion_actual": [self.y, self.x],
            "orientacion": self.orientacion,
            "posicion_anterior": [self.yAnterior, self.xAnterior]
        }

class HistoricoPosiciones:

    def __init__(self):
        self.dict_posiciones = {

        }
    def setNuevoPaso(self,y,x):
        self.dict_posiciones[f"{y},{x}"] = True

    def existePasoPrevio(self,y,x):
        return self.dict_posiciones.get(f"{y},{x}", False) is True

    def getDiccionario(self):
        return self.dict_posiciones
class Obstaculos:

    def __init__(self):
        self.dict_posiciones = {

        }
    def setNuevoObstaculo(self,y,x):
        self.dict_posiciones[f"{y},{x}"] = True

    def existeObstaculo(self,y,x):
        return self.dict_posiciones.get(f"{y},{x}", False) is True

    def getDiccionario(self):
        return self.dict_posiciones

def fueraDelTablero(y,x):
    return (x < 0 or x > xMax) or (y < 0 or y > yMax)

global yMax
global xMax

if __name__ == '__main__':
    with open('input.txt', 'r') as archivo:
        guardia = None
        obstaculos = Obstaculos()
        yMax = 0
        xMax = 0
        salioDelMapa = False

        for y,linea in enumerate(archivo):
            yMax += 1
            for x,valor in enumerate(linea):
                if valor.rstrip() == "^":
                    guardia = Guardia(y, x, Orientacion.NORTE)
                    xMax = len(linea) - 1
                if valor.rstrip() == "#":
                    obstaculos.setNuevoObstaculo(y, x)
        yMax = yMax - 1

        while not salioDelMapa:
            guardia.desplazamiento()
            if fueraDelTablero(guardia.y,guardia.x):
                salioDelMapa = True
                print("Ejercicio1 ",guardia.contadorDePasos)
                break
            siguiente = guardia.getSiguientePaso()
            if obstaculos.existeObstaculo(siguiente[0], siguiente[1]):
                guardia.girar_90_derecha()

