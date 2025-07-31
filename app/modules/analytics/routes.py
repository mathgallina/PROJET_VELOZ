"""
Wiki Veloz Fibra - Analytics Routes
Rotas para analytics e relatórios

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Create blueprint
analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/')
@login_required
def index():
    """Dashboard de analytics"""
    # Simulate analytics data
    stats = {
        'total_pages': 15,
        'total_documents': 42,
        'total_users': 8,
        'total_backups': 12,
        'storage_used': '2.3 GB',
        'storage_available': '47.7 GB'
    }
    
    return render_template('analytics/index.html', stats=stats)
