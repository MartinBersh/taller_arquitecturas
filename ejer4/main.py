from ejer4.GestionEstudiantes import GestionEstudiantes
from ejer4.InterfazUsuario import InterfazUsuario

if __name__ == "__main__":
    interfaz = InterfazUsuario()
    gestion_estudiantes = GestionEstudiantes()

    while True:
        interfaz.mostrar_menu_principal()
        opcion = interfaz.obtener_opcion()

        if opcion == "1":
            nombre, edad, carrera = interfaz.obtener_datos_estudiante()
            gestion_estudiantes.registrar_estudiante(nombre, edad, carrera)
            print("Estudiante registrado correctamente.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            estudiante = gestion_estudiantes.buscar_estudiante(nombre)
            if estudiante:
                interfaz.mostrar_estudiante(estudiante)
            else:
                print("Estudiante no encontrado.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante a actualizar: ")
            nueva_edad = input("Ingrese la nueva edad del estudiante: ")
            nueva_carrera = input("Ingrese la nueva carrera del estudiante: ")
            if gestion_estudiantes.actualizar_estudiante(nombre, nueva_edad, nueva_carrera):
                print("Estudiante actualizado correctamente.")
            else:
                print("Estudiante no encontrado.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del estudiante a eliminar: ")
            if gestion_estudiantes.eliminar_estudiante(nombre):
                print("Estudiante eliminado correctamente.")
            else:
                print("Estudiante no encontrado.")
        elif opcion == "5":
            print("Saliendo del sistema")
            break
        else:
            print("Opción inválida")
