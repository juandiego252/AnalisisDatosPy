datos = []
numeroVeces = int(input("Ingrese la cantidad de datos que quiere guardar: "))
for i in range(numeroVeces):
    datosIngresados = input( f"Danto N.{i+1} :")
    if datosIngresados.isnumeric() or datosIngresados.replace('.','',1).isdigit() or isinstance(datosIngresados,str):
        datos.append(datosIngresados)
    else:
        print("Error al guardar los datos")
print(f"Su lista es: {datos}")