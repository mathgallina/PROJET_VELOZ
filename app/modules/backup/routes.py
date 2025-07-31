"""
Wiki Veloz Fibra - Backup Routes
Rotas para gerenciamento de backup

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

# Create blueprint
backup_bp = Blueprint('backup', __name__)

@backup_bp.route('/')
@login_required
def index():
    """Lista de backups"""
    # Simulate backup data
    backups = [
        {
            'id': 1,
            'name': 'Backup Completo',
            'type': 'Completo',
            'size': '156 MB',
            'status': 'Concluído',
            'created_at': '2024-01-15 14:30'
        },
        {
            'id': 2,
            'name': 'Backup Incremental',
            'type': 'Incremental',
            'size': '23 MB',
            'status': 'Concluído',
            'created_at': '2024-01-14 09:15'
        },
        {
            'id': 3,
            'name': 'Backup de Documentos',
            'type': 'Documentos',
            'size': '89 MB',
            'status': 'Em andamento',
            'created_at': '2024-01-13 16:45'
        }
    ]
    
    return render_template('backup/index.html', backups=backups)

@backup_bp.route('/create')
@login_required
def create():
    """Criar novo backup"""
    return render_template('backup/create.html')
