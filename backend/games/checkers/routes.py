from flask import Blueprint, jsonify
from .ai import get_ai_move

checkers_bp = Blueprint('checkers', __name__, url_prefix='/api/checkers')

@checkers_bp.route('/move', methods=['POST'])
def ai_move():
    move = get_ai_move()
    return jsonify({"move": move})
