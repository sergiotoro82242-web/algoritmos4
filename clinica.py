import heapq

def menu_clinica():
    pacientes = []
    orden = 0

    while True:
        print("\nMENU CLINICA ")
        print("1. Ingresar paciente")
        print("2. Atender paciente")
        print("3. Mostrar cola")
        print("4. Salir")

        opcion = input("Opcion: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            prioridad = int(input("Prioridad (1-3): "))

            if 1 <= prioridad <= 3:
                heapq.heappush(pacientes, (prioridad, orden, nombre))
                orden += 1
                print("Paciente agregado")
            else:
                print("La prioridad debe ser entre 1 y 3")

        elif opcion == "2":
            if pacientes:
                prioridad, orden_llegada, nombre = heapq.heappop(pacientes)
                print(f"Atendiendo a {nombre} (Prioridad {prioridad})")
            else:
                print("No hay pacientes")

        elif opcion == "3":
            print("\nPacientes en espera:")

            if not pacientes:
                print("No hay pacientes")
            else:
                temp = []
                while pacientes:
                    p = heapq.heappop(pacientes)
                    print(f"Nombre: {p[2]} | Prioridad: {p[0]}")
                    temp.append(p)

                for p in temp:
                    heapq.heappush(pacientes, p)

        elif opcion == "4":
            break

        else:
            print("Opcion invalida")

menu_clinica()
