'''class Curso(object):
    nombre= "Marlon"
    def Saludar(self,saludo):
        print( saludo +  self.nombre)

Marlon = Curso()

Marlon.Saludar("Hola mi nombre es ")
'''
class Usuario:
    """docstring for Curso."""

    def __init__(self, nombre):
        #Metodo constructor
        self.nombre = nombre

    def Saludar(self,saludo):
        print( saludo +  self.nombre)

class Empleado(Usuario):
    salario = 0

    def modificarsalario(self,salario):
        self.salario =salario

    def ver_salario(self):
        print(self.salario)

    def Saludar(self):
        print( "Hola mi nombre es" + self.nombre +  "Mi salario es de "+ string(self.salario))

empleado = Empleado("Marlon")
empleado.modificarsalario(1000)
empleado.ver_salario()
empleado.Saludar()
