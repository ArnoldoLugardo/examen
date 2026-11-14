# SISTEMA DE REGISTRO Y ANALISIS DE ESTUDIANTES

estudiantes = []


# Funcion para mostrar el menu
def mostrar_menu():
    print("\n===== SISTEMA DE ESTUDIANTES =====")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Consultar promedio de un estudiante")
    print("4. Mostrar estadisticas generales")
    print("5. Salir")


# Funcion para calcular el promedio
def calcular_promedio(calificaciones):
    promedio = sum(calificaciones) / 3
    return promedio


# Funcion para registrar estudiantes
def registrar_estudiante():

    print("\n--- REGISTRO DE ESTUDIANTE ---")

    identificacion = input("Numero de identificacion: ")

    while identificacion.strip() == "":
        print("La identificacion no puede estar vacia.")
        identificacion = input("Numero de identificacion: ")

    # Verificar identificacion duplicada
    for estudiante in estudiantes:
        if estudiante["identificacion"] == identificacion:
            print("Error: Esta identificacion ya esta registrada.")
            return

    nombre = input("Nombre del estudiante: ")

    while nombre.strip() == "":
        print("El nombre no puede estar vacio.")
        nombre = input("Nombre del estudiante: ")

    calificaciones = []

    # Solicitar las tres calificaciones
    for i in range(3):

        while True:
            try:
                calificacion = float(input("Ingresa la calificacion " + str(i + 1) + ": "))

                if calificacion >= 0 and calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificacion debe estar entre 0 y 100.")

            except ValueError:
                print("Error: Ingresa un numero valido.")

    # Convertir calificaciones en tupla
    calificaciones = tuple(calificaciones)

    promedio = calcular_promedio(calificaciones)

    # Determinar situacion academica
    if promedio >= 70:
        situacion = "Aprobado"
    else:
        situacion = "Reprobado"

    # Guardar estudiante en diccionario
    nuevo_estudiante = {
        "identificacion": identificacion,
        "nombre": nombre,
        "calificaciones": calificaciones,
        "promedio": promedio,
        "situacion": situacion
    }

    estudiantes.append(nuevo_estudiante)

    print("\nEstudiante registrado correctamente.")
    print("Promedio:", round(promedio, 2))
    print("Situacion:", situacion)


# Funcion para mostrar todos los estudiantes
def mostrar_estudiantes():

    print("\n--- ESTUDIANTES REGISTRADOS ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            print("\nIdentificacion:", estudiante["identificacion"])
            print("Nombre:", estudiante["nombre"])
            print("Calificaciones:", estudiante["calificaciones"])
            print("Promedio:", round(estudiante["promedio"], 2))
            print("Situacion:", estudiante["situacion"])


# Funcion para consultar un estudiante
def consultar_estudiante():

    print("\n--- CONSULTAR ESTUDIANTE ---")

    identificacion = input("Ingresa el numero de identificacion: ")

    encontrado = False

    for estudiante in estudiantes:

        if estudiante["identificacion"] == identificacion:

            print("\nEstudiante encontrado.")
            print("Nombre:", estudiante["nombre"])
            print("Promedio:", round(estudiante["promedio"], 2))
            print("Situacion:", estudiante["situacion"])

            encontrado = True
            break

    if encontrado == False:
        print("No se encontro ningun estudiante con esa identificacion.")


# Funcion para mostrar estadisticas generales
def mostrar_estadisticas():

    print("\n--- ESTADISTICAS GENERALES ---")

    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    total = len(estudiantes)
    suma_promedios = 0
    aprobados = 0
    reprobados = 0
    promedio_alto = 0

    for estudiante in estudiantes:

        suma_promedios += estudiante["promedio"]

        if estudiante["situacion"] == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1

        if estudiante["promedio"] > promedio_alto:
            promedio_alto = estudiante["promedio"]

    promedio_general = suma_promedios / total

    print("Estudiantes registrados:", total)
    print("Promedio general:", round(promedio_general, 2))
    print("Estudiantes aprobados:", aprobados)
    print("Estudiantes reprobados:", reprobados)
    print("Promedio mas alto:", round(promedio_alto, 2))


# PROGRAMA PRINCIPAL

opcion = 0

while opcion != 5:

    mostrar_menu()

    try:
        opcion = int(input("\nSelecciona una opcion: "))

        if opcion == 1:
            registrar_estudiante()

        elif opcion == 2:
            mostrar_estudiantes()

        elif opcion == 3:
            consultar_estudiante()

        elif opcion == 4:
            mostrar_estadisticas()

        elif opcion == 5:
            print("\nGracias por utilizar el sistema.")

        else:
            print("Opcion no valida. Intenta nuevamente.")

    except ValueError:
        print("Error: Debes ingresar un numero.")
