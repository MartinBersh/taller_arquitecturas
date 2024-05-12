class GestionEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def registrar_estudiante(self, nombre, edad, carrera):
        estudiante = {"nombre": nombre, "edad": edad, "carrera": carrera}
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante["nombre"] == nombre:
                return estudiante
        return None

    def actualizar_estudiante(self, nombre, nueva_edad, nueva_carrera):
        for estudiante in self.estudiantes:
            if estudiante["nombre"] == nombre:
                estudiante["edad"] = nueva_edad
                estudiante["carrera"] = nueva_carrera
                return True
        return False

    def eliminar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante["nombre"] == nombre:
                self.estudiantes.remove(estudiante)
                return True
        return False
