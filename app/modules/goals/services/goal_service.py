"""
Wiki Veloz Fibra - Goal Service
Serviço para gerenciamento de metas

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, date
from app.modules.goals.models.goal import Goal, GoalStatus, GoalType
from app.modules.goals.repositories.goal_repository import GoalRepository

class GoalService:
    """Serviço para gerenciamento de metas"""
    
    def __init__(self):
        self.repository = GoalRepository()
    
    def create_goal(self, goal_data: Dict[str, Any]) -> Goal:
        """Cria uma nova meta"""
        goal = Goal(
            id=0,  # Será definido pelo repositório
            title=goal_data['title'],
            description=goal_data.get('description', ''),
            target_value=float(goal_data['target_value']),
            current_value=float(goal_data.get('current_value', 0)),
            goal_type=GoalType(goal_data['goal_type']),
            status=GoalStatus(goal_data.get('status', 'pending')),
            assigned_to=goal_data['assigned_to'],
            created_by=goal_data['created_by'],
            start_date=datetime.strptime(goal_data['start_date'], '%Y-%m-%d').date() if goal_data.get('start_date') else None,
            end_date=datetime.strptime(goal_data['end_date'], '%Y-%m-%d').date() if goal_data.get('end_date') else None,
            created_at=None,  # Será definido pelo repositório
            updated_at=None   # Será definido pelo repositório
        )
        
        return self.repository.create(goal)
    
    def get_all_goals(self) -> List[Goal]:
        """Retorna todas as metas"""
        return self.repository.get_all()
    
    def get_goal_by_id(self, goal_id: int) -> Optional[Goal]:
        """Retorna meta por ID"""
        return self.repository.get_by_id(goal_id)
    
    def get_goals_by_user(self, user_id: str) -> List[Goal]:
        """Retorna metas de um usuário"""
        return self.repository.get_by_assigned_to(user_id)
    
    def get_goals_by_status(self, status: str) -> List[Goal]:
        """Retorna metas por status"""
        return self.repository.get_by_status(GoalStatus(status))
    
    def get_overdue_goals(self) -> List[Goal]:
        """Retorna metas atrasadas"""
        return self.repository.get_overdue_goals()
    
    def update_goal(self, goal_id: int, goal_data: Dict[str, Any]) -> Optional[Goal]:
        """Atualiza uma meta"""
        goal = self.repository.get_by_id(goal_id)
        if not goal:
            return None
        
        # Atualiza campos
        if 'title' in goal_data:
            goal.title = goal_data['title']
        if 'description' in goal_data:
            goal.description = goal_data['description']
        if 'target_value' in goal_data:
            goal.target_value = float(goal_data['target_value'])
        if 'current_value' in goal_data:
            goal.current_value = float(goal_data['current_value'])
        if 'goal_type' in goal_data:
            goal.goal_type = GoalType(goal_data['goal_type'])
        if 'status' in goal_data:
            goal.status = GoalStatus(goal_data['status'])
        if 'assigned_to' in goal_data:
            goal.assigned_to = goal_data['assigned_to']
        if 'start_date' in goal_data and goal_data['start_date']:
            goal.start_date = datetime.strptime(goal_data['start_date'], '%Y-%m-%d').date()
        if 'end_date' in goal_data and goal_data['end_date']:
            goal.end_date = datetime.strptime(goal_data['end_date'], '%Y-%m-%d').date()
        
        return self.repository.update(goal)
    
    def update_goal_progress(self, goal_id: int, current_value: float) -> Optional[Goal]:
        """Atualiza o progresso de uma meta"""
        return self.repository.update_progress(goal_id, current_value)
    
    def delete_goal(self, goal_id: int) -> bool:
        """Remove uma meta"""
        return self.repository.delete(goal_id)
    
    def get_goals_summary(self) -> Dict[str, Any]:
        """Retorna resumo das metas"""
        all_goals = self.get_all_goals()
        
        total_goals = len(all_goals)
        completed_goals = len([g for g in all_goals if g.status == GoalStatus.COMPLETED])
        in_progress_goals = len([g for g in all_goals if g.status == GoalStatus.IN_PROGRESS])
        overdue_goals = len([g for g in all_goals if g.is_overdue])
        
        avg_progress = 0
        if all_goals:
            avg_progress = sum(g.progress_percentage for g in all_goals) / len(all_goals)
        
        # Calcula faturamento total baseado nas comissões
        total_revenue = sum(g.commission_value for g in all_goals)
        
        return {
            'total_goals': total_goals,
            'completed_goals': completed_goals,
            'in_progress_goals': in_progress_goals,
            'overdue_goals': overdue_goals,
            'avg_progress': round(avg_progress, 2),
            'completion_rate': round((completed_goals / total_goals * 100) if total_goals > 0 else 0, 2),
            'total_revenue': total_revenue
        }
    
    def get_goals_by_period(self, start_date: date, end_date: date) -> List[Goal]:
        """Retorna metas dentro de um período"""
        all_goals = self.get_all_goals()
        return [
            goal for goal in all_goals
            if goal.start_date and goal.end_date
            and goal.start_date <= end_date
            and goal.end_date >= start_date
        ] 