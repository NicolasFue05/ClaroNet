from menu import *
from Functions import *
import time, os
from datetime import datetime

# Se crea un bucle principal
while True:
    try:
        # se muestra el primer menu
        os.system("cls")
        menu()
        # se pide una opcion a ingresar
        opcion = int(input(">> "))
        if opcion == 1:
            os.system("cls")
            menuAdminClientes()
            eleccion =  int(input(">> "))
            while True:
                os.system("cls")
                if eleccion == 1:
                    print("AGREGAR NUEVO CLIENTE")
                    if CrearUsuario():
                        print("Cliente agregado")
                        time.sleep(2)
                        os.system("cls")
                        break
                elif eleccion == 2:
                    MostrarClientes()
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 3:
                    print("ACTUALIZAR CLIENTE")
                    ActualizarCliente()
                    if ActualizarCliente:
                        os.system("cls")
                        print("CLIENTE ACTUALIZADO EXITOSAMENTE")
                        time.sleep(2)
                        os.system("cls")
                    else:
                        print("No se guardo el cliente")
                        time.sleep(2)
                        os.system("cls")
                    break
                elif eleccion == 4:
                    print("ELIMINAR CLIENTE")
                    EliminarCliente()
                    salir = int(input("[1] SALIR\n>>"))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 5:
                    ClientesLeales()
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 6:
                    ClientesRegulares()
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 7:
                    ClientesNuevos()
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 8:
                    ofertas = obtener_ofertas_cliente("ClientesDataBase.json")
                    for oferta_cliente in ofertas:
                        print(f"Ofertas para el cliente {oferta_cliente["Cliente"]}")
                        for oferta in oferta_cliente["Ofertas"]:
                            print(f"- {oferta}")
                    salir = int(input("[1] Salir\n>> "))
                    if salir == 1:
                        os.system("cls")
                        break
                elif eleccion == 0:
                    os.system("cls")
                    break
                else:
                    print("INGRESE UNA OPCION VALIDA")
        # Servicios        
        elif opcion == 2:
            os.system("cls")
            menuAdminServicios()
            eleccion = int(input(">> "))
            while True:
                os.system("cls")
                if eleccion == 1:
                    print("AGREGAR NUEVO SERVICIO")
                    AgregarServicio()
                    break
                elif eleccion == 2:
                    MostrarCatalogo("ServiciosDataBase.json")
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 3:
                    MostrarCatalogo("ServiciosDataBase.json")
                    nombreServicio = input("Ingrese el nombre del servicio: ").title()
                    referencia = input("Ingrese la referencia del servicio: ")
                    nombre = input("Ingrese el nombre del cliente que desea comprarlo: ").title()
                    identificacion = input("Ingrese el ID del cliente: ")
                    if ComprarServicios(referencia,identificacion,nombre):
                        os.system("cls")
                        print("-----------------------------")
                        print("PRODUCTO AGREGADO CON EXITO!!")
                        print("-----------------------------")
                        time.sleep(2)
                        os.system("cls")
                    actualizarHistorialDeCompras(identificacion,nombreServicio, referencia)
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 4:
                    print("ACTUALIZAR SERVICIO")
                    ActualizarServicio()
                    break
                elif eleccion == 5:
                    print("ELIMINAR SERVICIO")
                    EliminarServicio()
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 0:
                    os.system("cls")
                    break
        # productos
        elif opcion == 3:
            os.system("cls")
            menuAdminProductos()
            eleccion = int(input(">> "))
            while True:
                os.system("cls")
                if eleccion == 1:
                    print("AGREGAR NUEVO PRODUCTO")
                    AgregarProducto()
                    break
                elif eleccion == 2:
                    MostrarCatalogo("ProductosDataBase.json")
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 3:
                    MostrarCatalogo("ProductosDataBase.json")
                    nombreProducto = input("Ingrese el nombre del producto: ").title()
                    referencia = input("Ingrese la referencia del producto: ")
                    nombre = input("Ingrese el nombre del cliente que desea comprarlo: ").title()
                    identificacion = input("Ingrese el ID del cliente: ")
                    if ComprarProductos(referencia,identificacion,nombre):
                        os.system("cls")
                        print("-----------------------------")
                        print("PRODUCTO AGREGADO CON EXITO!!")
                        print("-----------------------------")
                        time.sleep(2)
                        os.system("cls")
                    actualizarHistorialDeCompras(identificacion,nombreProducto, referencia)
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 4:
                    print("ACTUALIZAR PRODUCTO")
                    ActualizarProducto()
                    break
                elif eleccion == 5:
                    print("ELIMINAR PRODUCTO")
                    EliminarProducto()
                    salir = int(input("[1] SALIR\n>> "))
                    if salir == 1:
                        break
                    else:
                        print("INGRESE UNA OPCION VALIDA")
                elif eleccion == 0:
                    os.system("cls")
                    break
        # servicio al cliente
        elif opcion == 4:
            os.system("cls")
            menuServicioAlCliente()
            eleccion = int(input(">> "))
            while True:
                os.system("cls")
                if eleccion == 1:
                    print("SUGERENCIAS")
                    sugerencia = str(input("INGRESA LA SUGERENCIA QUE DESEES\n>> "))
                    GuardarSugerencia(sugerencia)
                    break
                elif eleccion == 2:
                    print("RECLAMOS")
                    reclamo = str(input("INGRESA EL RECLAMO QUE DESEES\n>> "))
                    GuardarReclamos(reclamo)
                    break
                elif eleccion == 0:
                    os.system("cls")
                    break
                else:
                    print("INGRESE UNA OPCION VALIDA")
        
        elif opcion == 0:
            os.system("cls")
            print("SALIENDO...")
            time.sleep(2)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("----------------")
            print("OPCION INVALIDA!")
            print("----------------")
            time.sleep(2)
            os.system("cls")

        os.system("cls")
        print("----------------")        
        print("VALOR INCORRECTO")
        print("----------------")
        os.system("cls")
        time.sleep(2) 
    except ValueError as e:
        capturarException(e)
    except Exception as e:
        capturarException(e)