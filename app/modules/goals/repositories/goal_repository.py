"""
Wiki Veloz Fibra - Goal Repository
Repositório para gerenciamento de metas

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

import json
import os
from datetime import datetime, date
from typing import List, Optional
from app.modules.goals.models.goal import Goal, GoalStatus, GoalType

class GoalRepository:
    """Repositório para gerenciamento de metas"""
    
    def __init__(self, data_file='goals.json'):
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
    
    def _load_goals(self) -> List[dict]:
        """Carrega metas do arquivo JSON"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_goals(self, goals: List[dict]):
        """Salva metas no arquivo JSON"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(goals, f, ensure_ascii=False, indent=2)
    
    def _dict_to_goal(self, goal_dict: dict) -> Goal:
        """Converte dicionário para objeto Goal"""
        return Goal(
            id=goal_dict['id'],
            title=goal_dict['title'],
            description=goal_dict['description'],
            target_value=goal_dict['target_value'],
            current_value=goal_dict['current_value'],
            goal_type=GoalType(goal_dict['goal_type']),
            status=GoalStatus(goal_dict['status']),
            assigned_to=goal_dict['assigned_to'],
            created_by=goal_dict['created_by'],
            start_date=datetime.fromisoformat(goal_dict['start_date']).date() if goal_dict['start_date'] else None,
            end_date=datetime.fromisoformat(goal_dict['end_date']).date() if goal_dict['end_date'] else None,
            created_at=datetime.fromisoformat(goal_dict['created_at']) if goal_dict['created_at'] else None,
            updated_at=datetime.fromisoformat(goal_dict['updated_at']) if goal_dict['updated_at'] else None
        )
    
    def _goal_to_dict(self, goal: Goal) -> dict:
        """Converte objeto Goal para dicionário"""
        return {
            'id': goal.id,
            'title': goal.title,
            'description': goal.description,
            'target_value': goal.target_value,
            'current_value': goal.current_value,
            'goal_type': goal.goal_type.value,
            'status': goal.status.value,
            'assigned_to': goal.assigned_to,
            'created_by': goal.created_by,
            'start_date': goal.start_date.isoformat() if goal.start_date else None,
            'end_date': goal.end_date.isoformat() if goal.end_date else None,
            'created_at': goal.created_at.isoformat() if goal.created_at else None,
            'updated_at': goal.updated_at.isoformat() if goal.updated_at else None
        }
    
    def get_all(self) -> List[Goal]:
        """Retorna todas as metas"""
        goals_data = self._load_goals()
        return [self._dict_to_goal(goal_dict) for goal_dict in goals_data]
    
    def get_by_id(self, goal_id: int) -> Optional[Goal]:
        """Retorna meta por ID"""
        goals_data = self._load_goals()
        for goal_dict in goals_data:
            if goal_dict['id'] == goal_id:
                return self._dict_to_goal(goal_dict)
        return None
    
    def get_by_assigned_to(self, user_id: str) -> List[Goal]:
        """Retorna metas atribuídas a um usuário"""
        goals = self.get_all()
        return [goal for goal in goals if goal.assigned_to == user_id]
    
    def get_by_status(self, status: GoalStatus) -> List[Goal]:
        """Retorna metas por status"""
        goals = self.get_all()
        return [goal for goal in goals if goal.status == status]
    
    def get_overdue_goals(self) -> List[Goal]:
        """Retorna metas atrasadas"""
        goals = self.get_all()
        return [goal for goal in goals if goal.is_overdue]
    
    def create(self, goal: Goal) -> Goal:
        """Cria uma nova meta"""
        goals_data = self._load_goals()
        
        # Gera ID único
        if goals_data:
            max_id = max(goal_dict['id'] for goal_dict in goals_data)
            goal.id = max_id + 1
        else:
            goal.id = 1
        
        # Define timestamps
        now = datetime.now()
        goal.created_at = now
        goal.updated_at = now
        
        goals_data.append(self._goal_to_dict(goal))
        self._save_goals(goals_data)
        
        return goal
    
    def update(self, goal: Goal) -> Goal:
        """Atualiza uma meta existente"""
        goals_data = self._load_goals()
        
        for i, goal_dict in enumerate(goals_data):
            if goal_dict['id'] == goal.id:
                goal.updated_at = datetime.now()
                goals_data[i] = self._goal_to_dict(goal)
                self._save_goals(goals_data)
                return goal
        
        raise ValueError(f"Meta com ID {goal.id} não encontrada")
    
    def delete(self, goal_id: int) -> bool:
        """Remove uma meta"""
        goals_data = self._load_goals()
        
        for i, goal_dict in enumerate(goals_data):
            if goal_dict['id'] == goal_id:
                del goals_data[i]
                self._save_goals(goals_data)
                return True
        
        return False
    
    def update_progress(self, goal_id: int, current_value: float) -> Optional[Goal]:
        """Atualiza o progresso de uma meta"""
        goal = self.get_by_id(goal_id)
        if not goal:
            return None
        
        goal.current_value = current_value
        
        # Atualiza status baseado no progresso
        if goal.current_value >= goal.target_value:
            goal.status = GoalStatus.COMPLETED
        elif goal.current_value > 0:
            goal.status = GoalStatus.IN_PROGRESS
        
        return self.update(goal) 