import json
from time import time
import os

import json,os,time, traceback
from datetime import datetime


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


# Capturar excepciones
def capturarException(exception):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear el mensaje de error con la fecha y hora
    mensaje_error = (f"Fecha y hora: {fecha_actual}\n")
    mensaje_error += traceback.format_exc()  # Agregar el traceback de la excepción
    
    # Guardar el mensaje de error en un archivo de texto
    with open("exceptions.txt", "a") as file:
        file.write(mensaje_error + "\n")


    os.system("cls")
    print("----------------")        
    print("VALOR INCORRECTO")
    print("----------------")
    os.system("cls")
    time.sleep(2)   


    
#USER SECTION

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

          

# Compra de servicios
def ComprarServicios(referencia, id_cliente, nombre_cliente):
    # Cargar los datos de los servicios
    with open("ServiciosDataBase.json", "r") as file :
        servicios = json.load(file)

    # Cargar json de las ventas
    with open("VentasDataBase.json", "r") as file:
        datos = json.load(file)

    # Buscar el cliente en el json de clientes
    cliente_encontrado = False
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)
        for cliente in clientes["Clientes"]:
            if cliente["Identificacion"] == id_cliente:
                cliente_encontrado = True
                break

    if cliente_encontrado:
        # Buscar el servicio en la lista de servicios
        for servicio in servicios["Servicios"]:
            if servicio["Referencia"] == referencia:
                # Añadir el servicio contratado a la lista de ventas de servicios
                datos["Ventas"].append({
                    "Servicio": servicio,
                    "Comprador": {
                        "ID": id_cliente,
                        "Nombre": nombre_cliente
                    }
                })
                os.system("cls") 
                print("COMPRA REALIZADA CON EXITO!")
                time.sleep(2)
                # Escribir los datos actualizados en el archivo JSON
                with open("VentasDataBase.json", "w") as file:
                    json.dump(datos, file, indent=4)
                return True
        print("NO SE ENCONTRO EL SERVICIO CON ESA REFERENCIA.")
    else:
        print("EL ID DEL CLIENTE NO SE ENCONTRO.")
    return False         


# Compra de productos
def ComprarProductos(referencia, id_cliente, nombre_cliente):
    # Cargar los datos de los productos
    with open("ProductosDataBase.json", "r") as file :
        productos = json.load(file)

    # Cargar json de las ventas
    with open("VentasDataBase.json", "r") as file:
        datos = json.load(file)

    # Buscar el cliente en el json de clientes
    cliente_encontrado = False
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)
        for cliente in clientes["Clientes"]:
            if cliente["Identificacion"] == id_cliente:
                cliente_encontrado = True
                break

    if cliente_encontrado:
        # Buscar el producto en la lista de productos
        for producto in productos["Productos"]:
            if producto["Referencia"] == referencia:
                # Añadir el producto vendido a la lista de ventas
                datos["Ventas"].append({
                    "Producto": producto,
                    "Comprador": {
                        "ID": id_cliente,
                        "Nombre": nombre_cliente
                    }
                })
                os.system("cls") 
                print("COMPRA REALIZADA CON EXITO!")
                time.sleep(2)                
                # Escribir los datos actualizados en el archivo JSON
                with open("VentasDataBase.json", "w") as file:
                    json.dump(datos, file, indent=4)
                return True
        print("NO SE ENCONTRO EL PRODUCTO CON ESA REFERENCIA.")
    else:
        print("EL ID DEL CLIENTE NO SE ENCONTRO.")
    return False



