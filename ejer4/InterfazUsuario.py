class InterfazUsuario:
    def __init__(self):
        pass

    def mostrar_menu_principal(self):
        print("1. Registrar nuevo estudiante")
        print("2. Buscar estudiante")
        print("3. Actualizar información de estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")

    def obtener_opcion(self):
        return input("Ingrese su opción: ")

    def obtener_datos_estudiante(self):
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        carrera = input("Carrera: ")
        return nombre, edad, carrera

    def mostrar_estudiante(self, estudiante):
        print("Datos del estudiante:")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Carrera: {estudiante['carrera']}")
