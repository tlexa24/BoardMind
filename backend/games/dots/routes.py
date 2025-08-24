from flask import Blueprint, jsonify
from .ai import get_ai_move

dots_bp = Blueprint('dots', __name__, url_prefix='/api/dots')

@dots_bp.route('/move', methods=['POST'])
def ai_move():
    move = get_ai_move()
    return jsonify({"move": move})
