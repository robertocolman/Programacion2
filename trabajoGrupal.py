from impresiones import *

#Escribir un método realizar_calculo(). El mismo debe solicitar al usuario seleccionar por consola la operación matemática deseada (opciones: suma, resta, multiplicación, y división). Luego, debe solicitar que se ingresen 2 números. Por último, debe imprimir el resultado. Asumir que los valores ingresados son del tipo de datos correcto.

def realizar_calculo():
    operacion = input("Que operacion desea realizar?: ")

    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))

    if operacion == "suma":
        res = num1 + num2
    elif operacion == "resta":
        res = num1 - num2
    elif operacion == "multiplicacion":
        res = num1 * num2
    elif operacion == "division":
        if num2 == 0:
            print("no se puede dividir por ser")
            return
        res = num1 / num2
    else:
        print("no es valido la opcion")
        return

    if res.is_integer(): 
        print(f"resultado es {int(res)}") 
    else:
        print(f"resultado es {res}") 
        
realizar_calculo()

#2. Escribir una función numero_en_orden_ascendente (numero) que retorne True si los dígitos del número están ordenados de menor a mayor, y False en caso contrario.

def numero_en_orden_ascendente(numero):
    digitos = str(numero)
    for i in range(len(digitos) - 1):
        if int(digitos[i]) > int(digitos[i+1]):
            return False
    return True

print(numero_en_orden_ascendente(1234))

#3. Escribir un método numeros_impares_juntos(entrada) que, dada una lista de números, concatene los números impares en un string, separados por coma.

def numeros_impares_juntos(entrada):
    impares = []
    for num in entrada:
        if num % 2 != 0: 
            impares.append(str(num)) 
    return ",".join(impares)

#4 Escribir un método lista_elementos_en_comun(lista1, lista2) que imprima los elementos en común que tienen las listas sin repetirlos.

def lista_elementos_en_comun(lista1, lista2):
    comunes = set(lista1) & set(lista2)
    print("Elementos en común:", list(comunes))

#Escribir una función clave_valida(clave) que devuelva True en caso de superar las siguientes validaciones sobre la clave proporcionada por el usuario: a. Longitud entre 6 y 20 caracteres. b. Debe contener al menos un número. c. No puede contener espacios.

def clave_valida(clave):
    if len(clave) < 6 or len(clave) > 20:
        return False
    if not any(c.isdigit() for c in clave):
        return False
    if " " in clave:
        return False
    return True

# Reescribir la siguiente función eliminando la sentencia if/else: def persona_mayor_de_edad(edad): if edad >= 18: return True else: return False

def persona_mayor_de_edad(edad): 
    if edad >= 18: 
        return True 
    else: 
        return False
    
# Dado el siguiente script, escriba una función declarar_comida_favorita(nombre_persona, nombre_comida) con el fin de mejorar la legibilidad del mismo. nombre = "Pablo" comida_favorita = "pollo frito" print("La comida favorita de " + nombre + " se llama: " + comida_favorita) nombre = "Pedro" comida_favorita = "canelones" print("La comida favorita de " + nombre + " se llama: " + comida_favorita) nombre = "Juan" comida_favorita = "pizza" print("La comida favorita de " + nombre + " se llama: " + comida_favorita)

declarar_comida_favorita("Pablo", "pollo frito")

# 9. Escribir una función cuenta_regresiva(entero_positivo) que imprima números enteros empezando por el valor pasado por parámetro y llegando hasta 0. Asumir que el número pasado por parámetro es un número entero positivo. Utilizar recursividad para desarrollar la solución.

def cuenta_regresiva(entero_positivo):
    if entero_positivo < 0:
        return
    print(entero_positivo)
    if entero_positivo > 0:
        cuenta_regresiva(entero_positivo - 1)

cuenta_regresiva(5)

# 10. Simplificar la siguiente expresión: (a and b) or True

a = False
b = False
print((a and b) or True)