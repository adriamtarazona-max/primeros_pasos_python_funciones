#***************** zona de funciones *******************
#palabra_clave + nombre_funcion(verbo) + parametro(adjetivo)
def capturar_nombre():
    nombre_usuario = input("escriba el nombre del usuario:")
    return nombre_usuario
def capturar_rol():
    rol_usuario = input("escriba su rol:")
    return rol_usuario
def capturar_hora():
    hora = int(input("escriba la hora (0-23):"))

    if  0 <=  hora < 12:
        saludo = "buenos dias"
    elif 12 <= hora < 18:
        saludo = "buenas tardes"
    elif  18 <=  hora < 24:
        saludo = "buenas noches"
    else :
        saludo = "hora incorrecta"

    return saludo, hora
    
def  hacer_mensaje(nombre_usuario, rol_usuario, saludo, hora):
    mensaje = f" {saludo} {nombre_usuario}. su rol es {rol_usuario}. la hora es {hora}."
    return mensaje
def impirmir_mensaje(mensaje):
    print(mensaje)


#****************** zona de codigo principal ***********************

dato_nombre = capturar_nombre()
dato_rol = capturar_rol()
saludo, dato_hora = capturar_hora()
dato_mensaje = hacer_mensaje(dato_nombre , dato_rol, saludo, dato_hora)
impirmir_mensaje(dato_mensaje)
