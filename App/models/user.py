from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    files = db.relationship('File', backref=db.backref('user'), lazy='joined')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        
    def __init__(self, username, password, admin):
        self.username = username
        self.set_password(password)
        self.admin = admin

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    def toggleAdmin(self):
        self.is_Admin = not self.is_Admin

