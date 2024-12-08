import numbers


class Tutorial1:

    def sumaDeValores(self):
        print("# Suma de valores")
        return (1+2)/100;

    def maxBetweenValues(self,*values):
        print("# Maximo valor del set")
        return max(list(values))

    def minBetweenValues(self,*values):
        print("# Minimo valor del set")
        return min(list(values))

    def absNumericValue(self,num:int):
        print("# abs valores numericos")
        if isinstance(num, numbers.Number):
            return abs(num)
        return None


def mult_by_n(num,n):
    return num*n;

def call(fn,num,n):
    return fn(num,n)