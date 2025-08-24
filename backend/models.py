from app import db

class GameStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(50), nullable=False)
    ai_wins = db.Column(db.Integer, default=0)
    human_wins = db.Column(db.Integer, default=0)
    draws = db.Column(db.Integer, default=0)