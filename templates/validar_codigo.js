function validarCodigo() {
  const input = document.getElementById("codigo");
  const resultado = document.getElementById("resultado");
  const codigoIngresado = input.value.toUpperCase(); // Convierte a mayúsculas

  fetch("codigos_promocionales.json")
    .then(respuesta => {
      if (!respuesta.ok) {
        throw new Error("No se pudo cargar el archivo de códigos.");
      }
      return respuesta.json();
    })
    .then(codigos => {
      if (codigoIngresado in codigos) {
        const descuento = codigos[codigoIngresado]; // Ej: 0.2
        const precioOriginal = 25000;
        const precioFinal = precioOriginal * (1 - descuento);

        resultado.textContent = `✅ Código válido. Descuento aplicado: ${descuento * 100}%. Precio final: $${precioFinal.toFixed(0)} COP`;
      } else {
        resultado.textContent = "❌ Código no válido.";
      }
    })
    .catch(error => {
      console.error(error);
      resultado.textContent = "⚠️ Error al validar el código.";
    });
    }
