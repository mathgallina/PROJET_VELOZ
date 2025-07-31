"""
Wiki Veloz Fibra - HR Service
Serviço principal para gerenciamento de RH

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
from app.modules.hr.models.employee import Employee, EmployeeStatus, EmployeeType
from app.modules.hr.repositories.employee_repository import EmployeeRepository

class HRService:
    """Serviço principal para gerenciamento de RH"""
    
    def __init__(self):
        self.employee_repository = EmployeeRepository()
    
    # Employee Management
    def create_employee(self, employee_data: Dict[str, Any]) -> Employee:
        """Cria um novo funcionário"""
        employee = Employee(
            id=0,  # Será definido pelo repositório
            name=employee_data['name'],
            email=employee_data['email'],
            phone=employee_data['phone'],
            position=employee_data['position'],
            department=employee_data['department'],
            employee_type=EmployeeType(employee_data['employee_type']),
            status=EmployeeStatus(employee_data.get('status', 'active')),
            hire_date=datetime.strptime(employee_data['hire_date'], '%Y-%m-%d').date() if employee_data.get('hire_date') else None,
            salary=float(employee_data['salary']),
            manager_id=employee_data.get('manager_id'),
            created_at=None,  # Será definido pelo repositório
            updated_at=None   # Será definido pelo repositório
        )
        
        return self.employee_repository.create(employee)
    
    def get_all_employees(self) -> List[Employee]:
        """Retorna todos os funcionários"""
        return self.employee_repository.get_all()
    
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """Retorna funcionário por ID"""
        return self.employee_repository.get_by_id(employee_id)
    
    def get_employees_by_department(self, department: str) -> List[Employee]:
        """Retorna funcionários por departamento"""
        return self.employee_repository.get_by_department(department)
    
    def get_employees_by_status(self, status: str) -> List[Employee]:
        """Retorna funcionários por status"""
        return self.employee_repository.get_by_status(EmployeeStatus(status))
    
    def get_active_employees(self) -> List[Employee]:
        """Retorna funcionários ativos"""
        return self.employee_repository.get_active_employees()
    
    def update_employee(self, employee_id: int, employee_data: Dict[str, Any]) -> Optional[Employee]:
        """Atualiza um funcionário"""
        employee = self.employee_repository.get_by_id(employee_id)
        if not employee:
            return None
        
        # Atualiza campos
        if 'name' in employee_data:
            employee.name = employee_data['name']
        if 'email' in employee_data:
            employee.email = employee_data['email']
        if 'phone' in employee_data:
            employee.phone = employee_data['phone']
        if 'position' in employee_data:
            employee.position = employee_data['position']
        if 'department' in employee_data:
            employee.department = employee_data['department']
        if 'employee_type' in employee_data:
            employee.employee_type = EmployeeType(employee_data['employee_type'])
        if 'status' in employee_data:
            employee.status = EmployeeStatus(employee_data['status'])
        if 'hire_date' in employee_data and employee_data['hire_date']:
            employee.hire_date = datetime.strptime(employee_data['hire_date'], '%Y-%m-%d').date()
        if 'salary' in employee_data:
            employee.salary = float(employee_data['salary'])
        if 'manager_id' in employee_data:
            employee.manager_id = employee_data['manager_id']
        
        return self.employee_repository.update(employee)
    
    def delete_employee(self, employee_id: int) -> bool:
        """Remove um funcionário"""
        return self.employee_repository.delete(employee_id)
    
    def get_hr_summary(self) -> Dict[str, Any]:
        """Retorna resumo do RH"""
        summary = self.employee_repository.get_employees_summary()
        
        # Adiciona estatísticas por departamento
        employees = self.get_all_employees()
        dept_stats = {}
        for emp in employees:
            if emp.department not in dept_stats:
                dept_stats[emp.department] = {
                    'total': 0,
                    'active': 0,
                    'avg_salary': 0,
                    'salaries': []
                }
            dept_stats[emp.department]['total'] += 1
            if emp.is_active:
                dept_stats[emp.department]['active'] += 1
            dept_stats[emp.department]['salaries'].append(emp.salary)
        
        # Calcula média salarial por departamento
        for dept in dept_stats:
            if dept_stats[dept]['salaries']:
                dept_stats[dept]['avg_salary'] = round(
                    sum(dept_stats[dept]['salaries']) / len(dept_stats[dept]['salaries']), 2
                )
            del dept_stats[dept]['salaries']
        
        summary['department_stats'] = dept_stats
        return summary
    
    def get_employees_by_period(self, start_date: datetime, end_date: datetime) -> List[Employee]:
        """Retorna funcionários contratados em um período"""
        employees = self.get_all_employees()
        return [
            emp for emp in employees
            if emp.hire_date and start_date.date() <= emp.hire_date <= end_date.date()
        ]
    
    def get_employees_by_salary_range(self, min_salary: float, max_salary: float) -> List[Employee]:
        """Retorna funcionários por faixa salarial"""
        employees = self.get_all_employees()
        return [
            emp for emp in employees
            if min_salary <= emp.salary <= max_salary
        ] 