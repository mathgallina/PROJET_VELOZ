"""
Wiki Veloz Fibra - Goals Routes
Rotas para sistema de metas

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from wtforms import StringField, TextAreaField, FloatField, SelectField, DateField
from wtforms.validators import DataRequired, Optional
from flask_wtf import FlaskForm
from datetime import datetime

from app.modules.goals.services.goal_service import GoalService
from app.modules.goals.models.goal import GoalStatus, GoalType

# Create blueprint
goals_bp = Blueprint('goals', __name__)

# Initialize service
goal_service = GoalService()

# Forms
class GoalForm(FlaskForm):
    """Formulário para criação/edição de metas"""
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descrição')
    target_value = FloatField('Valor Alvo', validators=[DataRequired()])
    current_value = FloatField('Valor Atual', default=0)
    goal_type = SelectField('Tipo de Meta', 
                          choices=[
                              ('sales_amount', 'Valor de Vendas'),
                              ('sales_quantity', 'Quantidade de Vendas'),
                              ('new_customers', 'Novos Clientes'),
                              ('customer_satisfaction', 'Satisfação do Cliente')
                          ],
                          validators=[DataRequired()])
    status = SelectField('Status',
                        choices=[
                            ('pending', 'Pendente'),
                            ('in_progress', 'Em Andamento'),
                            ('completed', 'Concluída'),
                            ('cancelled', 'Cancelada')
                        ],
                        validators=[DataRequired()])
    assigned_to = StringField('Responsável', validators=[DataRequired()])
    start_date = DateField('Data de Início', validators=[Optional()])
    end_date = DateField('Data de Fim', validators=[Optional()])

class ProgressForm(FlaskForm):
    """Formulário para atualização de progresso"""
    current_value = FloatField('Valor Atual', validators=[DataRequired()])

@goals_bp.route('/')
@login_required
def index():
    """Página principal de metas"""
    goals = goal_service.get_all_goals()
    summary = goal_service.get_goals_summary()
    
    return render_template('goals/index.html', 
                         goals=goals, 
                         summary=summary,
                         goal_types=GoalType,
                         goal_statuses=GoalStatus)

@goals_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Criar nova meta"""
    form = GoalForm()
    
    if form.validate_on_submit():
        try:
            goal_data = {
                'title': form.title.data,
                'description': form.description.data,
                'target_value': form.target_value.data,
                'current_value': form.current_value.data,
                'goal_type': form.goal_type.data,
                'status': form.status.data,
                'assigned_to': form.assigned_to.data,
                'created_by': current_user.username,
                'start_date': form.start_date.data.strftime('%Y-%m-%d') if form.start_date.data else None,
                'end_date': form.end_date.data.strftime('%Y-%m-%d') if form.end_date.data else None
            }
            
            goal = goal_service.create_goal(goal_data)
            flash('Meta criada com sucesso!', 'success')
            return redirect(url_for('goals.index'))
            
        except Exception as e:
            flash(f'Erro ao criar meta: {str(e)}', 'error')
    
    return render_template('goals/create.html', form=form)

@goals_bp.route('/<int:goal_id>')
@login_required
def show(goal_id):
    """Visualizar meta específica"""
    goal = goal_service.get_goal_by_id(goal_id)
    if not goal:
        flash('Meta não encontrada!', 'error')
        return redirect(url_for('goals.index'))
    
    return render_template('goals/show.html', goal=goal)

@goals_bp.route('/<int:goal_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(goal_id):
    """Editar meta"""
    goal = goal_service.get_goal_by_id(goal_id)
    if not goal:
        flash('Meta não encontrada!', 'error')
        return redirect(url_for('goals.index'))
    
    form = GoalForm(obj=goal)
    
    if form.validate_on_submit():
        try:
            goal_data = {
                'title': form.title.data,
                'description': form.description.data,
                'target_value': form.target_value.data,
                'current_value': form.current_value.data,
                'goal_type': form.goal_type.data,
                'status': form.status.data,
                'assigned_to': form.assigned_to.data,
                'start_date': form.start_date.data.strftime('%Y-%m-%d') if form.start_date.data else None,
                'end_date': form.end_date.data.strftime('%Y-%m-%d') if form.end_date.data else None
            }
            
            updated_goal = goal_service.update_goal(goal_id, goal_data)
            flash('Meta atualizada com sucesso!', 'success')
            return redirect(url_for('goals.show', goal_id=goal_id))
            
        except Exception as e:
            flash(f'Erro ao atualizar meta: {str(e)}', 'error')
    
    return render_template('goals/edit.html', form=form, goal=goal)

@goals_bp.route('/<int:goal_id>/progress', methods=['GET', 'POST'])
@login_required
def update_progress(goal_id):
    """Atualizar progresso da meta"""
    goal = goal_service.get_goal_by_id(goal_id)
    if not goal:
        flash('Meta não encontrada!', 'error')
        return redirect(url_for('goals.index'))
    
    form = ProgressForm()
    
    if form.validate_on_submit():
        try:
            updated_goal = goal_service.update_goal_progress(goal_id, form.current_value.data)
            flash('Progresso atualizado com sucesso!', 'success')
            return redirect(url_for('goals.show', goal_id=goal_id))
            
        except Exception as e:
            flash(f'Erro ao atualizar progresso: {str(e)}', 'error')
    
    return render_template('goals/progress.html', form=form, goal=goal)

@goals_bp.route('/<int:goal_id>/delete', methods=['POST'])
@login_required
def delete(goal_id):
    """Deletar meta"""
    try:
        success = goal_service.delete_goal(goal_id)
        if success:
            flash('Meta removida com sucesso!', 'success')
        else:
            flash('Meta não encontrada!', 'error')
    except Exception as e:
        flash(f'Erro ao remover meta: {str(e)}', 'error')
    
    return redirect(url_for('goals.index'))

# API Routes
@goals_bp.route('/api/goals')
@login_required
def api_get_goals():
    """API: Retorna todas as metas"""
    goals = goal_service.get_all_goals()
    return jsonify([goal.to_dict() for goal in goals])

@goals_bp.route('/api/goals/<int:goal_id>')
@login_required
def api_get_goal(goal_id):
    """API: Retorna meta específica"""
    goal = goal_service.get_goal_by_id(goal_id)
    if not goal:
        return jsonify({'error': 'Meta não encontrada'}), 404
    
    return jsonify(goal.to_dict())

@goals_bp.route('/api/goals/summary')
@login_required
def api_get_summary():
    """API: Retorna resumo das metas"""
    summary = goal_service.get_goals_summary()
    return jsonify(summary)

@goals_bp.route('/api/goals/overdue')
@login_required
def api_get_overdue():
    """API: Retorna metas atrasadas"""
    overdue_goals = goal_service.get_overdue_goals()
    return jsonify([goal.to_dict() for goal in overdue_goals]) 