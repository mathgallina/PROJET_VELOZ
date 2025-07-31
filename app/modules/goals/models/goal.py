"""
Wiki Veloz Fibra - Goal Model
Modelo de meta para vendas

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from datetime import datetime
from enum import Enum

class GoalStatus(Enum):
    """Status da meta"""
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class GoalType(Enum):
    """Tipo de meta"""
    RENEWALS = 'renewals'  # Renovações de contrato
    UPGRADES = 'upgrades'  # Upgrades de clientes
    NEW_CUSTOMERS = 'new_customers'  # Novos clientes
    REVENUE = 'revenue'  # Faturamento total
    CUSTOMER_SATISFACTION = 'customer_satisfaction'  # Satisfação do cliente

class Goal:
    """Modelo de meta para vendas"""
    
    def __init__(self, id, title, description, target_value, current_value, 
                 goal_type, status, assigned_to, created_by, start_date, 
                 end_date, created_at, updated_at):
        self.id = id
        self.title = title
        self.description = description
        self.target_value = target_value
        self.current_value = current_value
        self.goal_type = goal_type
        self.status = status
        self.assigned_to = assigned_to
        self.created_by = created_by
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = created_at
        self.updated_at = updated_at
    
    @property
    def progress_percentage(self):
        """Calcula o percentual de progresso da meta"""
        if self.target_value == 0:
            return 0
        return min(100, (self.current_value / self.target_value) * 100)
    
    @property
    def commission_value(self):
        """Calcula o valor da comissão baseado nas regras da Veloz Fibra"""
        if self.goal_type == GoalType.RENEWALS:
            # R$ 3 por renovação, mínimo 100 renovações
            if self.current_value >= 100:
                return self.current_value * 3.0
            return 0
        elif self.goal_type == GoalType.UPGRADES:
            # Diferença adicional para upgrades
            return self.current_value
        elif self.goal_type == GoalType.REVENUE:
            # Comissão baseada no faturamento
            return self.current_value * 0.05  # 5% do faturamento
        else:
            return 0
    
    @property
    def is_overdue(self):
        """Verifica se a meta está atrasada"""
        if self.status == GoalStatus.COMPLETED:
            return False
        return datetime.now().date() > self.end_date
    
    @property
    def days_remaining(self):
        """Calcula os dias restantes"""
        remaining = self.end_date - datetime.now().date()
        return max(0, remaining.days)
    
    def to_dict(self):
        """Converte meta para dicionário"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'target_value': self.target_value,
            'current_value': self.current_value,
            'goal_type': self.goal_type.value,
            'status': self.status.value,
            'assigned_to': self.assigned_to,
            'created_by': self.created_by,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'progress_percentage': self.progress_percentage,
            'is_overdue': self.is_overdue,
            'days_remaining': self.days_remaining,
            'commission_value': self.commission_value
        }
    
    def __repr__(self):
        return f'<Goal {self.title}>' 