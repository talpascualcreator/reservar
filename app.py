import pymysql
from flask import Flask, request, render_template
from database import db  # Importa db desde database.py
from models_def import Cliente, Habitacion, Reserva, Pago, Cancelacion  # Importa las clases correspondientes
from config import Config  # Importa las configuraciones

app = Flask(__name__)

# Conexión a la base de datos (MySQL)
def get_db_connection():
    conn = pymysql.connect(
        host='localhost',        # Cambia esto por tu host de MySQL si es diferente
        user='root',             # Usuario de la base de datos
        password='',             # Contraseña de la base de datos
        database='hotelbook',    # Nombre de tu base de datos
        cursorclass=pymysql.cursors.DictCursor  # Utiliza un diccionario como cursor para acceder a las filas por nombre de columna
    )
    return conn

@app.route('/')
def index():
    return render_template('formulario.html')  # Asegúrate de que el formulario esté en templates

# Ruta para manejar el envío de datos de cliente
@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Inserción en la base de datos
        cursor.execute("INSERT INTO clientes (nombre, apellido, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellido, email, telefono, direccion))
        conn.commit()
        conn.close()
        
        # Renderiza formulario.html después de guardar el cliente
        return render_template('formulario.html')

# Ruta para manejar la adición de habitación
@app.route('/add_habitacion', methods=['POST'])
def add_habitacion():
    if request.method == 'POST':
        tipo = request.form['tipo']
        precio_por_noche = request.form['precio_por_noche']
        estado = request.form['estado']
        capacidad = request.form['capacidad']
        detalles_adicionales = request.form['detalles_adicionales']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO habitaciones (tipo, precio_por_noche, estado, capacidad, detalles_adicionales) VALUES (%s, %s, %s, %s, %s)",
                       (tipo, precio_por_noche, estado, capacidad, detalles_adicionales))
        conn.commit()
        conn.close()
        
        # Renderiza formulario.html después de guardar el habitacion
        return render_template('formulario.html')

@app.route('/add_reserva', methods=['POST'])
def add_reserva():
    if request.method == 'POST':
        cliente_id = request.form.get('cliente_id')  # Usamos get() en lugar de []
        habitacion_id = request.form.get('habitacion_id')
        fecha_reserva = request.form.get('fecha_reserva')
        fecha_checkin = request.form.get('fecha_checkin')
        fecha_checkout = request.form.get('fecha_checkout')
        estado_reserva = request.form.get('estado_reserva')
        precio_total = request.form.get('precio_total')
        notas = request.form.get('notas')
        
        # Verificación adicional para asegurarnos de que todos los campos sean recibidos
        if not all([cliente_id, habitacion_id, fecha_reserva, fecha_checkin, fecha_checkout, estado_reserva, precio_total]):
            return "Faltan campos requeridos", 400
        
        # Conexión a la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insertar datos en la base de datos
        cursor.execute("INSERT INTO reservas (cliente_id, habitacion_id, fecha_reserva, fecha_checkin, fecha_checkout, estado_reserva, precio_total, notas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (cliente_id, habitacion_id, fecha_reserva, fecha_checkin, fecha_checkout, estado_reserva, precio_total, notas))
        conn.commit()
        conn.close()
        
        # Renderiza formulario.html después de guardar la reserva
        return render_template('formulario.html')

# Ruta para manejar la adición de pagos
@app.route('/add_pago', methods=['POST'])
def add_pago():
    if request.method == 'POST':
        reserva_id = request.form['reserva_id']
        monto = request.form['monto']
        fecha_pago = request.form['fecha_pago']
        metodo_pago = request.form['metodo_pago']
        estado_pago = request.form['estado_pago']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO pagos (reserva_id, monto, fecha_pago, metodo_pago, estado_pago) VALUES (%s, %s, %s, %s, %s)",
                       (reserva_id, monto, fecha_pago, metodo_pago, estado_pago))
        conn.commit()
        conn.close()
        
        # Renderiza formulario.html después de guardar el pago
        return render_template('formulario.html')

# Ruta para manejar la adición de cancelaciones
@app.route('/add_cancelacion', methods=['POST'])
def add_cancelacion():
    if request.method == 'POST':
        reserva_id = request.form['reserva_id']
        fecha_cancelacion = request.form['fecha_cancelacion']
        razon_cancelacion = request.form['razon_cancelacion']
        monto_reembolso = request.form['monto_reembolso']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO cancelaciones (reserva_id, fecha_cancelacion, razon_cancelacion, monto_reembolso) VALUES (%s, %s, %s, %s)",
                       (reserva_id, fecha_cancelacion, razon_cancelacion, monto_reembolso))
        conn.commit()
        conn.close()
        
        # Renderiza formulario.html después de guardar el cancelacion
        
        return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)



