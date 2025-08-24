from flask import Blueprint, jsonify
from .ai import get_ai_move

battleship_bp = Blueprint('battleship', __name__, url_prefix='/api/battleship')

@battleship_bp.route('/move', methods=['POST'])
def ai_move():
    move = get_ai_move()
    return jsonify({"move": move})