# Guardar Sugerencia
def GuardarSugerencia(Sugerencia):
    nombre = input("Ingrese el nombre del usuario que hace la sugerencia: ").title()
    identificacion = input("Ingrese la identificación del usuario que hace la sugerencia: ").title()

    # Abrir el archivo JSON de clientes y cargar los datos
    with open("ClientesDataBase.json", "r") as file:
        clientes_data = json.load(file)

    # Verificar si el usuario está en la lista de clientes
    usuario_encontrado = False
    for cliente in clientes_data["Clientes"]:
        if cliente.get("Nombre") == nombre and cliente.get("Identificacion") == identificacion:
            usuario_encontrado = True
            break

    if usuario_encontrado:
        # Abrir el archivo JSON de sugerencias y cargar los datos
        with open("SugerenciasDataBase.json", "r") as file:
            sugerencias_data = json.load(file)

        # Añadir la sugerencia al diccionario
        sugerencias_data["Sugerencias"].append({"Nombre": nombre, "Identificacion": identificacion, "Sugerencia": Sugerencia})

        # Actualizar el archivo JSON de sugerencias
        with open("SugerenciasDataBase.json", "w") as file:
            json.dump(sugerencias_data, file, indent=4)
        

        print("-----------------------------")
        print("SUGERENCIA ENVIADA CON EXITO!")
        print("-----------------------------")
        time.sleep(2)
    else:
        print("EL USUARIO NO SE ENCUENTRA EN LA BASE DE DATOS DEL CLIENTE.")
        time.sleep(2)


# Función para guardar un reclamo en el archivo JSON
def GuardarReclamos(reclamo):
    nombre = input("Ingrese el nombre del usuario que reporta el problema: ").title()
    identificacion = input("Ingrese la identificación del usuario que reporta el problema: ").title()

    # Abrir el archivo JSON de clientes y cargar los datos
    with open("ClientesDataBase.json", "r") as file:
        clientes_data = json.load(file)

    # Verificar si el usuario está en la lista de clientes
    usuario_encontrado = False
    for cliente in clientes_data["Clientes"]:
        if cliente.get("Nombre") == nombre and cliente.get("Identificacion") == identificacion:
            usuario_encontrado = True
            break

    if usuario_encontrado:
        # Abrir el archivo JSON de reclamos y cargar los datos
        with open("ReclamosDataBase.json", "r") as file:
            reclamos_data = json.load(file)

        # Añadir el problema al diccionario
        reclamos_data["Reclamos"].append({"Nombre": nombre, "Identificacion": identificacion, "Reclamo": reclamo})

        # Actualizar el archivo JSON de reclamos
        with open("ReclamosDataBase.json", "w") as file:
            json.dump(reclamos_data, file, indent=4)
        
        print("RECLAMO GUARDADO CON EXITO")
        time.sleep(2)
        os.system("cls")
        return
    else:
        print("EL USUARIO NO SE ENCUENTRA EN LA BASE DE DATOS DEL CLIENTE.")
        time.sleep(2)
        os.system("cls")      



# Crear User
def CrearUsuario():
    # Se abre el JSON de clientes y se carga en la variable clientes
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)

    # Se crea un diccionario de cliente y se solicita la información del cliente
    clienteNuevo = {
        "Nombre": input("INGRESA EL NOMBRE DEL CLIENTE: ").title(),
        "Identificacion": input("INGRESA EL ID DEL CLIENTE: "),
        "Informacion de Contacto": input("INGRESA LA INFORMACION DE CONTACTO DEL CLIENTE: "),
        "Telefono Del Cliente": input("INGRESA EL TELEFONO DE CONTACTO DEL CLIENTE: "),
        "Direccion de Residencia": input("INGRESA LA DIRECCION DEL RESIDENCIA DEL CLIENTE: ").title(),
        "Tipo de cliente": "Nuevo",
        "Historial de Compras": "ACTUALMENTE EL CLIENTE NO TIENE COMPRAS"
    }

    # Verificar si ya existe un cliente con el mismo ID
    for cliente in clientes["Clientes"]:
        if cliente["Identificacion"] == clienteNuevo["Identificacion"]:
            print("Ya existe un cliente con el mismo ID.")
            return

    # Se solicita confirmación para agregar el cliente
    option = int(input("SEGURO QUE DESEAS AGREGAR ESE CLIENTE?\n[1] Si\n[2] NO\n>> "))
    if option == 1:
        # Se agrega el usuario a la lista de clientes
        clientes["Clientes"].append(clienteNuevo)

        # Se sobrescribe el JSON de clientes con los datos actualizados
        with open("ClientesDataBase.json", "w") as file:
            json.dump(clientes, file, indent=4)
            return True
    else:
        print("NO SE HA AGREGADO EL CLIENTE.")

