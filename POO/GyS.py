class Usuario:
    __edad=0
    """docstring fs Usuario"""
    def __init__(self,nombre):
        self._nombre = nombre
        #_nombre es que es protegido.
    def saludar(self,saludo):
        print(saludo + self.nombre)

    @property
    def edad(self): #getter
        return self.__edad


    @edad.setter
    def edad(self,valor):
        if valor < 0:
            raise ValueError('Numero no puede ser menor que 0')
        else:
            self.__edad = valor



class Empleado(Usuario):
    __salario = 0

    def modificar_salario(self,salario): #Setter
        self.__salario = salario

    def ver_salario(self): #Getter
        print(self.__salario)

    def saluda(self):
        print ("Hola mi nombre es "+self._nombre+"y gano: " + str(self.__salario))


    # __ es cuando portege el atributo, ponerlo en privado.
empleado = Empleado("Marlon")
empleado.edad = -1
print(empleado.edad)
