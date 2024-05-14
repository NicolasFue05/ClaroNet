def menu():
    print("""
--------------------------------------------
            CLARO DATABASE                   
--------------------------------------------
[1] USUARIOS
[2] SERVICIOS
[3] PRODUCTOS
[4] ATENCION AL CLIENTE 
[0] SALIR                        
--------------------------------------------
""") 
    


    
def menuAdminClientes():
    print("""
--------------------------------
            USUARIOS                    
--------------------------------          
[1] CREAR USUARIO
[2] LEER INFORMACION DE USUARIO
[3] ACTUALIZAR USUARIO
[4] ELIMINAR USUARIO              
[5] MOSTRAR CLIENTES LEALES
[6] MOSTRAR CLIENTES REGULARES
[7] MOSTRAR CLIENTES NUEVOS 
[8] OFERTAS Y PROMOCIONES      
[0] SALIR          
-------------------------------          
""")
    
def menuAdminServicios():
    print("""
--------------------------------
          SERVICIOS          
--------------------------------          
[1] AGREGAR SERVICIO AL CATALOGO
[2] MOSTRAR CATALOGO DE SERVICIOS
[3] COMPRAR SERVICIOS          
[4] ACTUALIZAR SERVICIOS          
[5] ELIMINAR SERVICIOS    
[6] VOLVER AL MENU PRINCIPAL          
[0] SALIR
--------------------------------          
""")

# MENU USER
def menuAdminProductos():
    print("""
-----------------------------
          PRODUCTOS          
-----------------------------       
[1] AGREGAR PRODUCTO
[2] MOSTRAR CATALOGO DE PRODUCTOS
[3] COMPRAR PRODUCTO
[4] ACTUALIZAR PRODUCTO
[5] ELIMINAR PRODUCTO
[0] SALIR                              
-----------------------------           
""")
    

def menuServicioAlCliente():
    print("""
---------------------------
    SERVICIO AL CLIENTE          
---------------------------
[1] SUGERENCIAS
[2] RECLAMOS
[0] VOLVER
---------------------------               
""")