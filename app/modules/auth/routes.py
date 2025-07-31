"""
Wiki Veloz Fibra - Auth Routes
Rotas de autenticação e login

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

from app.modules.auth.models.user import User
from app.modules.auth.services.auth_service import AuthService
from app.core.database import DatabaseManager
from app.core.config import Config

# Create blueprint
auth_bp = Blueprint('auth', __name__)

# Initialize services
config = Config()
db_manager = DatabaseManager(config)
auth_service = AuthService(db_manager)

# Login form
class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        # Use real authentication service
        user_data = auth_service.authenticate_user(form.username.data, form.password.data)
        
        if user_data:
            # Create User object for Flask-Login
            user = User(
                id=user_data['id'],
                username=user_data['username'],
                name=user_data['name'],
                role=user_data['role'],
                created_at=user_data['created_at']
            )
            login_user(user, remember=form.remember_me.data)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Usuário ou senha inválidos!', 'error')
    
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('auth.login'))
