"""
Wiki Veloz Fibra - Users Routes
Rotas para gerenciamento de usuários

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

# Create blueprint
users_bp = Blueprint('users', __name__)

@users_bp.route('/')
@login_required
def index():
    """Lista de usuários (apenas admin)"""
    if not current_user.is_admin():
        return redirect(url_for('main.index'))
    
    # Simulate users data
    users = [
        {
            'id': 1,
            'username': 'admin',
            'name': 'Administrador',
            'role': 'admin',
            'email': 'admin@velozfibra.com',
            'created_at': '2024-01-01 00:00',
            'is_active': True
        },
        {
            'id': 2,
            'username': 'user1',
            'name': 'João Silva',
            'role': 'user',
            'email': 'joao@velozfibra.com',
            'created_at': '2024-01-05 10:30',
            'is_active': True
        },
        {
            'id': 3,
            'username': 'user2',
            'name': 'Maria Santos',
            'role': 'user',
            'email': 'maria@velozfibra.com',
            'created_at': '2024-01-10 14:15',
            'is_active': True
        }
    ]
    
    return render_template('users/index.html', users=users)

@users_bp.route('/profile')
@login_required
def profile():
    """Perfil do usuário atual"""
    return render_template('users/profile.html')
