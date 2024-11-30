print("")
print("Zamarripa Castro Erick Fabian 3W 1220")
print("")

#Clase "Contacto" con contactos como definido
class Agenda:
    def __init__(self):
        self.contactos = []

#Permite añadir un contacto a la agenda
    def añadir_contacto(self):
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el teléfono: ")
        email = input("Ingrese el email: ")
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print(f"Contacto '{nombre}' añadido exitosamente.")

#Muestra la lista de los contactos ya añadidos
    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

#Permite buscar un contacto ya existente
    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre.lower():
                print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                return
        print(f"Contacto '{nombre}' no encontrado.")

#Permire editar el contacto deseado ya registrado
    def editar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre.lower():
                nuevo_nombre = input("Ingrese el nuevo nombre (dejar vacío para no cambiar): ")
                nuevo_telefono = input("Ingrese el nuevo teléfono (dejar vacío para no cambiar): ")
                nuevo_email = input("Ingrese el nuevo email (dejar vacío para no cambiar): ")

                if nuevo_nombre:
                    contacto['nombre'] = nuevo_nombre
                if nuevo_telefono:
                    contacto['telefono'] = nuevo_telefono
                if nuevo_email:
                    contacto['email'] = nuevo_email

                print(f"Contacto '{nombre}' editado exitosamente.")
                return
        print(f"Contacto '{nombre}' no encontrado.")

#Muestra el menu y da las opciones a elegir dependiendo del numero ingresado
    def menu(self):
        while True:
            print("\n--- Menú de Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.añadir_contacto()
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                print("Cerrando la agenda...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

#Ejecución de la agenda
if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()