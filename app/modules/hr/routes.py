"""
Wiki Veloz Fibra - HR Routes
Rotas para sistema de RH

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from wtforms import StringField, EmailField, SelectField, DateField, FloatField
from wtforms.validators import DataRequired, Email, Optional
from flask_wtf import FlaskForm
from datetime import datetime

from app.modules.hr.services.hr_service import HRService
from app.modules.hr.models.employee import EmployeeStatus, EmployeeType

# Create blueprint
hr_bp = Blueprint('hr', __name__)

# Initialize service
hr_service = HRService()

# Forms
class EmployeeForm(FlaskForm):
    """Formulário para criação/edição de funcionários"""
    name = StringField('Nome Completo', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired(), Email()])
    phone = StringField('Telefone', validators=[DataRequired()])
    position = StringField('Cargo', validators=[DataRequired()])
    department = StringField('Departamento', validators=[DataRequired()])
    employee_type = SelectField('Tipo de Funcionário',
                              choices=[
                                  ('full_time', 'Tempo Integral'),
                                  ('part_time', 'Meio Período'),
                                  ('contractor', 'Contratado'),
                                  ('intern', 'Estagiário')
                              ],
                              validators=[DataRequired()])
    status = SelectField('Status',
                        choices=[
                            ('active', 'Ativo'),
                            ('inactive', 'Inativo'),
                            ('on_leave', 'Em Licença'),
                            ('terminated', 'Demitido')
                        ],
                        validators=[DataRequired()])
    hire_date = DateField('Data de Contratação', validators=[DataRequired()])
    salary = FloatField('Salário', validators=[DataRequired()])
    manager_id = StringField('ID do Gerente', validators=[Optional()])

@hr_bp.route('/')
@login_required
def index():
    """Página principal de RH"""
    employees = hr_service.get_all_employees()
    summary = hr_service.get_hr_summary()
    
    return render_template('hr/index.html', 
                         employees=employees, 
                         summary=summary,
                         employee_types=EmployeeType,
                         employee_statuses=EmployeeStatus)

@hr_bp.route('/employees')
@login_required
def employees():
    """Lista de funcionários"""
    employees = hr_service.get_all_employees()
    summary = hr_service.get_hr_summary()
    
    return render_template('hr/employees.html', 
                         employees=employees, 
                         summary=summary)

@hr_bp.route('/employees/create', methods=['GET', 'POST'])
@login_required
def create_employee():
    """Criar novo funcionário"""
    form = EmployeeForm()
    
    if form.validate_on_submit():
        try:
            employee_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'position': form.position.data,
                'department': form.department.data,
                'employee_type': form.employee_type.data,
                'status': form.status.data,
                'hire_date': form.hire_date.data.strftime('%Y-%m-%d'),
                'salary': form.salary.data,
                'manager_id': form.manager_id.data if form.manager_id.data else None
            }
            
            employee = hr_service.create_employee(employee_data)
            flash('Funcionário criado com sucesso!', 'success')
            return redirect(url_for('hr.employees'))
            
        except Exception as e:
            flash(f'Erro ao criar funcionário: {str(e)}', 'error')
    
    return render_template('hr/create_employee.html', form=form)

@hr_bp.route('/employees/<int:employee_id>')
@login_required
def show_employee(employee_id):
    """Visualizar funcionário específico"""
    employee = hr_service.get_employee_by_id(employee_id)
    if not employee:
        flash('Funcionário não encontrado!', 'error')
        return redirect(url_for('hr.employees'))
    
    return render_template('hr/show_employee.html', employee=employee)

@hr_bp.route('/employees/<int:employee_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_employee(employee_id):
    """Editar funcionário"""
    employee = hr_service.get_employee_by_id(employee_id)
    if not employee:
        flash('Funcionário não encontrado!', 'error')
        return redirect(url_for('hr.employees'))
    
    form = EmployeeForm(obj=employee)
    
    if form.validate_on_submit():
        try:
            employee_data = {
                'name': form.name.data,
                'email': form.email.data,
                'phone': form.phone.data,
                'position': form.position.data,
                'department': form.department.data,
                'employee_type': form.employee_type.data,
                'status': form.status.data,
                'hire_date': form.hire_date.data.strftime('%Y-%m-%d'),
                'salary': form.salary.data,
                'manager_id': form.manager_id.data if form.manager_id.data else None
            }
            
            updated_employee = hr_service.update_employee(employee_id, employee_data)
            flash('Funcionário atualizado com sucesso!', 'success')
            return redirect(url_for('hr.show_employee', employee_id=employee_id))
            
        except Exception as e:
            flash(f'Erro ao atualizar funcionário: {str(e)}', 'error')
    
    return render_template('hr/edit_employee.html', form=form, employee=employee)

@hr_bp.route('/employees/<int:employee_id>/delete', methods=['POST'])
@login_required
def delete_employee(employee_id):
    """Deletar funcionário"""
    try:
        success = hr_service.delete_employee(employee_id)
        if success:
            flash('Funcionário removido com sucesso!', 'success')
        else:
            flash('Funcionário não encontrado!', 'error')
    except Exception as e:
        flash(f'Erro ao remover funcionário: {str(e)}', 'error')
    
    return redirect(url_for('hr.employees'))

@hr_bp.route('/departments')
@login_required
def departments():
    """Lista de departamentos"""
    summary = hr_service.get_hr_summary()
    return render_template('hr/departments.html', summary=summary)

@hr_bp.route('/reports')
@login_required
def reports():
    """Relatórios de RH"""
    summary = hr_service.get_hr_summary()
    active_employees = hr_service.get_active_employees()
    
    return render_template('hr/reports.html', 
                         summary=summary,
                         active_employees=active_employees)

# API Routes
@hr_bp.route('/api/employees')
@login_required
def api_get_employees():
    """API: Retorna todos os funcionários"""
    employees = hr_service.get_all_employees()
    return jsonify([employee.to_dict() for employee in employees])

@hr_bp.route('/api/employees/<int:employee_id>')
@login_required
def api_get_employee(employee_id):
    """API: Retorna funcionário específico"""
    employee = hr_service.get_employee_by_id(employee_id)
    if not employee:
        return jsonify({'error': 'Funcionário não encontrado'}), 404
    
    return jsonify(employee.to_dict())

@hr_bp.route('/api/employees/department/<department>')
@login_required
def api_get_employees_by_department(department):
    """API: Retorna funcionários por departamento"""
    employees = hr_service.get_employees_by_department(department)
    return jsonify([employee.to_dict() for employee in employees])

@hr_bp.route('/api/hr/summary')
@login_required
def api_get_hr_summary():
    """API: Retorna resumo do RH"""
    summary = hr_service.get_hr_summary()
    return jsonify(summary) 