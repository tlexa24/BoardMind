import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/boardmind_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
