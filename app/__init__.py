"""
Wiki Veloz Fibra - Flask Application Factory
Clean and modular Flask application

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

import os
import logging
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app(config_name=None):
    """
    Application factory pattern for Flask
    """
    app = Flask(__name__, template_folder='templates')
    
    # Configuration
    app.config.from_object('app.core.config.Config')
    
    # Initialize extensions
    initialize_extensions(app)
    
    # Register blueprints
    register_blueprints(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    logger.info("Aplicação Flask criada com sucesso")
    return app

def initialize_extensions(app):
    """Initialize Flask extensions"""
    # CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'info'
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.modules.auth.models.user import User
        return User.get_by_id(user_id)
    
    logger.info("Extensões Flask inicializadas")

def register_blueprints(app):
    """Register Flask blueprints"""
    from app.modules.auth.routes import auth_bp
    from app.modules.main.routes import main_bp
    from app.modules.pages.routes import pages_bp
    from app.modules.documents.routes import documents_bp
    from app.modules.backup.routes import backup_bp
    from app.modules.analytics.routes import analytics_bp
    from app.modules.notifications.routes import notifications_bp
    from app.modules.pdfs.routes import pdfs_bp
    from app.modules.users.routes import users_bp
    from app.modules.goals.routes import goals_bp
    from app.modules.hr.routes import hr_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(pages_bp, url_prefix='/pages')
    app.register_blueprint(documents_bp, url_prefix='/documents')
    app.register_blueprint(backup_bp, url_prefix='/backup')
    app.register_blueprint(analytics_bp, url_prefix='/analytics')
    app.register_blueprint(notifications_bp, url_prefix='/notifications')
    app.register_blueprint(pdfs_bp, url_prefix='/pdfs')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(goals_bp, url_prefix='/goals')
    app.register_blueprint(hr_bp, url_prefix='/hr')
    
    logger.info("Blueprints registrados")

def register_error_handlers(app):
    """Register error handlers"""
    @app.errorhandler(404)
    def not_found_error(error):
        return {'error': 'Página não encontrada'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Erro interno do servidor'}, 500
    
    logger.info("Handlers de erro registrados")
