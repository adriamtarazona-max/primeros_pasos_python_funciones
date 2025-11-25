 #zona de funciones 
def tomar_numero():
    numero = int(input("escriba el numero"))
    return numero

def validar_numero(dato_numero):
    if dato_numero >0:
        mensaje = "el numero es positivo"
    elif dato_numero ==0:
        mensaje = "el numero es negativo"
    else:
        mensaje = "el numero es negativo"
    return mensaje
def imprimir_numero(dato_mensaje):
    print("el numero es:" + dato_mensaje)

# codigo primcipal 
dato_numero = tomar_numero()
dato_mensaje = validar_numero(dato_numero)
imprimir_numero(dato_mensaje)