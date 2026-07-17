import requests

def trivia_fetch(num):
    respuesta = requests.get(f"http://numbersapi.com/{num}?json")
    print("Status code:", respuesta.status_code)
    print("Contenido crudo:", respuesta.text)
    datos = respuesta.json()
    return datos

def main():
    numero = int(input("Ingresa un número para conocer su trivia: "))
    resultado = trivia_fetch(numero)
    print(resultado["text"])

if __name__=="__main__":
    main()


def trivia_fetch(num):
    trivia = {}
    trivia["number"] = num
    trivia["is_even"] = num % 2 == 0
    trivia["is_negative"] = num < 0

    if num == 0:
        trivia["text"] = "0 es el elemento neutro de la suma."
    elif num % 2 == 0:
        trivia["text"] = f"{num} es un número par."
    else:
        trivia["text"] = f"{num} es un número impar."

    return trivia

def main():
    numero = int(input("Ingresa un número para conocer su trivia: "))
    resultado = trivia_fetch(numero)
    print(resultado["text"])

if __name__=="__main__":
    main()