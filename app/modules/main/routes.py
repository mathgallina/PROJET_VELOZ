"""
Wiki Veloz Fibra - Main Routes
Rotas principais do sistema

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Create blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    """Dashboard principal"""
    # Simulate dashboard data
    stats = {
        'pages': 15,
        'documents': 42,
        'users': 8,
        'backups': 12
    }
    
    recent_pages = [
        {
            'id': 1,
            'title': 'Configuração de Rede',
            'category': 'Técnico',
            'updated_at': '2024-01-15 14:30'
        },
        {
            'id': 2,
            'title': 'Procedimentos de Backup',
            'category': 'Administrativo',
            'updated_at': '2024-01-14 09:15'
        },
        {
            'id': 3,
            'title': 'Manual do Usuário',
            'category': 'Documentação',
            'updated_at': '2024-01-13 16:45'
        }
    ]
    
    recent_activity = [
        {
            'title': 'Página criada',
            'description': 'Nova página "Configuração de Rede" foi criada',
            'created_at': '2024-01-15 14:30'
        },
        {
            'title': 'Documento enviado',
            'description': 'Manual técnico foi enviado para backup',
            'created_at': '2024-01-15 13:20'
        },
        {
            'title': 'Usuário logado',
            'description': 'Administrador fez login no sistema',
            'created_at': '2024-01-15 12:00'
        }
    ]
    
    return render_template('main/index.html', 
                         stats=stats,
                         recent_pages=recent_pages,
                         recent_activity=recent_activity)

@main_bp.route('/about')
def about():
    """Sobre o sistema"""
    return render_template('main/about.html')

@main_bp.route('/help')
@login_required
def help():
    """Página de ajuda"""
    return render_template('main/help.html')
