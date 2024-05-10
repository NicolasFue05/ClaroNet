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
def GuardarConsulta():
     None


# Servicio al cliente
def ServicioCliente():
    None