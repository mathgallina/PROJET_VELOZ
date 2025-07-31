"""
Wiki Veloz Fibra - Pages Routes
Rotas para gerenciamento de páginas

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

# Create blueprint
pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
@login_required
def index():
    """Lista de páginas"""
    # Simulate pages data
    pages = [
        {
            'id': 1,
            'title': 'Configuração de Rede',
            'category': 'Técnico',
            'created_at': '2024-01-15 14:30',
            'updated_at': '2024-01-15 14:30'
        },
        {
            'id': 2,
            'title': 'Procedimentos de Backup',
            'category': 'Administrativo',
            'created_at': '2024-01-14 09:15',
            'updated_at': '2024-01-14 09:15'
        },
        {
            'id': 3,
            'title': 'Manual do Usuário',
            'category': 'Documentação',
            'created_at': '2024-01-13 16:45',
            'updated_at': '2024-01-13 16:45'
        }
    ]
    
    return render_template('pages/index.html', pages=pages)

@pages_bp.route('/create')
@login_required
def create():
    """Criar nova página"""
    return render_template('pages/create.html')

@pages_bp.route('/<int:page_id>')
@login_required
def view(page_id):
    """Visualizar página"""
    # Simulate page data
    page = {
        'id': page_id,
        'title': f'Página {page_id}',
        'content': 'Conteúdo da página...',
        'category': 'Geral',
        'created_at': '2024-01-15 14:30',
        'updated_at': '2024-01-15 14:30'
    }
    
    return render_template('pages/view.html', page=page)

@pages_bp.route('/<int:page_id>/edit')
@login_required
def edit(page_id):
    """Editar página"""
    # Simulate page data
    page = {
        'id': page_id,
        'title': f'Página {page_id}',
        'content': 'Conteúdo da página...',
        'category': 'Geral'
    }
    
    return render_template('pages/edit.html', page=page)
