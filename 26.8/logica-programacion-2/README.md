# Conversor de Temperatura (Celsius → Fahrenheit y Kelvin)

## Luis Angel Hernandez Martinez

### 26/08/2026

Programa en JavaScript que solicita al usuario una temperatura en grados Celsius, valida que el dato ingresado sea numérico, y calcula su equivalente en **Fahrenheit** y **Kelvin**.

## 📋 Descripción

El programa cuenta con dos formas de uso:

1. **Interfaz web (HTML + input):** un formulario simple donde el usuario escribe la temperatura y presiona un botón para convertirla.
2. **Versión por consola (prompt):** una función alternativa que solicita el dato mediante `prompt()` del navegador y muestra el resultado por `console.log()` y `alert()`.

Ambas versiones comparten la misma lógica de conversión y validación de datos.

## 🚀 Cómo usarlo

1. Descarga el archivo `conversor_temperatura.html`.
2. Ábrelo con cualquier navegador (doble clic o "Abrir con").
3. Escribe una temperatura en el campo de texto y presiona **Convertir**.
4. Los resultados se muestran en pantalla.

### Usar la versión por `prompt()`

Si prefieres la versión por consola con ventanas emergentes:

1. Abre el archivo `conversor_temperatura.html` en el navegador.
2. Abre la consola de desarrollador (F12).
3. Ejecuta manualmente:
   ```js
   pedirTemperaturaPorPrompt();
   ```
   O bien, descomenta esta línea dentro del `<script>` del archivo:
   ```js
   // pedirTemperaturaPorPrompt();
   ```

## 🧮 Fórmulas utilizadas

| Conversión           | Fórmula              |
| -------------------- | -------------------- |
| Celsius → Kelvin     | `K = C + 273.15`     |
| Celsius → Fahrenheit | `F = (C × 9/5) + 32` |

## ✅ Validación de datos

- El programa verifica que el valor ingresado sea numérico usando `isNaN()`.
- Si el usuario ingresa un valor no numérico (texto, vacío, símbolos, etc.), se muestra un mensaje de error y se le vuelve a solicitar el dato:
  - En la versión web: mediante un mensaje en pantalla y limpiando el campo de entrada.
  - En la versión por `prompt()`: mediante un bucle `while` que repite la solicitud hasta recibir un valor válido.

## 🧪 Pruebas realizadas

| Entrada (°C) | Kelvin esperado | Fahrenheit esperado | Resultado   |
| ------------ | --------------- | ------------------- | ----------- |
| 45           | 318.15          | 113.00              | ✅ Correcto |
| 14           | 287.15          | 57.20               | ✅ Correcto |

Estas pruebas se ejecutan automáticamente al cargar el archivo HTML y los resultados pueden verse en la consola del navegador (F12 → pestaña _Console_).

## 📁 Estructura del proyecto

```
├── conversor_temperatura.html   # Programa principal (HTML + JS)
└── README.md                    # Este archivo
```

## 🛠️ Tecnologías

- HTML5
- JavaScript (Vanilla, sin librerías externas)

## 📌 Notas

- La función `convertirTemperatura(celsius)` es independiente de la interfaz (pura), lo que permite reutilizarla o probarla fácilmente en otros contextos.
- No requiere instalación ni dependencias: solo un navegador web.
