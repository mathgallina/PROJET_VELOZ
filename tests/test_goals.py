"""
Testes para o sistema de metas da Veloz Fibra

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

import unittest
import json
import os
import tempfile
from datetime import datetime, date
from unittest.mock import patch, MagicMock

from app.modules.goals.models.goal import Goal, GoalStatus, GoalType
from app.modules.goals.services.goal_service import GoalService
from app.modules.goals.repositories.goal_repository import GoalRepository


class TestGoalModel(unittest.TestCase):
    """Testes para o modelo Goal"""
    
    def setUp(self):
        """Configuração inicial para os testes"""
        self.goal_data = {
            'id': 1,
            'title': 'Test Goal',
            'description': 'Test Description',
            'target_value': 100,
            'current_value': 50,
            'goal_type': GoalType.RENEWALS,
            'status': GoalStatus.IN_PROGRESS,
            'assigned_to': 'Test User',
            'created_by': 'admin',
            'start_date': date(2024, 1, 1),
            'end_date': date(2024, 1, 31),
            'created_at': datetime(2024, 1, 1, 8, 0, 0),
            'updated_at': datetime(2024, 1, 15, 14, 30, 0)
        }
        self.goal = Goal(**self.goal_data)
    
    def test_goal_creation(self):
        """Testa criação de meta"""
        self.assertEqual(self.goal.title, 'Test Goal')
        self.assertEqual(self.goal.target_value, 100)
        self.assertEqual(self.goal.current_value, 50)
        self.assertEqual(self.goal.goal_type, GoalType.RENEWALS)
        self.assertEqual(self.goal.status, GoalStatus.IN_PROGRESS)
    
    def test_progress_percentage(self):
        """Testa cálculo do percentual de progresso"""
        self.assertEqual(self.goal.progress_percentage, 50.0)
        
        # Testa meta zerada
        self.goal.target_value = 0
        self.assertEqual(self.goal.progress_percentage, 0)
        
        # Testa progresso maior que 100%
        self.goal.target_value = 100
        self.goal.current_value = 150
        self.assertEqual(self.goal.progress_percentage, 100.0)
    
    def test_commission_calculation(self):
        """Testa cálculo de comissão"""
        # Testa renovações com meta mínima atingida
        self.goal.goal_type = GoalType.RENEWALS
        self.goal.current_value = 120  # Acima de 100
        expected_commission = 120 * 3.0
        self.assertEqual(self.goal.commission_value, expected_commission)
        
        # Testa renovações abaixo da meta mínima
        self.goal.current_value = 80  # Abaixo de 100
        self.assertEqual(self.goal.commission_value, 0)
        
        # Testa upgrades
        self.goal.goal_type = GoalType.UPGRADES
        self.goal.current_value = 500
        self.assertEqual(self.goal.commission_value, 500)
        
        # Testa faturamento
        self.goal.goal_type = GoalType.REVENUE
        self.goal.current_value = 10000
        expected_commission = 10000 * 0.05
        self.assertEqual(self.goal.commission_value, expected_commission)
    
    def test_is_overdue(self):
        """Testa verificação de meta atrasada"""
        # Meta futura
        self.goal.end_date = date(2025, 12, 31)
        self.assertFalse(self.goal.is_overdue)
        
        # Meta passada
        self.goal.end_date = date(2023, 12, 31)
        self.assertTrue(self.goal.is_overdue)
        
        # Meta concluída não é atrasada
        self.goal.status = GoalStatus.COMPLETED
        self.assertFalse(self.goal.is_overdue)
    
    def test_days_remaining(self):
        """Testa cálculo de dias restantes"""
        # Meta futura
        self.goal.end_date = date(2025, 12, 31)
        days = self.goal.days_remaining
        self.assertGreater(days, 0)
        
        # Meta passada
        self.goal.end_date = date(2023, 12, 31)
        self.assertEqual(self.goal.days_remaining, 0)
    
    def test_to_dict(self):
        """Testa conversão para dicionário"""
        goal_dict = self.goal.to_dict()
        
        self.assertEqual(goal_dict['id'], 1)
        self.assertEqual(goal_dict['title'], 'Test Goal')
        self.assertEqual(goal_dict['goal_type'], 'renewals')
        self.assertEqual(goal_dict['status'], 'in_progress')
        self.assertIn('commission_value', goal_dict)


class TestGoalRepository(unittest.TestCase):
    """Testes para o repositório de metas"""
    
    def setUp(self):
        """Configuração inicial para os testes"""
        # Cria arquivo temporário para testes
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.write('[]')
        self.temp_file.close()
        
        # Mock do caminho do arquivo
        with patch.object(GoalRepository, '__init__', return_value=None):
            self.repository = GoalRepository()
            self.repository.data_file = self.temp_file.name
    
    def tearDown(self):
        """Limpeza após os testes"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_create_goal(self):
        """Testa criação de meta"""
        goal = Goal(
            id=0,
            title='Test Goal',
            description='Test Description',
            target_value=100,
            current_value=50,
            goal_type=GoalType.RENEWALS,
            status=GoalStatus.IN_PROGRESS,
            assigned_to='Test User',
            created_by='admin',
            start_date=date(2024, 1, 1),
            end_date=date(2024, 1, 31),
            created_at=None,
            updated_at=None
        )
        
        created_goal = self.repository.create(goal)
        
        self.assertEqual(created_goal.id, 1)
        self.assertIsNotNone(created_goal.created_at)
        self.assertIsNotNone(created_goal.updated_at)
    
    def test_get_all_goals(self):
        """Testa busca de todas as metas"""
        # Cria algumas metas de teste
        goals_data = [
            {
                'id': 1,
                'title': 'Goal 1',
                'description': 'Description 1',
                'target_value': 100,
                'current_value': 50,
                'goal_type': 'renewals',
                'status': 'in_progress',
                'assigned_to': 'User 1',
                'created_by': 'admin',
                'start_date': '2024-01-01',
                'end_date': '2024-01-31',
                'created_at': '2024-01-01T08:00:00',
                'updated_at': '2024-01-15T14:30:00'
            },
            {
                'id': 2,
                'title': 'Goal 2',
                'description': 'Description 2',
                'target_value': 200,
                'current_value': 100,
                'goal_type': 'upgrades',
                'status': 'completed',
                'assigned_to': 'User 2',
                'created_by': 'admin',
                'start_date': '2024-01-01',
                'end_date': '2024-03-31',
                'created_at': '2024-01-01T09:00:00',
                'updated_at': '2024-01-20T16:45:00'
            }
        ]
        
        with open(self.temp_file.name, 'w') as f:
            json.dump(goals_data, f)
        
        goals = self.repository.get_all()
        
        self.assertEqual(len(goals), 2)
        self.assertEqual(goals[0].title, 'Goal 1')
        self.assertEqual(goals[1].title, 'Goal 2')
    
    def test_get_by_id(self):
        """Testa busca de meta por ID"""
        goals_data = [
            {
                'id': 1,
                'title': 'Goal 1',
                'description': 'Description 1',
                'target_value': 100,
                'current_value': 50,
                'goal_type': 'renewals',
                'status': 'in_progress',
                'assigned_to': 'User 1',
                'created_by': 'admin',
                'start_date': '2024-01-01',
                'end_date': '2024-01-31',
                'created_at': '2024-01-01T08:00:00',
                'updated_at': '2024-01-15T14:30:00'
            }
        ]
        
        with open(self.temp_file.name, 'w') as f:
            json.dump(goals_data, f)
        
        goal = self.repository.get_by_id(1)
        self.assertIsNotNone(goal)
        self.assertEqual(goal.title, 'Goal 1')
        
        # Testa meta inexistente
        goal = self.repository.get_by_id(999)
        self.assertIsNone(goal)


class TestGoalService(unittest.TestCase):
    """Testes para o serviço de metas"""
    
    def test_goal_service_creation(self):
        """Testa criação do serviço"""
        service = GoalService()
        self.assertIsNotNone(service)
        self.assertIsNotNone(service.repository)
    
    def test_commission_calculation_logic(self):
        """Testa lógica de cálculo de comissão"""
        # Testa regra de renovações
        renewals_goal = Goal(
            id=1,
            title='Test Renewals',
            description='Test',
            target_value=100,
            current_value=120,  # Acima de 100
            goal_type=GoalType.RENEWALS,
            status=GoalStatus.IN_PROGRESS,
            assigned_to='Test',
            created_by='admin',
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        expected_commission = 120 * 3.0
        self.assertEqual(renewals_goal.commission_value, expected_commission)
        
        # Testa regra de upgrades
        upgrades_goal = Goal(
            id=2,
            title='Test Upgrades',
            description='Test',
            target_value=100,
            current_value=500,
            goal_type=GoalType.UPGRADES,
            status=GoalStatus.IN_PROGRESS,
            assigned_to='Test',
            created_by='admin',
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        self.assertEqual(upgrades_goal.commission_value, 500)


if __name__ == '__main__':
    unittest.main() 