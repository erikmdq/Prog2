############## Programación 2 ##############
############## Trabajo práctico 1 ##############

############## EJERCICIO 1 ##############

def realizar_calculo():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == '+':
            resultado = numero1 + numero2
        elif operacion == '-':
            resultado = numero1 - numero2
        elif operacion == '*':
            resultado = numero1 * numero2
        elif operacion == '/':
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                print("Error: División por cero no permitida.")
                return
        else:
            print("Operación no válida.")
            return

        print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")

    except ValueError:
        print("Error: Por favor ingrese números válidos.")

realizar_calculo()


############## EJERCICIO 2 ##############

def numero_en_orden_ascendente(numero):
  num = str(numero)
  for i in range(len(num) - 1):
    actual = int(num[i])
    siguiente = int(num[i+1])
    if actual > siguiente:
      return False

  return True

print(numero_en_orden_ascendente(12))
print(numero_en_orden_ascendente(21))
print(numero_en_orden_ascendente(583))
print(numero_en_orden_ascendente(248))

############## EJERCICIO 3 ##############

def numeros_impares_juntos(entrada):
  salida = []
  for n in str(entrada):
    if int(n) % 2 != 0:
      salida.append(n)
  return(",".join(salida))

print(numeros_impares_juntos(23679643))

#Otra forma de resolverlo podría ser utilizando comprensión de listas:#

def numeros_impares_juntos(entrada):
    return ",".join(d for d in str(entrada) if int(d) % 2 != 0)

print(numeros_impares_juntos(23679643))

############## EJERCICIO 4 ##############

def lista_elementos_en_comun(lista1, lista2):
  salida = []
  for n in lista1:
    if n in lista2 and n not in salida:
        salida.append(n)
  return salida

print(lista_elementos_en_comun("16864849841", "26841568468"))

############## EJERCICIO 5 ##############

def clave_valida(clave):
  if not(len(clave) >= 6 and len(clave) <= 20):
    return False

  if " " in clave:
    return False

  tiene_numero = False
  for caracter in clave:
      if caracter.isdigit():
          tiene_numero = True
          break
  if not tiene_numero:
    return False

  return True

print(clave_valida("hy4eh"))
print(clave_valida("hy4eo efgeg"))
print(clave_valida("hy4eogbfgh"))

############## EJERCICIO 6 ##############

def persona_mayor_de_edad(edad):
  return edad >= 18

print(persona_mayor_de_edad(12))
print(persona_mayor_de_edad(20))

############## EJERCICIO 7 ##############

def declarar_comida_favorita(nombre_persona, nombre_comida):
    print(f"La comida favorita de {nombre_persona} se llama: {nombre_comida}")

# Uso del procedimiento para mejorar la legibilidad
declarar_comida_favorita("Pablo", "pollo frito")
declarar_comida_favorita("Pedro", "canelones")
declarar_comida_favorita("Juan", "pizza")

############## EJERCICIO 8 ##############

from impresiones import declarar_comida_favorita

declarar_comida_favorita("Pablo", "pollo frito")
declarar_comida_favorita("Pedro", "canelones")

############## EJERCICIO 9 ##############

def cuenta_regresiva(entero_positivo):
  print(entero_positivo)

  if entero_positivo == 0:
    return

  cuenta_regresiva(entero_positivo - 1)

cuenta_regresiva(10)

############## EJERCICIO 10 ##############

#
#(a and b) or True  = True
#
#Cualquier expresión evaluada con un OR donde uno de los valores sea True, dará como resultado True. Por lo tanto la expresión se puede simplificar a True.
#
