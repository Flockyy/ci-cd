"""Routes for user authentication."""
import os
from flask import Blueprint, flash, redirect, url_for
from dotenv import load_dotenv
from . import login_manager
from .models import User, db

load_dotenv(override=True)

# Blueprint Configuration
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)
    
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    pass
    
@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("main_bp.index"))