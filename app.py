from flask import Flask, render_template, request, redirect, session
import csv
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesario para usar session

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        correo = request.form['correo']
        codigo = request.form['codigo']
        telefono = request.form['telefono']

        # Guardamos los datos temporalmente en sesión
        session['correo'] = correo
        session['codigo'] = codigo
        session['telefono'] = telefono

        # Guarda en archivo CSV
        with open('usuarios.csv', 'a', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([correo, codigo, telefono])

        return redirect('/pagos')
    return render_template('registro.html')

@app.route('/pagos')
def pagos():
    codigo = session.get('codigo', '')
    descuento = 0.20 if codigo == 'SKYPREMIUM20' else 0.0  # Código de descuento válido
    return render_template('pagos.html', descuento=descuento)

if __name__ == '__main__':
    app.run(debug=True)
