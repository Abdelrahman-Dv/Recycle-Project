from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(256), nullable=True)
    message = db.Column(db.Text, nullable=True)
    services = db.Column(db.Text, nullable=True)  # For storing comma-separated services
    organization = db.Column(db.String(100), nullable=True)  # Added for registration form
    position = db.Column(db.String(100), nullable=True)  # Added for registration form
    registration_type = db.Column(db.String(20), nullable=True)  # To distinguish different registration types
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Add timestamp for when entry was created
    is_admin = db.Column(db.Boolean, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        if self.password_hash:
            return check_password_hash(self.password_hash, password)
        return False