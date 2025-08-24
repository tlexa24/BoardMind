from flask import Blueprint, jsonify
from .ai import get_ai_move

gomoku_bp = Blueprint('gomoku', __name__, url_prefix='/api/gomoku')

@gomoku_bp.route('/move', methods=['POST'])
def ai_move():
    move = get_ai_move()
    return jsonify({"move": move})
