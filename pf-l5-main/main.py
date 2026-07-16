def addmultiplenumbers(numeros):
    # Variable acumuladora, empieza en 0 porque 0 es el "neutro" de la suma
    total = 0
    # Recorremos cada número de la lista uno por uno
    for numero in numeros:
        # Vamos sumando cada número al total acumulado
        total = total + numero
    # Devolvemos el resultado final de la suma
    return total


def multiplymultiplenumbers(numeros):
    # Variable acumuladora, empieza en 1 porque 1 es el "neutro" de la multiplicación
    resultado = 1
    # Recorremos cada número de la lista uno por uno
    for numero in numeros:
        # Vamos multiplicando el resultado acumulado por cada número
        resultado = resultado * numero
    # Devolvemos el resultado final de la multiplicación
    return resultado


def isiteven(num):
    # Un número es entero (whole number) si al dividirlo entre 1 no deja residuo
    # y es par si al dividirlo entre 2 el residuo es 0
    return num % 1 == 0 and num % 2 == 0


def isitaninteger(num):
    # Un número es entero si al dividirlo entre 1 no deja ningún residuo (resto == 0)
    return num % 1 == 0


def main():
    # Aquí va toda la lógica interactiva (inputs, prints al usuario, menú, etc.)
    print("Hello learners!")


if __name__ == "__main__":
    # Este bloque solo se ejecuta cuando alguien corre el archivo directamente,
    # no cuando el archivo se importa (como hace el test)
    main()