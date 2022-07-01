# models.py
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class User(UserMixin, db.Model):
    """User account model."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    sub = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    picture = db.Column(db.String(255))
    fullname = db.Column(db.String(255))

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )
        
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)