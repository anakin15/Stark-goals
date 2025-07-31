from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

# Configuración
CODIGO_DESC = "STARKBET"
USOS_MAX = 20
ARCHIVO_USUARIOS = "codigos_usados.json"

# Precios normales
precios_base = {
    "mensual": 65.000,
    "trimestral": 177.000,
    "semestral": 390.000,
    "anual": 790.000
}

# Links de pago (AstroPay)
links = {
    "mensual": "https://onetouch.astropay.com/payment?external_reference_id=yQhLPb2z0AxcipNOmAz9PMvcclXU1yU9",
    "trimestral": "https://onetouch.astropay.com/payment?external_reference_id=FIKYIzFSVKBBtyb8nXc5RxBOia5SwsQJ",
    "semestral": "https://onetouch.astropay.com/payment?external_reference_id=dlrDIgquJRYEFAHZkN3wipC3Y8ekQHGV",
    "anual": "https://onetouch.astropay.com/payment?external_reference_id=TByrspBzhDYFcCYSvXoqq8s04YBvb7YO"
}

# Información de contacto
contacto = {
    "whatsapp": "https://wa.me/573117776320",
    "telegram": "https://t.me/StarkPadilla",
    "paypal_correo": "danielpadilla152018@gmail.com"
}

# Funciones para manejo de correos
def cargar_usuarios():
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as f:
            return json.load(f)
    return []

def guardar_usuario(correo):
    correos = cargar_usuarios()
    correos.append(correo)
    with open(ARCHIVO_USUARIOS, "w") as f:
        json.dump(correos, f)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    precios = precios_base.copy()
    correos_usados = cargar_usuarios()
    mensaje = ""
    clase = ""
    descuento_aplicado = False

    if request.method == 'POST':
        correo = request.form.get('correo', '').strip().lower()
        codigo = request.form.get('codigo', '').strip().upper()

        if correo in correos_usados:
            mensaje = "⚠️ Ya usaste el descuento anteriormente."
            clase = "error"
        elif codigo == CODIGO_DESC and len(correos_usados) < USOS_MAX:
            for k in precios:
                precios[k] = int(precios[k] * 0.8)
            guardar_usuario(correo)
            mensaje = "✅ ¡Descuento aplicado correctamente!"
            clase = "ok"
            descuento_aplicado = True

    # Formatear precios con puntos
    precios_format = {k: "{:,.0f}".format(v).replace(",", ".") for k, v in precios.items()}

    return render_template("index.html",
                           mensaje=mensaje,
                           clase=clase,
                           precios=precios_format,
                           links=links,
                           contacto=contacto)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
