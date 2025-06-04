from flask import Flask
from flask_cors import CORS
from .proveedor.proveedor_routes import proveedor_bp
from .marca.marca_routes import marca_bp
from .categoria.categoria_routes import categoria_bp
from app.articulos.articulo_routes import articulo_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(proveedor_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(articulo_bp)

    @app.route("/")
    def home():
        return "<h1>Bienvenido a la app PWD2025</h1>"

    return app
