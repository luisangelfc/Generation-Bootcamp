numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es:", resultado)

print("\n--- Funciones extra ---\n")

resta = numero1 - numero2
print("Resta:", resta)

multiplicacion = numero1 * numero2
print("Multiplicación:", multiplicacion)

if numero2 != 0:
    division = numero1 / numero2
    print("División:", division)
else:
    print("División: no se puede dividir entre 0")

if numero2 != 0:
    modulo = numero1 % numero2
    print("Módulo:", modulo)
else:
    print("Módulo: no se puede calcular con divisor 0")

print("\n--- Elige una operación ---")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Módulo")

op = input("Elige una opción (1-5): ")

if op == "1":
    print("Resultado:", numero1 + numero2)
elif op == "2":
    print("Resultado:", numero1 - numero2)
elif op == "3":
    print("Resultado:", numero1 * numero2)
elif op == "4":
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("No se puede dividir entre 0")
elif op == "5":
    if numero2 != 0:
        print("Resultado:", numero1 % numero2)
    else:
        print("No se puede calcular módulo con divisor 0")
else:
    print("Opción no válida")

print("\n--- Suma de 3 números ---")
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
print("Suma total:", n1 + n2 + n3)

print("\n--- Mezcla de operaciones con 3+ números ---")
print("Ejemplo de formato: 2 + 4 - 3")
expresion = input("Escribe tu expresión: ")
resultado_expresion = eval(expresion)
print("Resultado:", resultado_expresion)