# Mostrar Clientes
def MostrarClientes():
    # cargar el json de clientes
    with open("ClientesDataBase.json", "r") as file:
        data = json.load(file)
    
    # Se verifica si hay clientes en la lista
    clientes = data.get("Clientes", [])
    if len(clientes) == 0:
        print("No hay clientes registrados.")
    else:
        print("LISTADO DE CLIENTES:")
        for cliente in clientes:
            print("--------------------")
            print("Nombre:", cliente["Nombre"])
            print("Identificación:", cliente["Identificacion"])
            print("Información de Contacto:", cliente["Informacion de Contacto"])
            print("Dirección de Residencia:", cliente["Direccion de Residencia"])
            print("Tipo de Cliente:", cliente.get("Tipo de cliente", "Regular"))  # Se maneja el caso de que no haya tipo de cliente
            print("Historial de Compras:", cliente["Historial de Compras"])
            print("--------------------")

def obtener_ofertas_cliente(json_data):
    # Cargar el JSON
    with open(json_data, "r") as file:
        data = json.load(file)

    # Obtener la lista de clientes
    clientes = data["Clientes"]

    # Función para obtener las ofertas según el tipo de cliente
    def obtener_ofertas(tipo_cliente):
        ofertas = []
        
        # Ofertas para clientes regulares
        if tipo_cliente == "Regular":
            ofertas.append("Descuento del 10% en la compra de un Smartwatch Apple Series 7.")
            ofertas.append("Promoción: Plan PostPago con SMS Ilimitados por $8 en lugar de $10.")
        
        # Ofertas para clientes leales
        elif tipo_cliente == "Leal":
            ofertas.append("Upgrade gratuito a la versión Pro del Servicio de Atención al Cliente 24/7.")
            ofertas.append("Oferta especial: Consola PlayStation 5 Slim Standard a $3,500.")
        
        # Ofertas para clientes nuevos
        elif tipo_cliente == "Nuevo":
            ofertas.append("Descuento del 15% en la compra de un iPhone 13 Pro Max.")
            ofertas.append("Promoción de bienvenida: Internet de Fibra Óptica con 1 mes gratis.")
        
        return ofertas

    # Lista para almacenar las ofertas de cada cliente
    ofertas_clientes = []

    # Analizar el tipo de cliente para cada cliente en la lista
    for cliente in clientes:
        tipo_cliente = cliente["Tipo de cliente"]
        nombre_cliente = cliente["Nombre"]
        ofertas_cliente = obtener_ofertas(tipo_cliente)
        ofertas_clientes.append({"Cliente": nombre_cliente, "Ofertas": ofertas_cliente})

    return ofertas_clientes

# ACTUALIZAR CLIENTE
def ActualizarCliente():
    # Abrir el archivo JSON de clientes y cargar los datos
    with open("ClientesDataBase.json", "r") as file:
        clientes_data = json.load(file)

    # Pedir al usuario que ingrese la identificación del cliente que desea actualizar
    identificacion = input("Ingrese la identificación del cliente que desea actualizar: ")

    # Buscar el cliente con la identificación proporcionada
    cliente_encontrado = False
    for cliente in clientes_data["Clientes"]:
        if cliente.get("Identificacion") == identificacion:
            cliente_encontrado = True
            # Mostrar las características actuales del cliente
            print("Características actuales del cliente:")
            print("--------------------")
            for key, value in cliente.items():
                print(f"{key}: {value}")
            print("--------------------")
            
            # Pedir al usuario que ingrese las características que desea actualizar
            print("Ingrese las características que desea actualizar (deje vacío para mantener el valor actual):")
            for key in cliente.keys():
                if key != "Identificacion":
                    new_value = input(f"{key}: ")
                    if new_value:
                        cliente[key] = new_value
            
            # Actualizar el archivo JSON con los datos actualizados del cliente
            with open("ClientesDataBase.json", "w") as file:
                json.dump(clientes_data, file, indent=4)
            return True


