#**************** zona de funcion **************
def dar_letra():
    while True:
        print("digite la letra 'A' para Actualizar Sistema ")
        print("digite la letra 'B' para Eliminar Catalogo")
        print("digite la letra 'C' para Crear Productos")
        print("digite la letra 'D' para Salir del programa")
        letra = str (input ("seleccione opcion"))
        return letra

def validar_letra(dato_let):

     if dato_let=='D' or dato_let== 'd':
        mensaje = "finalizado con exito."
     elif dato_let == 'A' or dato_let == 'a':
        mensaje = "Actualizando sistema..........."

     elif dato_let == 'B' or dato_let == 'b':
          mensaje = "Eliminado catalogo........"
     elif dato_let == 'C' or dato_let=='c':
        mensaje = "Creando productos............"
    
     return mensaje
    
def dar_mensaje(dato_mensaje):
    print("se esta " + dato_mensaje)

def mensaje_alt():
    print("EL DO WHILE ha finalizado.")

#*********** zona de codigo ***************


dato_let = dar_letra()
dato_mensaje= validar_letra(dato_let)
dar_mensaje (dato_mensaje)
mensaje_alt()


    

         


