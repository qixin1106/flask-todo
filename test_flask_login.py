#!/usr/bin/env python3
"""Test script to verify Flask-Login import"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import flask_login
    print("✓ Successfully imported flask_login")
    print(f"  Version: {flask_login.__version__}")
    
    # Test importing specific components
    from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
    print("✓ Successfully imported all required components from flask_login")
    
    # Test Flask app integration
    from flask import Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test-secret-key'
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    print("✓ Successfully initialized LoginManager")
    
    print("\nAll tests passed! Flask-Login is working correctly.")
    
except ImportError as e:
    print(f"✗ Failed to import flask_login: {e}")
    print(f"  Python path: {sys.path}")
    print(f"  Current directory: {os.getcwd()}")
    print(f"  Python version: {sys.version}")
    sys.exit(1)
