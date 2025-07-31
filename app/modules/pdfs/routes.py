"""
Wiki Veloz Fibra - PDFs Routes
Rotas para gerenciamento de PDFs

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template
from flask_login import login_required

# Create blueprint
pdfs_bp = Blueprint('pdfs', __name__)

@pdfs_bp.route('/')
@login_required
def index():
    """Lista de PDFs"""
    # Simulate PDFs data
    pdfs = [
        {
            'id': 1,
            'title': 'Manual Técnico',
            'filename': 'manual_tecnico.pdf',
            'size': '2.5 MB',
            'uploaded_at': '2024-01-15 14:30'
        },
        {
            'id': 2,
            'title': 'Procedimentos Administrativos',
            'filename': 'procedimentos.pdf',
            'size': '1.8 MB',
            'uploaded_at': '2024-01-14 09:15'
        },
        {
            'id': 3,
            'title': 'Configurações de Rede',
            'filename': 'config_rede.pdf',
            'size': '856 KB',
            'uploaded_at': '2024-01-13 16:45'
        }
    ]
    
    return render_template('pdfs/index.html', pdfs=pdfs)
