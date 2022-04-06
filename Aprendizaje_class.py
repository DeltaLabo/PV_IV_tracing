class Saludo:
    def __init__(self):
        self.nombre = "Name"
       
    
    def saludar(self):
        print(f"Hola, {self.nombre}")

saludos = Saludo()
saludos.saludar()


class Rectangulo:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return self.b * self.h
rectangulo = Rectangulo(20 , 10)
print('El área es: ', rectangulo.area())


class Person:
    name = ''
    school = ''
     
    def print_information(self, name, school):
        print (self.name)
        print (self.school)
             
jorge = Person()
jorge.name = 'Jorge'
jorge.school = 'Universidad de la vida'
jorge.print_information(jorge.name, jorge.school)

voltaje = 0
corriente = 0
for x in range (0,15):
    voltaje = voltaje + 0.5
    corriente = corriente + 0.2
    print("V: ",voltaje,"   ","Curr:  ",corriente)
