

def obtenerComboOperandValor(valor,registros = list[int]):
    if valor >= 0 or valor <=3:
        return valor
    if valor == 4:
        return registros[0]
    if valor == 5:
        return registros[1]
    if valor == 6:
        return registros[2]
    raise Exception("No es valido")

if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        print("hola")
        map = [ linea.strip().split() for linea in file ]
        registers = [int(reg[2]) for reg in map[0:3]]
        program = [int(numeros) for numeros in map[4][1].split(',')]
        print(registers)
        print(program)



