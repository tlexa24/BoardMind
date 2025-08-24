from app import app, db
from models import GameStats

# Set up the application context
with app.app_context():
    db.create_all()
    print("Database tables created!")