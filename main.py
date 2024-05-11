# imports
import menu,os,time,Functions

while True: # bucle principal
    menu.menu()
    try:
        option = menu.eleccion()
        # USUARIO
        if option == 1:
                while True:
                    os.system("clear")
                    menu.menuUser() # menu usuario
                    option = menu.eleccion()
                    os.system("clear")
                    if option == 1:
                        while True: # Mostrar catalogo de servicios
                            Functions.MostrarCatalogo("ServiciosDataBase.json")
                            print("--------------------")
                            print("[1] COMPRAR PRODUCTO")
                            print("[0] VOLVER")
                            print("---------------------")
                            option = menu.eleccion()
                            id = str(input("INGRESA TU IDENTIFICACION\n>> "))
                             # PONER EXCEPTION     
                            if option == 1:                                
                                print("----------------------------------------------------")
                                print("INGRESE LA REFERENCIA DEL SERVICIO QUE DESEA COMPRAR")
                                print("----------------------------------------------------")
                                referencia = str(input(">> ")) # PONER EXCEPTION
                                Functions.ComprarProductos(referencia)
                                os.system("clear")
                                print("-----------------------------")
                                print("PRODUCTO AGREGADO CON EXITO!!")
                                print("-----------------------------")
                                time.sleep(2)
                                os.system("clear")
                            elif option == 0:
                                 break
                            else:
                                os.system("clear")
                                print("----------------")
                                print("OPCION INVALIDA!")
                                print("----------------")
                                break
                    elif option == 2: # Mostrar catalogo de productos
                        while True:
                            Functions.MostrarCatalogo("ProductosDataBase.json")
                            print("--------------------")
                            print("[1] COMPRAR PRODUCTO")
                            print("[0] VOLVER")
                            print("---------------------")
                            option = menu.eleccion()   # PONER EXCEPTION     
                            if option == 1:                                
                                print("----------------------------------------------------")
                                print("INGRESE LA REFERENCIA DEL PRODUCTO QUE DESEA COMPRAR")
                                print("----------------------------------------------------")
                                referencia = str(input(">> ")) # PONER EXCEPTION
                                Functions.ComprarServicios(referencia)
                                os.system("clear")
                                print("-------------------------------")
                                print("COMPRA REALIZADA EXITOSAMENTE!!")
                                print("-------------------------------")
                                time.sleep(2)
                                os.system("clear")
                            elif option == 0:
                                 break
                            else:
                                os.system("clear")
                                print("----------------")
                                print("OPCION INVALIDA!")
                                print("----------------")
                                break
                    elif option == 3:
                        while True:  # servicio al cliente
                            menu.menuServicioAlCliente()
                            option = menu.eleccion()
                            os.system("clear")
                        #    while True:
                            if option == 1: # Sugerencias
                                    sugerencia = str(input("INGRESA LA SUGERENCIA QUE DESEES\n>> "))
                                    Functions.GuardarConsulta(sugerencia)
                                    os.system("clear")
                                    print("---------------------------")
                                    print("SUGERENCIA ENVIADA CON EXITO!")
                                    print("---------------------------")                                  
                                    time.sleep(2)
                                    print("----------")
                                    print("[1] VOLVER")
                                    print("----------") 
                                    chose = menu.eleccion()
                                    if chose == 1:
                                        os.system("clear")
                                        break                        
                                    
                            elif option == 2: # Reclamos
                                    reclamo = str(input("INGRESA EL RECLAMO QUE DESEES\n>> "))
                                    Functions.GuardarProblemas(reclamo)
                                    os.system("clear")
                                    print("---------------------------")
                                    print("RECLAMO ENVIADO CON EXITO")
                                    print("---------------------------")
                                    time.sleep(2)
                                    print("----------")
                                    print("[1] VOLVER")
                                    print("----------")
                                    option = menu.eleccion()
                                    if option == 1:
                                         os.system("clear")
                                         break                            

                            elif option == 3:
                                    break                              
                    elif option == 4:
                        break
                    else:
                        while True:
                            print("---------------")
                            print("OPCION INVALIDA")
                            print("---------------")
                            time.sleep(1)
                            os.system("clear")
                            break
            
        
        # ADMINISTRADOR 
        elif option == 2:
            os.system("clear")
            menu.menuAdmin() # mostrar menu admin
            option = menu.eleccion()
            while True: # Bucle menuAdmin
                if option == 1:
                     None # mostrar usuarios
                elif option == 2:
                    None # mostrar servicios
                elif option == 3:
                    break # volver al menu
                else:
                    os.system("clear")
                    print("------------------")
                    print("OPCION INVALIDA!!!")
                    print("------------------")
                    time.sleep(1)
                    os.system("clear")
                    break
        elif option == 3: # salir del programa
            os.system("clear")
            break
        else:
            os.system("clear")
            print("------------------")
            print("OPCION INVALIDA!!!")
            print("------------------")
            time.sleep(1)
            os.system("clear")
    except ValueError:
            os.system("clear")
            print("----------------")
            print("VALOR INVAlIDO!!")
            print("----------------")
            time.sleep(1)
            os.system("clear")
