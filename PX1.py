print("")
print("Zamarripa Castro Erick Fabian 3W 1220")
print("")

#Crear clase "Alumno" con nombre y nota como definidos
class Alumno:
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

#Permite al usuario ingresar nombre y nota para luego mostrar si aprobo o no
a = Alumno(str(input("Escriba su nombre: ")),float(input("Ingresa tu calificacion final: ")))

if a.nota < 6:
  print (a.nombre, "Reprobaste con: ", a.nota)
else:
  print (a.nombre, "Aprobaste con: ", a.nota)