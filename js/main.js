// Espera a que cargue todo el contenido
document.addEventListener('DOMContentLoaded', () => {
  const nombreUsuario = document.getElementById('nombreUsuario');
  const precioOriginal = document.getElementById('precioOriginal');
  const precioConDescuento = document.getElementById('precioConDescuento');

  // Obtener datos guardados en localStorage
  const nombre = localStorage.getItem('nombre');
  const correo = localStorage.getItem('correo');
  const promocion = localStorage.getItem('promocion');

  // Mostrar el nombre
  if (nombre) {
    nombreUsuario.textContent = nombre;
  }

  // Verificar si hay código promocional y aplicar descuento
  if (promocion && promocion.toLowerCase() === "vipdaniel") {
    const precioConDescuentoValor = 20000;
    precioConDescuento.textContent = `Con descuento: $${precioConDescuentoValor.toLocaleString()} COP`;
    precioConDescuento.style.color = "green";
    precioOriginal.style.textDecoration = "line-through";
  } else {
    precioConDescuento.textContent = "";
    precioOriginal.style.textDecoration = "none";
  }
});

// Funciones para pago
function pagarNequi() {
  const nombre = localStorage.getItem('nombre') || "Usuario";
  const promocion = localStorage.getItem('promocion') || "";
  let mensaje = `Hola, soy ${nombre}.\nRealicé el pago por Nequi para el Plan VIP.`;

  if (promocion.toLowerCase() === "vipdaniel") {
    mensaje += "\nUsé el código promocional VIPDANIEL.";
  }

  alert("Realiza el pago a este número Nequi: 3117776320\nDespués de pagar, serás redirigido.");
  window.location.href = "gracias.html";
}

function pagarDaviplata() {
  const nombre = localStorage.getItem('nombre') || "Usuario";
  const promocion = localStorage.getItem('promocion') || "";
  let mensaje = `Hola, soy ${nombre}.\nRealicé el pago por Daviplata para el Plan VIP.`;

  if (promocion.toLowerCase() === "vipdaniel") {
    mensaje += "\nUsé el código promocional STARKBET.";
  }

  alert("Realiza el pago a este número Daviplata: 3117776320\nDespués de pagar, serás redirigido.");
  window.location.href = "gracias.html";
}
