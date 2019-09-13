class Curso(object):
    nombre= "Marlon"
    def Saludar(self,saludo):
        print( saludo +  self.nombre)

Marlon = Curso()

Marlon.Saludar("Hola mi nombre es ")
