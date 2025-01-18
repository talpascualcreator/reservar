from database import db  # Importa el objeto db desde el archivo database.py



# Tabla Clientes
class Cliente(db.Model):
    __tablename__ = 'clientes'
    cliente_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    direccion = db.Column(db.String(200), nullable=True)

    # Relación con Reservas
    reservas = db.relationship('Reserva', backref='cliente', lazy=True)

# Tabla Habitaciones
class Habitacion(db.Model):
    __tablename__ = 'habitaciones'
    habitacion_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50), nullable=False)  # Ej. Estándar, Suite
    precio_por_noche = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(50), nullable=False)  # Ej. Disponible, Reservada
    capacidad = db.Column(db.Integer, nullable=False)
    detalles_adicionales = db.Column(db.String(200), nullable=True)

    # Relación con Reservas
    reservas = db.relationship('Reserva', backref='habitacion', lazy=True)

# Tabla Reservas
class Reserva(db.Model):
    __tablename__ = 'reservas'
    reserva_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.cliente_id'), nullable=False)
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitaciones.habitacion_id'), nullable=False)
    fecha_reserva = db.Column(db.DateTime, nullable=False)
    fecha_checkin = db.Column(db.Date, nullable=False)
    fecha_checkout = db.Column(db.Date, nullable=False)
    estado_reserva = db.Column(db.String(50), nullable=False)  # Confirmada, Cancelada
    precio_total = db.Column(db.Float, nullable=False)
    notas = db.Column(db.Text, nullable=True)

    # Relación con Pagos y Cancelaciones
    pagos = db.relationship('Pago', backref='reserva', lazy=True)
    cancelaciones = db.relationship('Cancelacion', backref='reserva', lazy=True)

# Tabla Pagos
class Pago(db.Model):
    __tablename__ = 'pagos'
    pago_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.reserva_id'), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha_pago = db.Column(db.DateTime, nullable=False)
    metodo_pago = db.Column(db.String(50), nullable=False)  # Tarjeta, PayPal
    estado_pago = db.Column(db.String(50), nullable=False)  # Pagado, Pendiente

# Tabla Cancelaciones
class Cancelacion(db.Model):
    __tablename__ = 'cancelaciones'
    cancelacion_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.reserva_id'), nullable=False)
    fecha_cancelacion = db.Column(db.DateTime, nullable=False)
    razon_cancelacion = db.Column(db.Text, nullable=True)
    monto_reembolso = db.Column(db.Float, nullable=True)


