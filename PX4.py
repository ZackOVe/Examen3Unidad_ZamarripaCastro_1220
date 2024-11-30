print("")
print("Zamarripa Castro Erick Fabian 3W 1220")
print("")

#Clase "Calculadora" con numeros como definidos
class Calculadora:
    def __init__(self):
        # Inicializa los valores de la calculadora
        self.num1 = int(input("Introduce el primer número entero: "))
        self.num2 = int(input("Introduce el segundo número entero: "))

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"

#Crear una instancia de la clase Calculadora
calculadora = Calculadora()

#Realizar las operaciones y mostrar los resultados
print(f"Suma: {calculadora.suma()}")
print(f"Resta: {calculadora.resta()}")
print(f"Multiplicación: {calculadora.multiplicacion()}")
print(f"División: {calculadora.division()}")