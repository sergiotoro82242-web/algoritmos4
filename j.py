
import time

class Clinica:
    def __init__(self, Nombre, Documento):
        self.Nombre = Nombre
        self.Documento = Documento
        self.siguiente= None
class Paciente:
    def __init__(self):
        self.head = None
        self.tail = None
    def agregarPaciente(self, Nombre, Documento):
        nuevoPaciente = Clinica(Nombre, Documento)
        if self.head is None:
            self.head = nuevoPaciente
        else:
            actual = self.head
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevoPaciente

    def atenderEmergencia(self, Nombre, Documento):
            nuevoPaciente = Clinica(Nombre, Documento)
            if self.head is None:
                self.head = nuevoPaciente
            else:
                nuevoPaciente.siguiente = self.head
                self.head = nuevoPaciente
    def atenderPaciente(self):
        if self.head is None:
            print ("No se encuntran pacientes")
        else:
            print("Atendiendo al Paciente",self.head.Nombre)
            self.head = self.head.siguiente
    def mostrar(self):
        actual = self.head
        while actual is not None:
            print("Nombre paciente: ", actual.Nombre, "Documento: ", actual.Documento, end= "--->")
            actual = actual.siguiente
        print("No hay mas pacientes")
            


paciente = Paciente()
print("Bienvenido a la clinica una nueva esperanza")
while True:
    print("¿Qué deseas hacer?")
    print("1. Ingresar paciente normal")
    print("2. Ingresar paciente de emergencia")
    print("3. Atender al primer paciente de la lista")
    print("4. Mostrar la lista completa")
    print("0. Cerrar explorador")
    opcion = int(input())
    if opcion == 1:
        Nombre = input("Ingrese el nombre: ")
        Documento = input("Ingrese el documento del paciente: ")
        paciente.agregarPaciente(Nombre, Documento)
        
    elif opcion == 2:
        Nombre = input("Ingrese el nombre del paciente: ")
        Documento = input("Ingrese el documento de la persona: ")
        paciente.atenderEmergencia(Nombre, Documento)

    elif opcion == 3:
        paciente.atenderPaciente()

    elif opcion == 4:
        paciente.mostrar()

    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opción no permitida")