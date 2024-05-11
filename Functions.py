import json

# Cargar Datos
def CargarDatos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos = json.load(file)
    return datos

# Guardar Datos        
def GuardarDatos(datos, archivo):
    datos = dict(datos)
    diccionario=json.dumps(datos, indent=4)
    file = open(archivo,"w")
    file.write(diccionario)
    file.close()

# Mostrar Catalogo de Servicios
def MostrarCatalogo(archivo):
    datos = CargarDatos(archivo)
    # Comenzar a iterar
    for clave, valor in datos.items():
        print("----------------------------------------------------")
        print(f"{clave}:")
        print("----------------------------------------------------")
        for i in valor:
            for k in i.keys():
                print(f"{k}: {i[k]}")
            print("----------------------------------------------------")


# Guardar Consultas
def GuardarConsulta(consulta):
    with open("SugerenciasDataBase.json", "r") as file:
        datos = json.load(file)
    
    # Añadir la consulta al diccionario
    datos["Sugerencias"].append(consulta)
    
    # Actualizar el archivo json
    with open("SugerenciasDataBase.json", "w") as file:
        json.dump(datos, file, indent=4)


# Guarda problemas
def GuardarProblemas(problema):
    with open("ReclamosDataBase.json", "r") as file:
        datos = json.load(file)

    # añadir problema al diccionario
    datos["Reclamos"].append(problema)

    # Actualizar el json
    with open("ReclamosDataBase.json", "w") as file:
        json.dump(datos, file, indent=4)

# Compra de servicios
def ComprarServicios(referencia):
    # Cargar los datos de los productos
    with open("ServiciosDataBase.json", "r") as file :
        servicios = json.load(file)

    # Cargar json de las ventas
    with open("VentasDataBase.json", "r") as file:
        datos = json.load(file)

    # Buscar el producto en la lista de productos
    for servicio in servicios["Servicios"]:
        if servicio["Referencia"] == referencia:
            # Añadir el producto vendido a la lista de ventas
            datos["Ventas"].append(servicio)
            # Escribir los datos actualizados en el archivo JSON
            with open("VentasDataBase.json", "w") as file:
                json.dump(datos, file, indent=4)
            return
        
# Compra de productos
def ComprarProductos(referencia):
    # Cargar los datos de los productos
    with open("ProductosDataBase.json", "r") as file :
        servicios = json.load(file)

    # Cargar json de las ventas
    with open("VentasDataBase.json", "r") as file:
        datos = json.load(file)

    # Buscar el producto en la lista de productos
    for servicio in servicios["Servicios"]:
        if servicio["Referencia"] == referencia:
            # Añadir el producto vendido a la lista de ventas
            datos["Productos"].append(servicio)
            # Escribir los datos actualizados en el archivo JSON
            with open("VentasDataBase.json", "w") as file:
                json.dump(datos, file, indent=4)
            return        
        

# Verificar identificacion
def VerificarID():
    datos = CargarDatos("ClientesDataBase.json")
    for i in datos:
        None