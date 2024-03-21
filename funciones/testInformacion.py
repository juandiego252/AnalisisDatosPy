import informacion

for i in range(12):
    nombreUsuario = input("Ingrese su Nombre y Apellido: ")
    anioUsuario = int(input("Ingrese su año de Nacimiento:"))
    informacion.agregar_nombre(nombreUsuario)
    informacion.agregar_edad(anioUsuario)
print("---- Informacion Pacientes ----")
print(informacion.nombre_paciente)
print("---- Edades Pacientes ----")
print(informacion.edad)
print("---- Paciente menor ----")
print(min(informacion.edad))
print("---- Paciente Mayor ----")
print(max(informacion.edad))
