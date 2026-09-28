// Valida que la entrada sea un número entero mayor o igual a 0
function esNumeroValido(entrada) {
  if (entrada === null || entrada === undefined) return false;
  const texto = String(entrada).trim();
  if (texto === "") return false;
  const numero = Number(texto);
  return typeof numero === "number" && Number.isInteger(numero) && numero >= 0;
}

// Calcula el factorial (BigInt para no perder precisión con números grandes)
function factorial(n) {
  let resultado = 1n;
  for (let i = 2n; i <= BigInt(n); i++) {
    resultado *= i;
  }
  return resultado;
}

// Solicita el dato hasta que sea válido
function solicitarNumero() {
  while (true) {
    const entrada = prompt("Ingresa un número entero (0 o mayor):");

    // El usuario presionó "Cancelar"
    if (entrada === null) return null;

    if (esNumeroValido(entrada)) return Number(entrada);

    alert("Error: el dato ingresado no es un número entero válido. Intenta de nuevo.");
    console.error(`Entrada inválida: "${entrada}"`);
  }
}

function main() {
  const numero = solicitarNumero();
  if (numero === null) {
    console.log("Operación cancelada.");
    return;
  }
  console.log(`El factorial de ${numero} es: ${factorial(numero)}`);
}

// Se ejecuta en el navegador; en Node se exportan las funciones para pruebas
if (typeof prompt === "function") {
  main();
} else if (typeof module !== "undefined") {
  module.exports = { esNumeroValido, factorial };
}