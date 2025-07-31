"""
Wiki Veloz Fibra - Training Model
Modelo de treinamento para RH

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from datetime import datetime
from enum import Enum

class TrainingStatus(Enum):
    """Status do treinamento"""
    PLANNED = 'planned'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class TrainingType(Enum):
    """Tipo de treinamento"""
    TECHNICAL = 'technical'
    SOFT_SKILLS = 'soft_skills'
    COMPLIANCE = 'compliance'
    LEADERSHIP = 'leadership'
    PRODUCT = 'product'

class Training:
    """Modelo de treinamento"""
    
    def __init__(self, id, title, description, training_type, instructor,
                 start_date, end_date, location, max_participants, status,
                 created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.training_type = training_type
        self.instructor = instructor
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.max_participants = max_participants
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
    
    @property
    def duration_days(self):
        """Calcula duração em dias"""
        if not self.start_date or not self.end_date:
            return 0
        delta = self.end_date - self.start_date
        return delta.days + 1
    
    @property
    def is_upcoming(self):
        """Verifica se treinamento está próximo"""
        if not self.start_date:
            return False
        return self.start_date > datetime.now().date()
    
    @property
    def is_ongoing(self):
        """Verifica se treinamento está em andamento"""
        if not self.start_date or not self.end_date:
            return False
        today = datetime.now().date()
        return self.start_date <= today <= self.end_date
    
    def to_dict(self):
        """Converte treinamento para dicionário"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'training_type': self.training_type.value,
            'instructor': self.instructor,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'location': self.location,
            'max_participants': self.max_participants,
            'status': self.status.value,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'duration_days': self.duration_days,
            'is_upcoming': self.is_upcoming,
            'is_ongoing': self.is_ongoing
        }
    
    def __repr__(self):
        return f'<Training {self.title}>' 