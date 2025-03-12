# Archivo app.py (Flask backend)
from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Página principal para registro
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('empleados.db')
    c = conn.cursor()
    empleados = c.execute('SELECT * FROM empleados').fetchall()

    if request.method == 'POST':
        empleado_id = request.form['empleado']
        tipo_registro = request.form['tipo_registro']
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        c.execute('INSERT INTO registros_horarios (id_empleado, tipo_registro, fecha_hora) VALUES (?, ?, ?)',
                  (empleado_id, tipo_registro, fecha_hora))
        conn.commit()
        conn.close()

        return redirect('/')

    conn.close()
    return render_template('index.html', empleados=empleados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)