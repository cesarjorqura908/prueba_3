import random
alumnos = []

def menu_principal():
    while True:
        print("Menú:")
        print("1. Grabar alumno")
        print("2. Buscar alumno")
        print("3. Imprimir certificados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            grabar()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            imprimir()
        elif opcion == "4":
            print("¡Hasta luego!")
            exit()
        else:
            print("Opción inválida. Intente nuevamente.")
            

def imprimir():
    
    print("Menú:")
    print("1) Certificado de Notas")
    print("2) Certificado Alumno Regular")
    print("3) certificdo de Matricula")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        C_notas()
    elif opcion == "2":
        C_regular()
    elif opcion == "3":
        C_matricula()
    elif opcion == "4":
        main()
    else:
        print("Opción inválida. Intente nuevamente.")


def C_notas():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Certificador Notas:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print("Asignaturas:")
            for asignatura in alumno['asignaturas']:
                print(f"Nombre: {asignatura['nombre']}")
                print(f"Promedio: {asignatura['promedio']}")
            print(f"Valor Certificado: {alumno['certificado_notas']}")
            return
    
def C_regular():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Alumno Regular:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
            print(f"Carrera: {alumno['carrera']}")
            print(f"Valor Certificado: {alumno['certificado_alumno_regular']}")
            return
    
    print("Alumno no encontrado.")

def C_matricula():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Matricula:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
            print(f"Carrera: {alumno['carrera']}")
            print(f"Valor Certificado: {alumno['certificado_matricula']}")
            return
    
    print("Alumno no encontrado.")
    
def grabar():
    rut = input("Ingrese el Rut del alumno (8 dígitos seguidos de guion y letra 'k' o número): ")
   
    while len(rut) != 10 or rut[9].lower() != 'k' and not rut[9].isdigit():
        rut = input("rut invalido ingresalo nuevamente")
    
    nombre = input("Ingrese nombre del alumno (entre 2 y 12 caracteres)")
    while len(nombre) < 2 or len(nombre) > 12:
        nombre = input("nombre invalido ingresalo nuevamente")
    
    apellido = input("Ingrese apellido")
    fecha = input("Ingrese fecha nacimiento")
    carrera = input("Ingrese carrera")
    
    asignaturas = []
    cant = int(input("Ingrese cantidad de asignaturas del alumno"))
    for i in range(cant):
        nomasig = input("Ingrese el nombre de la asignatura: ")
        prom = float(input("Ingrese el promedio de la asignatura: "))
        while prom < 1.0 or prom > 7.0:
            prom = float(input("Promedio inválido. Vuelva a ingresar el promedio de la asignatura: "))
        asignaturas.append({"nombre": nomasig, "promedio": prom})
    C_notas = random.randint(1000, 5000)
    C_matricula = random.randint(1000, 5000)
    C_regular = random.randint(1000, 5000)
    alumno = {"rut": rut, "nombre": nombre, "apellido": apellido, "fecha_nacimiento": fecha, "carrera": carrera, "asignaturas": asignaturas, "certificado_notas": C_notas, "certificado_alumno_regular": C_regular, "certificado_matricula": C_matricula}
    alumnos.append(alumno)
    print("Alumno registrado")
    
def buscar():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Información del alumno:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
            print(f"Carrera: {alumno['carrera']}")
            print("Asignaturas:")
            for asignatura in alumno['asignaturas']:
                print(f"Nombre: {asignatura['nombre']}")
                print(f"Promedio: {asignatura['promedio']}")
            return
    
    print("Alumno no encontrado.")

#programa_principal
menu_principal()