# Eliminar clientes de la lista
def EliminarCliente():
    #Abrir el archivo json de clientes 
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)

    #pedir al usuario el id del cliente a eliminar
    identificacion = input("INGRESA EL ID DEL CLIENTE QUE DESEAS ELIMINAR\n>> ")

    #Buscar el indice del cliente con la identificacion
    indexCliente = None
    for index, cliente in enumerate(clientes["Clientes"]):
        if cliente.get("Identificacion") == identificacion:
            indexCliente = index
            break

        # preguntar
    eliminar = int(input("Seguro que deseas eliminar ese cliente?[1] Si / [2] No : "))


    # si se encuentra el cliente eliminarlo
    if indexCliente is not None and eliminar == 1:
        del clientes["Clientes"][indexCliente]

        #actualizar el json de la lista de clientes
        with open("ClientesDataBase.json", "w") as file:
            json.dump(clientes, file, indent=4)
            os.system("cls")
            print("CLIENTE ELIMINADO CORRECTAMENTE")
            time.sleep(2)
    else:
        os.system("cls")
        print("NO SE ENCUENTRA NINGUN CLIENTE CON ESE ID")
        time.sleep(2)


# listar los clientes leales
def ClientesLeales():
    # abrir el json de clientes
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)

    # filtrar los clientes de tipo leal
    leales = [cliente for cliente in clientes["Clientes"] if cliente.get("Tipo de cliente") == "Leal"]

    # Mostrar la lista de clientes leales
    if leales:
        print("CLIENTES LEALES:")
        print("----------------")
        for cliente in leales:
            print(f"Nombre: {cliente['Nombre']}")
            print(f"Identificacion: {cliente['Identificacion']}")
            print(f"Informacion de Contacto: {cliente['Informacion de Contacto']}")
            print(f"Telefono De Contacto: {cliente['Telefono Del Cliente']}")
            print(f"Direccion de Residencia: {cliente['Direccion de Residencia']}")
            print(f"Historial de Compras: {cliente['Historial de Compras']}")
            print("---------------------------------------------------------------")
    else:
        print("NO HAY CLIENTES LEALES")


# mostrar clientes regulares
def ClientesRegulares():
    # abrir el json de clientes
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)

    # filtrar los clientes regulares
    regulares = [cliente for cliente in clientes["Clientes"] if cliente.get("Tipo de cliente") == "Regular"]

    # mostrar la lista de clientes regulares
    if regulares:
        print("CLIENTES REGULARES")
        print("------------------")
        for cliente in regulares:
            print(f"Nombre: {cliente['Nombre']}")
            print(f"Identificacion: {cliente['Identificacion']}")
            print(f"Informacion de Contacto: {cliente['Informacion de Contacto']}")
            print(f"Telefono De Contacto: {cliente['Telefono Del Cliente']}")
            print(f"Direccion de Residencia: {cliente['Direccion de Residencia']}")
            print(f"Historial de Compras: {cliente['Historial de Compras']}")
            print("-------------------------------------------------------------")
    else:
        print("NO SE ENCUENTRA EL TIPO DE CLIENTE")


# mostrar clientes nuevos
def ClientesNuevos():
    # abrir el json de clientes
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)

    # filtrar los clientes regulares
    regulares = [cliente for cliente in clientes["Clientes"] if cliente.get("Tipo de cliente") == "Nuevo"]

    # mostrar la lista de clientes regulares
    if regulares:
        print("CLIENTES NUEVOS")
        print("------------------")
        for cliente in regulares:
            print(f"Nombre: {cliente['Nombre']}")
            print(f"Identificacion: {cliente['Identificacion']}")
            print(f"Informacion de Contacto: {cliente['Informacion de Contacto']}")
            print(f"Telefono De Contacto: {cliente['Telefono Del Cliente']}")
            print(f"Direccion de Residencia: {cliente['Direccion de Residencia']}")
            print(f"Historial de Compras: {cliente['Historial de Compras']}")
            print("-------------------------------------------------------------")
    else:
        print("NO SE ENCUENTRA EL TIPO DE CLIENTE")


