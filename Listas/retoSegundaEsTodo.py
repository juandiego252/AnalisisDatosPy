menu = ["Salchipapa","Encebollado","Bowl Cerdo"]
print("--- MENU ---")
print("1. Añadir plato al Menu")
print("2. Buscar en el Menu")
print("3. Eliminar plato del Menu")
print("4. Mostrar Platos en el Menu")
opcionUsuario = int(input("Seleccione su opcion (1-4): "))
if opcionUsuario == 1:
    platoNuevo = input("Ingrese el plato que quiere añadir = ")
    menu.append(platoNuevo)
    print(f"El plato {platoNuevo} se ha añadido con exito al menu")
elif opcionUsuario == 2:
    platoBuscar = input("Ingrese el plato que quiere buscar: ")
    if platoBuscar in menu:
        print(f"El plato se encuentra en la lista en la posicion {menu.index(platoBuscar)}")
    else:
        print("El plato no se encuentra en la lista")
elif opcionUsuario == 3:
    platoEliminar = input("Ingrese el plato que quiere eliminar: ")
    menu.remove(platoEliminar)
    print("Plato eliminado con exito")
elif opcionUsuario == 4:
    print(menu)