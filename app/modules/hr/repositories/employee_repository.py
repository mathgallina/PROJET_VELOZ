"""
Wiki Veloz Fibra - Employee Repository
Repositório para gerenciamento de funcionários

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

import json
import os
from datetime import datetime
from typing import List, Optional
from app.modules.hr.models.employee import Employee, EmployeeStatus, EmployeeType

class EmployeeRepository:
    """Repositório para gerenciamento de funcionários"""
    
    def __init__(self, data_file='employees.json'):
        self.data_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            'data',
            data_file
        )
        self._ensure_data_file()
    
    def _ensure_data_file(self):
        """Garante que o arquivo de dados existe"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)
    
    def _load_employees(self) -> List[dict]:
        """Carrega funcionários do arquivo JSON"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_employees(self, employees: List[dict]):
        """Salva funcionários no arquivo JSON"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(employees, f, ensure_ascii=False, indent=2)
    
    def _dict_to_employee(self, employee_dict: dict) -> Employee:
        """Converte dicionário para objeto Employee"""
        return Employee(
            id=employee_dict['id'],
            name=employee_dict['name'],
            email=employee_dict['email'],
            phone=employee_dict['phone'],
            position=employee_dict['position'],
            department=employee_dict['department'],
            employee_type=EmployeeType(employee_dict['employee_type']),
            status=EmployeeStatus(employee_dict['status']),
            hire_date=datetime.fromisoformat(employee_dict['hire_date']).date() if employee_dict['hire_date'] else None,
            salary=employee_dict['salary'],
            manager_id=employee_dict.get('manager_id'),
            created_at=datetime.fromisoformat(employee_dict['created_at']) if employee_dict['created_at'] else None,
            updated_at=datetime.fromisoformat(employee_dict['updated_at']) if employee_dict['updated_at'] else None
        )
    
    def _employee_to_dict(self, employee: Employee) -> dict:
        """Converte objeto Employee para dicionário"""
        return {
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'phone': employee.phone,
            'position': employee.position,
            'department': employee.department,
            'employee_type': employee.employee_type.value,
            'status': employee.status.value,
            'hire_date': employee.hire_date.isoformat() if employee.hire_date else None,
            'salary': employee.salary,
            'manager_id': employee.manager_id,
            'created_at': employee.created_at.isoformat() if employee.created_at else None,
            'updated_at': employee.updated_at.isoformat() if employee.updated_at else None
        }
    
    def get_all(self) -> List[Employee]:
        """Retorna todos os funcionários"""
        employees_data = self._load_employees()
        return [self._dict_to_employee(emp_dict) for emp_dict in employees_data]
    
    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        """Retorna funcionário por ID"""
        employees_data = self._load_employees()
        for emp_dict in employees_data:
            if emp_dict['id'] == employee_id:
                return self._dict_to_employee(emp_dict)
        return None
    
    def get_by_department(self, department: str) -> List[Employee]:
        """Retorna funcionários por departamento"""
        employees = self.get_all()
        return [emp for emp in employees if emp.department == department]
    
    def get_by_status(self, status: EmployeeStatus) -> List[Employee]:
        """Retorna funcionários por status"""
        employees = self.get_all()
        return [emp for emp in employees if emp.status == status]
    
    def get_active_employees(self) -> List[Employee]:
        """Retorna funcionários ativos"""
        return self.get_by_status(EmployeeStatus.ACTIVE)
    
    def create(self, employee: Employee) -> Employee:
        """Cria um novo funcionário"""
        employees_data = self._load_employees()
        
        # Gera ID único
        if employees_data:
            max_id = max(emp_dict['id'] for emp_dict in employees_data)
            employee.id = max_id + 1
        else:
            employee.id = 1
        
        # Define timestamps
        now = datetime.now()
        employee.created_at = now
        employee.updated_at = now
        
        employees_data.append(self._employee_to_dict(employee))
        self._save_employees(employees_data)
        
        return employee
    
    def update(self, employee: Employee) -> Employee:
        """Atualiza um funcionário existente"""
        employees_data = self._load_employees()
        
        for i, emp_dict in enumerate(employees_data):
            if emp_dict['id'] == employee.id:
                employee.updated_at = datetime.now()
                employees_data[i] = self._employee_to_dict(employee)
                self._save_employees(employees_data)
                return employee
        
        raise ValueError(f"Funcionário com ID {employee.id} não encontrado")
    
    def delete(self, employee_id: int) -> bool:
        """Remove um funcionário"""
        employees_data = self._load_employees()
        
        for i, emp_dict in enumerate(employees_data):
            if emp_dict['id'] == employee_id:
                del employees_data[i]
                self._save_employees(employees_data)
                return True
        
        return False
    
    def get_employees_summary(self) -> dict:
        """Retorna resumo dos funcionários"""
        employees = self.get_all()
        
        total_employees = len(employees)
        active_employees = len([emp for emp in employees if emp.is_active])
        departments = list(set(emp.department for emp in employees))
        
        avg_salary = 0
        if employees:
            avg_salary = sum(emp.salary for emp in employees) / len(employees)
        
        return {
            'total_employees': total_employees,
            'active_employees': active_employees,
            'departments_count': len(departments),
            'avg_salary': round(avg_salary, 2),
            'departments': departments
        } 