print("")
print("Zamarripa Castro Erick Fabian 3W 1220")
print("")

#Clase "Triangulo" con los lados como definidos
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        #Retorna el lado mayor del triángulo.
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        #Determina el tipo de triángulo.
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir_info(self):
        #Imprime el lado mayor y el tipo de triángulo.
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")


#Ejemplo de uso
if __name__ == "__main__":
    # Solicitar al usuario que ingrese los lados del triángulo
    lado1 = float(input("Ingrese el lado 1: "))
    lado2 = float(input("Ingrese el lado 2: "))
    lado3 = float(input("Ingrese el lado 3: "))

     #Crear una instancia de Triangulo
    triangulo = Triangulo(lado1, lado2, lado3)

    #Imprimir información del triángulo
    triangulo.imprimir_info()
