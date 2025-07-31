"""
Wiki Veloz Fibra - Department Model
Modelo de departamento para RH

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from datetime import datetime

class Department:
    """Modelo de departamento"""
    
    def __init__(self, id, name, description, manager_id, budget, 
                 created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.manager_id = manager_id
        self.budget = budget
        self.created_at = created_at
        self.updated_at = updated_at
    
    def to_dict(self):
        """Converte departamento para dicionário"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'manager_id': self.manager_id,
            'budget': self.budget,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Department {self.name}>' 