def AgregarServicio():
    # Abrir el archivo JSON de servicios 
    with open("ServiciosDataBase.json", "r") as file:
        servicios = json.load(file)

    
    servicioNuevo = {
        "Nombre" : input("Ingresa el nombre del servicio: "),
        "Referencia" : input("Ingresa la referencia del servicio: "),
        "Descripcion" : input("Ingresa la descripcion del servicio: "),
        "Detalles" : input("Ingresa los detalles del servicio: "),
        "Precio" : input("Ingresa el precio del servicio: ")
    }

    # verificar si ya existe un servicio con la misma referencia
    for servicio in servicios["Servicios"]:
        if servicio["Referencia"] == servicioNuevo["Referencia"]:
            print("YA EXISTE UN SERVICIO CON LA MISMA REFERENCIA.")
            return
        
    # Se solicita confirmación para agregar el SERVICIO
    option = int(input("SEGURO QUE DESEAS AGREGAR ESE SERVICIO?\n[1] Si\n[2] NO\n>> "))
    if option == 1:
        # Se agrega el usuario a la lista de clientes
        servicios["Servicios"].append(servicioNuevo)

        # Se sobrescribe el JSON de clientes con los datos actualizados
        with open("ServiciosDataBase.json", "w") as file:
            json.dump(servicios, file, indent=4)
        print("SERVICIO AGREGADO CON EXITO.")
        time.sleep(2)
        os.system("cls")
    else:
        print("NO SE HA AGREGADO EL CLIENTE.")



# Compra de servicios
def ComprarServicios(referencia, id_cliente, nombre_cliente):
    # Cargar los datos de los servicios
    with open("ServiciosDataBase.json", "r") as file :
        servicios = json.load(file)

    # Cargar json de las ventas
    with open("VentasDataBase.json", "r") as file:
        datos = json.load(file)

    # Buscar el cliente en el json de clientes
    cliente_encontrado = False
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)
        for cliente in clientes["Clientes"]:
            if cliente["Identificacion"] == id_cliente:
                cliente_encontrado = True
                break

    if cliente_encontrado:
        # Buscar el servicio en la lista de servicios
        for servicio in servicios["Servicios"]:
            if servicio["Referencia"] == referencia:
                # Añadir el servicio contratado a la lista de ventas de servicios
                datos["Ventas"].append({
                    "Servicio": servicio,
                    "Comprador": {
                        "Nombre": nombre_cliente,
                        "Identificacion": id_cliente
                    }
                })
    
                os.system("cls")
                # Escribir los datos actualizados en el archivo JSON
                with open("VentasDataBase.json", "w") as file:
                    json.dump(datos, file, indent=4)
                return True
        print("NO SE ENCONTRO EL SERVICIO CON ESA REFERENCIA.")
    else:
        print("EL ID DEL CLIENTE NO SE ENCONTRO.")
    return False



        
# Compra de productos
def ComprarProductos(referencia, id_cliente, nombre_cliente):
    # Cargar los datos de los productos
    with open("ProductosDataBase.json", "r") as file :
        productos = json.load(file)

    # Cargar json de las ventas
    with open("VentasDataBase.json", "r") as file:
        datos = json.load(file)

    # Buscar el cliente en el json de clientes
    cliente_encontrado = False
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)
        for cliente in clientes["Clientes"]:
            if cliente["Identificacion"] == id_cliente:
                cliente_encontrado = True
                break

    if cliente_encontrado:
        # Buscar el producto en la lista de productos
        for producto in productos["Productos"]:
            if producto["Referencia"] == referencia:
                # Añadir el producto vendido a la lista de ventas
                datos["Ventas"].append({
                    "Producto": producto,
                    "Comprador": {
                        "identificacion": id_cliente,
                        "Nombre": nombre_cliente
                    }
                })
                # Escribir los datos actualizados en el archivo JSON
                with open("VentasDataBase.json", "w") as file:
                    json.dump(datos, file, indent=4)
                return True
        print("NO SE ENCONTRO EL PRODUCTO CON ESA REFERENCIA.")
    else:
        print("EL ID DEL CLIENTE NO SE ENCONTRO.")
    return False




