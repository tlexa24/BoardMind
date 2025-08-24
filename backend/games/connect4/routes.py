from flask import Blueprint, jsonify
from .ai import get_ai_move

connect4_bp = Blueprint('connect4', __name__, url_prefix='/api/connect4')

@connect4_bp.route('/move', methods=['POST'])
def ai_move():
    move = get_ai_move()
    return jsonify({"move": move})
