"""
Wiki Veloz Fibra - Documents Routes
Rotas para gerenciamento de documentos

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required

# Create blueprint
documents_bp = Blueprint('documents', __name__)

@documents_bp.route('/')
@login_required
def index():
    """Lista de documentos"""
    # Simulate documents data
    documents = [
        {
            'id': 1,
            'title': 'Manual Técnico',
            'filename': 'manual_tecnico.pdf',
            'category': 'Técnico',
            'size': '2.5 MB',
            'uploaded_at': '2024-01-15 14:30'
        },
        {
            'id': 2,
            'title': 'Procedimentos Administrativos',
            'filename': 'procedimentos.pdf',
            'category': 'Administrativo',
            'size': '1.8 MB',
            'uploaded_at': '2024-01-14 09:15'
        },
        {
            'id': 3,
            'title': 'Configurações de Rede',
            'filename': 'config_rede.docx',
            'category': 'Técnico',
            'size': '856 KB',
            'uploaded_at': '2024-01-13 16:45'
        }
    ]
    
    return render_template('documents/index.html', documents=documents)

@documents_bp.route('/upload')
@login_required
def upload():
    """Upload de documento"""
    return render_template('documents/upload.html')

@documents_bp.route('/<int:document_id>')
@login_required
def view(document_id):
    """Visualizar documento"""
    # Simulate document data
    document = {
        'id': document_id,
        'title': f'Documento {document_id}',
        'filename': f'documento_{document_id}.pdf',
        'category': 'Geral',
        'size': '1.2 MB',
        'uploaded_at': '2024-01-15 14:30',
        'description': 'Descrição do documento...'
    }
    
    return render_template('documents/view.html', document=document)