# Actualizar historial de compras con nombre y referencia del servicio
def actualizarHistorialDeCompras(id_cliente, nombre_servicio, referencia_servicio):
    # Cargar los datos del archivo JSON de clientes
    with open("ClientesDataBase.json", "r") as file:
        clientes = json.load(file)

    # Buscar el cliente por su identificación
    for cliente in clientes["Clientes"]:
        if cliente["Identificacion"] == id_cliente:
            # Actualizar el historial de compras del cliente con el nombre y la referencia del servicio
            if cliente["Historial de Compras"] == "ACTUALMENTE EL CLIENTE NO TIENE COMPRAS":
                cliente["Historial de Compras"] = [f"{nombre_servicio} - {referencia_servicio}"]
            else:
                cliente["Historial de Compras"] += [f"{nombre_servicio} - {referencia_servicio}"]

            # Escribir los datos actualizados en el archivo JSON
            with open("ClientesDataBase.json", "w") as file:
                json.dump(clientes, file, indent=4)
            return True

    print("EL ID DEL CLIENTE NO SE ENCONTRO.")
    return False


# actualizar servicios
def ActualizarServicio():
    # Abrir el archivo JSON de servicios y cargar los datos
    with open("ServiciosDataBase.json", "r") as file:
        servicios_data = json.load(file)

    # Pedir al usuario que ingrese la referencia del servicio que desea actualizar
    referencia = input("Ingrese la referencia del servicio que desea actualizar: ")

    # Buscar el servicio con la referencia proporcionada
    servicio_encontrado = False
    for servicio in servicios_data["Servicios"]:
        if servicio.get("Referencia") == referencia:
            servicio_encontrado = True
            # Mostrar las características actuales del servicio
            print("Características actuales del servicio:")
            print("--------------------")
            for key, value in servicio.items():
                print(f"{key}: {value}")
            print("--------------------")
            
            # Pedir al usuario que ingrese las características que desea actualizar
            print("Ingrese las características que desea actualizar (deje vacío para mantener el valor actual):")
            for key in servicio.keys():
                if key != "Referencia":
                    new_value = input(f"{key}: ")
                    if new_value:
                        servicio[key] = new_value
            
            # Actualizar el archivo JSON con los datos actualizados del servicio
            with open("ServiciosDataBase.json", "w") as file:
                json.dump(servicios_data, file, indent=4)
            
            os.system("cls")
            print("SERVICIO ACTUALIZADO CORRECTAMENTE.")
            time.sleep(2)
            os.system("cls") 
            break

    if not servicio_encontrado:
        print("NO SE ENCONTRÓ NINGÚN SERVICIO CON ESA REFERENCIA.")


# eliminar servicio
def EliminarServicio():
    # Abrir el archivo JSON de servicios y cargar los datos
    with open("ServiciosDataBase.json", "r") as file:
        servicios = json.load(file)

    # Pedir al usuario la referencia del servicio a eliminar
    referencia = input("Ingrese la referencia del servicio que desea eliminar: ")

    # Buscar el índice del servicio con la referencia
    index_servicio = None
    for index, servicio in enumerate(servicios["Servicios"]):
        if servicio.get("Referencia") == referencia:
            index_servicio = index
            break

    # Si se encuentra el servicio, eliminarlo
    if index_servicio is not None:
        del servicios["Servicios"][index_servicio]

        # Actualizar el archivo JSON de la lista de servicios
        with open("ServiciosDataBase.json", "w") as file:
            json.dump(servicios, file, indent=4)
            os.system("cls")
            print("SERVICIO ELIMINADO CORRECTAMENTE")
            time.sleep(2)
    else:
        os.system("cls")
        print("NO SE ENCUENTRA NINGÚN SERVICIO CON ESA REFERENCIA")
        time.sleep(2)

