class Usuario:
    """docstring fs Usuario"""
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self,saludo):
        print(saludo + self.nombre)

class Empleado(Usuario):
    salario = 0

    def modificar_salario(self,salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)

    def saluda(self):
        print ("Hola mi nombre es "+self.nombre+"y gano: " + str(self.salario))


empleado = Empleado("Marlon")

empleado.modificar_salario(1000)
empleado.ver_salario()

empleado.saluda()

#hay un metdo super que llama lo que originalmente habie en ese valor 
