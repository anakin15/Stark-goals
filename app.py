from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
import os  # <-- Importamos os para leer variables de entorno

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pago', methods=['POST'])
def pago():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    telefono = request.form.get('telefono')
    telegram = request.form.get('telegram')
    plan = request.form.get('plan')
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('pagos.csv', mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([fecha, nombre, correo, telefono, telegram, plan])

    return redirect(url_for('exito'))

@app.route('/exito')
def exito():
    return render_template('exito.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto que Render asigna
    app.run(host='0.0.0.0', port=port)
