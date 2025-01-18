import os

class Config:
    """Configuración base para la aplicación."""
    # URI de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "mysql+pymysql://root:@localhost/hotelbook"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_por_defecto'


