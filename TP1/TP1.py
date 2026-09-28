
############## Ejercicio 1 ##############
# %%
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


############## Ejercicio 2 ##############
# %%
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


