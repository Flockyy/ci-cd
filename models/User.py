# # model.py

# from flask_sqlalchemy import SQLAlchemy
# from channel_app.views import app
# from flask_authorize import RestrictionsMixin, AllowancesMixin
# from flask_authorize import PermissionsMixin

# # Create database connection object
# db = SQLAlchemy(app)

# # mapping tables
# UserGroup = db.Table(
#     'user_group', db.Model.metadata,
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
# )

# UserRole = db.Table(
#     'user_role', db.Model.metadata,
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
# )

# # models
# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False, unique=True)

#     # `roles` and `groups` are reserved words that *must* be defined
#     # on the `User` model to use group- or role-based authorization.
#     roles = db.relationship('Role', secondary=UserRole)
#     groups = db.relationship('Group', secondary=UserGroup)

# class Group(db.Model, RestrictionsMixin):
#     __tablename__ = 'groups'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False, unique=True)

# class Role(db.Model, AllowancesMixin):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False, unique=True)

# class Article(db.Model, PermissionsMixin):
#     __tablename__ = 'articles'
#     __permissions__ = dict(
#         owner=['read', 'update', 'delete', 'revoke'],
#         group=['read', 'update'],
#         other=['read']
#     )

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), index=True, nullable=False)
#     content = db.Column(db.Text)
    
    
# import logging as lg

# def init_db():
#     db.drop_all()
#     db.create_all()
#     db.session.commit()
#     lg.warning('Database initialized!')
