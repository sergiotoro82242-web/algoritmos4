class Estudiante:
    def _init_(self, documento, nombre, telefono):
        self.documento = documento
        self.nombre = nombre
        self.telefono = telefono
estudiante1 = Estudiante(1111, "Juan", 24848)