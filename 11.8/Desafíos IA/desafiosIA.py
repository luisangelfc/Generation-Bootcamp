"""
Desafíos IA - Nivel 1
Generation:You Employed

Este archivo contiene las tres soluciones de los Desafíos de Nivel 1:
1. Eliminar Duplicados de un Array
2. Verificador de Palíndromos
3. Revisión de Código: máximo/mínimo y longitud de cadena sin funciones integradas

Sugerencia de uso (según la metodología del desafío):
- Primero, intenta resolver cada función por tu cuenta, SIN mirar el código de abajo.
- Luego compara tu solución con esta, o pídele a una herramienta de IA que la revise/optimice.
- Anota cuánto tiempo tardaste con y sin IA, y qué diferencias notaste en precisión o
  legibilidad, para la sección de Reflexión.
"""


# ---------------------------------------------------------------------------
# 1. Eliminar Duplicados de un Array
# ---------------------------------------------------------------------------
def eliminar_duplicados(arr):
    """Devuelve una nueva lista con los elementos únicos, conservando el orden
    de la primera aparición."""
    vistos = set()
    resultado = []
    for elemento in arr:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    return resultado


# ---------------------------------------------------------------------------
# 2. Verificador de Palíndromos
# ---------------------------------------------------------------------------
def es_palindromo(valor):
    """Verifica si una cadena o número se lee igual hacia adelante que hacia
    atrás. Ignora mayúsculas/minúsculas y espacios en el caso de texto."""
    texto = str(valor).lower().replace(" ", "")
    return texto == texto[::-1]


# ---------------------------------------------------------------------------
# 3. Revisión de Código: máximo/mínimo y longitud sin funciones integradas
# ---------------------------------------------------------------------------
def encontrar_maximo(arr):
    """Encuentra el valor máximo de un array sin usar max()."""
    if not arr:
        raise ValueError("El array no puede estar vacío")
    maximo = arr[0]
    for elemento in arr[1:]:
        if elemento > maximo:
            maximo = elemento
    return maximo


def encontrar_minimo(arr):
    """Encuentra el valor mínimo de un array sin usar min()."""
    if not arr:
        raise ValueError("El array no puede estar vacío")
    minimo = arr[0]
    for elemento in arr[1:]:
        if elemento < minimo:
            minimo = elemento
    return minimo


def longitud_cadena(cadena):
    """Determina la longitud de una cadena sin usar len()."""
    contador = 0
    for _ in cadena:
        contador += 1
    return contador


# ---------------------------------------------------------------------------
# Pruebas (incluye casos límite)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== 1. Eliminar Duplicados ===")
    casos_duplicados = [
        [1, 2, 2, 3, 4, 4, 4, 5],
        [],
        [7],
        ["a", "b", "a", "c", "b"],
    ]
    for caso in casos_duplicados:
        print(f"{caso} -> {eliminar_duplicados(caso)}")

    print("\n=== 2. Verificador de Palíndromos ===")
    casos_palindromos = ["reconocer", "Python", 12321, 123456, "Anita lava la tina"]
    for caso in casos_palindromos:
        print(f"{caso!r} -> {es_palindromo(caso)}")

    print("\n=== 3. Máximo, Mínimo y Longitud ===")
    arr_prueba = [3, 7, 1, 9, 4, -2, 9]
    print(f"Array: {arr_prueba}")
    print(f"Máximo -> {encontrar_maximo(arr_prueba)}")
    print(f"Mínimo -> {encontrar_minimo(arr_prueba)}")

    cadena_prueba = "Desafíos IA"
    print(f"Cadena: {cadena_prueba!r}")
    print(f"Longitud -> {longitud_cadena(cadena_prueba)}")