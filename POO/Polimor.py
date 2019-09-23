class Numero:
    value = 0

    def __init__(self,value):
        self.value= value

    def compare(self,numero):
        if numero.value > self.value:
            return numero.value
        return self.value

class Cadena:
    value = ""

    def __init__(self,value):
        self.value= value

    def compare(self,cadena):
        palabras=[self.value,cadena.value]
        palabras.sort()
        return palabras[0]


class Lista:
    value = []

    def __init__(self,value):
        self.value= value


    def compare(self,lista):
        if len(self.value) > len(lista.value):
            return self.value
        return lista.value


def retornElMayor(a,b):
    return a.compare(b)

num1 = Numero(100)
num2 = Numero(12)

cad1 = Cadena("Marlon")
cad2 = Cadena("Andrea")

list1 = Lista([1,2,3])
list2 = Lista([1,2,3,4,5])

print(retornElMayor(num1,num2))
print(retornElMayor(cad1,cad2))
print(retornElMayor(list1,list2))

"""
def retornElMayor(a,b):
    if isinstance(a,int) and isinstance(b,int):
        if a > b:
            return a
        return b
    if isinstance(a,str) and isinstance(b,str):
        palabras=[a,b]
        palabras.sort()
        return palabras[0]
    if isinstance(a,list) and isinstance(b,list):
        if len(a) > len(b):
            return a
        return b

print(retornElMayor("Marlon","Andrea"))
"""
