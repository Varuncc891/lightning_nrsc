# CORE SECURITY
SECRET_KEY = "superset_311_local_dev_secret_key_123456"
from flask_appbuilder.security.manager import AUTH_DB

AUTH_TYPE = AUTH_DB

# Assign Public role to anonymous users
AUTH_ROLE_PUBLIC = "Public_View_Only"

# Initialize Public role with base Superset permissions
TALISMAN_ENABLED = False
PREFERRED_URL_SCHEME = "http"
ENABLE_PROXY_FIX = True


# FEATURE FLAGS
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}


# DECK.GL MAP SETTINGS
DECKGL_BASE_MAP = [
    ['tile://http://localhost:5000/tiles/{z}/{x}/{-y}.jpg', 'Bhuvan Vector (-y)'],
    ['tile://http://localhost:5000/tiles_sat/{z}/{x}/{y}.jpg', 'Bhuvan Satellite (y)'],
    ['tile://https://tile.openstreetmap.org/{z}/{x}/{y}.png', 'OpenStreetMap'],
    ['tile://https://cartodb-basemaps-a.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', 'CartoDB Positron'],
]

DECK_GL_DEFAULT_VIEWPORT = {
    "latitude": 20.0,
    "longitude": 78.0,
    "zoom": 4.0,
    "pitch": 0,
    "bearing": 0,
    "maxZoom": 20,
    "minZoom": 1
}

DECK_GL_AUTO_ZOOM = False


# CORS
ENABLE_CORS = True
CORS_OPTIONS = {
    "origins": [
        "https://c.tile.openstreetmap.org",
        "http://localhost:5000"
    ]
}


# CSRF (Disabled only for local dev)
WTF_CSRF_ENABLED = False

# CONTENT SECURITY POLICY (LOCAL ONLY)
CONTENT_SECURITY_POLICY = {
    'default-src': ["'self'"],
    'style-src': ["'self'", "'unsafe-inline'"],
    'script-src': ["'self'"],
    'img-src': ["'self'", "data:", "http://localhost:5001"],
    'font-src': ["'self'"],
    'connect-src': ["'self'"]
}


# DATABASE

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres123@localhost:5432/superset_metadata'
PREVENT_UNSAFE_DB_CONNECTIONS = False
