def menu():
    print("""
--------------------------------------------
       QUIEN ESTA USANDO EL PROGRAMA?                    
--------------------------------------------
[1] USUARIO
[2] ADMINISTRADOR
[3] SALIR
--------------------------------------------
""") 

# MENUS ADMIN
def menuAdmin():
    print("""
[1] USUARIOS
[2] SERVICIOS
[3] VOLVER AL MENU PRINCIPAL          
""")
def menuUsers_Admin():
    print("""
[1] CREAR USUARIO
[2] LEER INFORMACION DE USUARIO
[3] ACTUALIZAR USUARIO
[4] ELIMINAR USUARIO              
[5] MOSTRAR CLIENTES LEALES
[6] MOSTRAR CLIENTES REGULARES
[7] VOLVER AL MENU PRINCIPAL          
[8] SALIR          
""")
def menuServices_Admin():
    print("""
[1] AGREGAR SERVICIO AL CATALOGO
[2] LEER SERVICIO DEL CATALOGO
[3] ACTUALIZAR SERVICIOS          
[4] ELIMINAR SERVICIOS    
[5] VOLVER AL MENU PRINCIPAL          
[5] SALIR
""")

# MENU USER
def menuUser():
    print("""
-----------------------------       
[1] MOSTRAR CATALOGO DE SERVICIOS
[2] MOSTRAR CATALOGO DE PRODUCTOS          
[3] SERVICIO AL CLIENTE
[4] RECLAMOS
[5] SUGERENCIAS
[6] VOLVER AL MENU PRINCIPAL                 
-----------------------------           
""")

def eleccion():
    return int(input(">> "))
    