# agregar productos
def AgregarProducto():
    # Abrir el archivo JSON de productos 
    with open("ProductosDataBase.json", "r") as file:
        productos = json.load(file)

    # Crear un nuevo producto con la información proporcionada por el usuario
    nuevo_producto = {
        "Nombre": input("Ingrese el nombre del producto: "),
        "Referencia": input("Ingrese la referencia del producto: "),
        "Descripcion": input("Ingrese la descripcion del producto: "),
        "Especificaciones": input("Ingresa las especificaciones del producto: "),
        "Caracteristicas": input("Ingrese las caracteristicas del producto: "),
        "Disponibilidad" : "Disponible",
        "Precio": input("Ingrese el precio del producto: ")
    }

    # Verificar si ya existe un producto con la misma referencia
    for producto in productos["Productos"]:
        if producto["Referencia"] == nuevo_producto["Referencia"]:
            print("YA EXISTE UN PRODUCTO CON LA MISMA REFERENCIA.")
            return
        
    # Solicitar confirmación para agregar el producto
    option = int(input("¿Seguro que deseas agregar este producto?\n[1] Si\n[2] NO\n>> "))
    if option == 1:
        # Agregar el producto a la lista de productos
        productos["Productos"].append(nuevo_producto)

        # Sobrescribir el JSON de productos con los datos actualizados
        with open("ProductosDataBase.json", "w") as file:
            json.dump(productos, file, indent=4)
        print("PRODUCTO AGREGADO CON ÉXITO.")
        time.sleep(2)
        os.system("cls")
    else:
        print("NO SE HA AGREGADO EL PRODUCTO.")


# actualizar productos
def ActualizarProducto():
    # Abrir el archivo JSON de productos y cargar los datos
    with open("ProductosDataBase.json", "r") as file:
        productos_data = json.load(file)

    # Pedir al usuario que ingrese la referencia del producto que desea actualizar
    referencia = input("Ingrese la referencia del producto que desea actualizar: ")

    # Buscar el producto con la referencia proporcionada
    producto_encontrado = False
    for producto in productos_data["Productos"]:
        if producto.get("Referencia") == referencia:
            producto_encontrado = True
            # Mostrar las características actuales del producto
            print("Características actuales del producto:")
            print("--------------------")
            for key, value in producto.items():
                print(f"{key}: {value}")
            print("--------------------")
            
            # Pedir al usuario que ingrese las características que desea actualizar
            print("Ingrese las características que desea actualizar (deje vacío para mantener el valor actual):")
            for key in producto.keys():
                if key != "Referencia":
                    new_value = input(f"{key}: ")
                    if new_value:
                        producto[key] = new_value
            
            # Actualizar el archivo JSON con los datos actualizados del producto
            with open("ProductosDataBase.json", "w") as file:
                json.dump(productos_data, file, indent=4)
            
            os.system("cls")
            print("PRODUCTO ACTUALIZADO CORRECTAMENTE.")
            time.sleep(2)
            os.system("cls") 
            break

    if not producto_encontrado:
        print("NO SE ENCONTRÓ NINGÚN PRODUCTO CON ESA REFERENCIA.")


# eliminar productos
def EliminarProducto():
    # Abrir el archivo JSON de productos y cargar los datos
    with open("ProductosDataBase.json", "r") as file:
        productos = json.load(file)

    # Pedir al usuario la referencia del producto a eliminar
    referencia = input("Ingrese la referencia del producto que desea eliminar: ")

    # Buscar el índice del producto con la referencia
    index_producto = None
    for index, producto in enumerate(productos["Productos"]):
        if producto.get("Referencia") == referencia:
            index_producto = index
            break

    # Si se encuentra el producto, eliminarlo
    if index_producto is not None:
        del productos["Productos"][index_producto]

        # Actualizar el archivo JSON de la lista de productos
        with open("ProductosDataBase.json", "w") as file:
            json.dump(productos, file, indent=4)
            os.system("cls")
            print("PRODUCTO ELIMINADO CORRECTAMENTE")
            time.sleep(2)
    else:
        os.system("cls")
        print("NO SE ENCUENTRA NINGÚN PRODUCTO CON ESA REFERENCIA")
        time.sleep(2)