#*** zona funcion ***
def definir_numero():
    numero= int (input("digite un numero del 1 al 12: "))
    return numero
def procesar_resultado(num):
    match num:
        case 1:
            print("el mes de enero.")
        case 2:
            print("el mes de febrero.")
        case 3:
            print ("es el mes de marzo.")
        case 4: 
            print("es el mes de abril.")
        case 5: 
            print("es el mes de mayo.")
        case 6:
            print("es el mes de junio.")
        case 7:
            print(" es el mes de julio.")
        case 8:
            print("es el mes de agosto.")
        case 9:
            print("es el mes de sptiembre.")
        case 10:
            print("es el mes de octubre.")
        case 11:
            print("es el mes de noviembre.")
        case 12:
            print("es el mes de diciembre.")

def imprimir_resultado():
    print("el programa finaliza.")

#*** codigo principal ***

num= definir_numero()
procesar_resultado(num)
imprimir_resultado()