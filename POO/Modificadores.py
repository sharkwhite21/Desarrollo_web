class Usuario:
    """docstring fs Usuario"""
    def __init__(self,nombre):
        self._nombre = nombre
        #_nombre es que es protegido.
    def saludar(self,saludo):
        print(saludo + self.nombre)

class Empleado(Usuario):
    __salario = 0

    def modificar_salario(self,salario):
        self.__salario = salario

    def ver_salario(self):
        print(self.__salario)

    def saluda(self):
        print ("Hola mi nombre es "+self._nombre+"y gano: " + str(self.__salario))

    # __ es cuando portege el atributo, ponerlo en privado.
empleado = Empleado("Marlon")

empleado.modificar_salario(1000)
empleado.ver_salario()

# asi se puede acceder al privado
print(empleado._Empleado__salario)

empleado.saluda()
