import os
from dotenv import load_dotenv
load_dotenv()

# Server Config
PORT = int(os.getenv("PORT", 8080))

PRODUCTION=os.getenv("PRODUCTION", False)

# DB Config
DB_CONFIG = {
        'driver': 'postgresql',
        'username': os.getenv("DB_USER", 'root'),
        'password': os.getenv("DB_PASSWORD", ''),
        'host': os.getenv("DB_HOST", 'localhost'),
        'port': os.getenv("DB_PORT", 5432),
        'db_name': os.getenv("DB_NAME", 5432)
    }

# SQLALCHEMY Config
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = DB_CONFIG['driver']+'://'+DB_CONFIG['username']+':'+DB_CONFIG['password']+'@'+DB_CONFIG['host']+':'+DB_CONFIG['port']+'/'+DB_CONFIG['db_name']
