from flask import Blueprint, jsonify
from .ai import get_ai_move

tictactoe_bp = Blueprint('tictactoe', __name__, url_prefix='/api/tictactoe')

@tictactoe_bp.route('/move', methods=['POST'])
def ai_move():
    move = get_ai_move()
    return jsonify({"move": move})
