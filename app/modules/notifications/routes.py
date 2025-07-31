"""
Wiki Veloz Fibra - Notifications Routes
Rotas para gerenciamento de notificações

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Create blueprint
notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/')
@login_required
def index():
    """Lista de notificações"""
    # Simulate notifications data
    notifications = [
        {
            'id': 1,
            'title': 'Backup Concluído',
            'message': 'Backup automático foi concluído com sucesso',
            'type': 'success',
            'created_at': '2024-01-15 14:30',
            'read': False
        },
        {
            'id': 2,
            'title': 'Nova Página Criada',
            'message': 'Página "Configuração de Rede" foi criada',
            'type': 'info',
            'created_at': '2024-01-15 13:20',
            'read': True
        },
        {
            'id': 3,
            'title': 'Documento Enviado',
            'message': 'Manual técnico foi enviado para backup',
            'type': 'warning',
            'created_at': '2024-01-15 12:00',
            'read': True
        }
    ]
    
    return render_template('notifications/index.html', notifications=notifications)
