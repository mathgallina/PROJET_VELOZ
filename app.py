"""
Wiki Veloz Fibra - Main Application Entry Point
Clean and modular Flask application

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

import os
import logging

from app import create_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # Configuration
    port = int(os.environ.get("PORT", 8001))
    debug = os.environ.get("FLASK_DEBUG", "True").lower() == "true"
    host = os.environ.get("FLASK_HOST", "0.0.0.0")
    
    logger.info(f"Iniciando servidor Flask na porta {port}")
    logger.info(f"Debug mode: {debug}")
    logger.info(f"Host: {host}")
    logger.info(f"Acesse: http://localhost:{port}")
    
    # Run the application
    app.run(debug=debug, host=host, port=port)
