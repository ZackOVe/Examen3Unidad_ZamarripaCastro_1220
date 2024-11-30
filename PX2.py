print("")
print("Zamarripa Castro Erick Fabian 3W 1220")
print("")

#Clase "Persona" con nombre y edad como definidos
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

#Permite al usuario ingresar nombre y edad para mostrar si es mayor de edad o no
a = Persona(str(input("Escriba su nombre: ")),float(input("Ingresa tu edad: ")))

if a.edad < 18:
  print (a.nombre, "Eres menor con: ", a.edad)
else:
  print (a.nombre, "Eres mayor con: ", a.edad)
