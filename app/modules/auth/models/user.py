"""
Wiki Veloz Fibra - User Model
Modelo de usuário para Flask-Login

@author: Matheus Gallina
@version: 1.0.0
@license: MIT
"""

from flask_login import UserMixin
from datetime import datetime
from app.core.config import Config
from app.core.database import DatabaseManager

class User(UserMixin):
    """User model for Flask-Login"""
    
    def __init__(self, id, username, name, role, created_at):
        self.id = id
        self.username = username
        self.name = name
        self.role = role
        self.created_at = created_at
    
    def get_id(self):
        """Return user ID for Flask-Login"""
        return str(self.id)
    
    def is_authenticated(self):
        """Check if user is authenticated"""
        return True
    
    def is_active(self):
        """Check if user is active"""
        return True
    
    def is_anonymous(self):
        """Check if user is anonymous"""
        return False
    
    def is_admin(self):
        """Check if user is admin"""
        return self.role == 'admin'
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID from real data"""
        try:
            config = Config()
            db_manager = DatabaseManager(config)
            user_data = db_manager.get_by_id('users.json', user_id)
            
            if user_data:
                return User(
                    id=user_data['id'],
                    username=user_data['username'],
                    name=user_data['name'],
                    role=user_data['role'],
                    created_at=user_data['created_at']
                )
        except Exception as e:
            print(f"Error loading user {user_id}: {e}")
        
        return None
    
    def to_dict(self):
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'role': self.role,
            'created_at': self.created_at
        }
    
    def __repr__(self):
        return f'<User {self.username}>'
