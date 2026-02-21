def crearListadeEstudiantes(numeroEstudiantes):
    estudiantes = []
    for _ in range(numeroEstudiantes):
        estudiante={}
        estudiante["id"] = input("Ingrese el id del estudiante")
        estudiante["nombre"] = input("Ingrese el nombre del estudiante")
        estudiante["documento"] = input("Ingrese el documento del estudiante")
        estudiante["semestre"] = input("Ingrese el semestre del estudiante")
        estudiantes.append(estudiante)
    return estudiantes

crearListadeEstudiantes(30)