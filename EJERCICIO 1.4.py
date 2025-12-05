 #ZONA DE FUNCIONES

def definir_cantidad():
    return int (input("digite la cantidad de numero que desea sumar: "))

def acumular_suma(cantidad):
    suma = 0
    for i in range (cantidad):
        print("digite el numero", i + 1, ":", end="")
        numero = int(input())
        suma = suma + numero
    return suma
def mostrar_total(suma):
    print("la sumatoria total es:", suma)

#CODIGO PRINCIPAL
cantidad = definir_cantidad()
suma_total = acumular_suma (cantidad)
mostrar_total(suma_total)
