"""
Wiki Veloz Fibra - Employee Model
Modelo de funcionário para RH

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from datetime import datetime
from enum import Enum

class EmployeeStatus(Enum):
    """Status do funcionário"""
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    ON_LEAVE = 'on_leave'
    TERMINATED = 'terminated'

class EmployeeType(Enum):
    """Tipo de funcionário"""
    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    CONTRACTOR = 'contractor'
    INTERN = 'intern'

class Employee:
    """Modelo de funcionário"""
    
    def __init__(self, id, name, email, phone, position, department, 
                 employee_type, status, hire_date, salary, manager_id=None,
                 created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.position = position
        self.department = department
        self.employee_type = employee_type
        self.status = status
        self.hire_date = hire_date
        self.salary = salary
        self.manager_id = manager_id
        self.created_at = created_at
        self.updated_at = updated_at
    
    @property
    def years_of_service(self):
        """Calcula anos de serviço"""
        if not self.hire_date:
            return 0
        delta = datetime.now().date() - self.hire_date
        return delta.days // 365
    
    @property
    def is_active(self):
        """Verifica se funcionário está ativo"""
        return self.status == EmployeeStatus.ACTIVE
    
    def to_dict(self):
        """Converte funcionário para dicionário"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'position': self.position,
            'department': self.department,
            'employee_type': self.employee_type.value,
            'status': self.status.value,
            'hire_date': self.hire_date.isoformat() if self.hire_date else None,
            'salary': self.salary,
            'manager_id': self.manager_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'years_of_service': self.years_of_service,
            'is_active': self.is_active
        }
    
    def __repr__(self):
        return f'<Employee {self.name}>' 