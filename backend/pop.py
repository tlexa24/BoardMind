import os

# Root folder where BoardMind lives
ROOT = os.path.expanduser("~/Desktop/BoardMind")

# -------------------------
# Backend: minimal boilerplate
# -------------------------
backend_games = ["connect4", "tictactoe", "gomoku", "checkers", "battleship",
                 "dots"]

for game in backend_games:
    routes_path = os.path.join(ROOT, f"backend/games/{game}/routes.py")
    ai_path = os.path.join(ROOT, f"backend/games/{game}/ai.py")

    with open(routes_path, "w") as f:
        f.write(f"""from flask import Blueprint, jsonify
from .ai import get_ai_move

{game}_bp = Blueprint('{game}', __name__, url_prefix='/api/{game}')

@{game}_bp.route('/move', methods=['POST'])
def ai_move():
    move = get_ai_move()
    return jsonify({{"move": move}})
""")

    with open(ai_path, "w") as f:
        f.write(f"""def get_ai_move():
    # TODO: implement AI logic for {game}
    return 0  # placeholder move
""")

# -------------------------
# Frontend: minimal React boilerplate
# -------------------------
frontend_games = backend_games

# Pages
for game in frontend_games:
    page_path = os.path.join(ROOT,
                             f"frontend/src/pages/{game.capitalize()}Page.jsx")
    with open(page_path, "w") as f:
        f.write(f"""import React from 'react';
import Game from '../components/{game}/Game';

function {game.capitalize()}Page() {{
    return (
        <div>
            <h1>{game.capitalize()}</h1>
            <Game />
        </div>
    );
}}

export default {game.capitalize()}Page;
""")

# API stubs
for game in frontend_games:
    api_path = os.path.join(ROOT, f"frontend/src/api/{game}.js")
    with open(api_path, "w") as f:
        f.write(f"""export async function getAIMove(boardState) {{
    // TODO: implement API call to Flask for {game}
    return 0;
}}
""")

# Components
for game in frontend_games:
    board_path = os.path.join(ROOT,
                              f"frontend/src/components/{game}/Board.jsx")
    game_path = os.path.join(ROOT, f"frontend/src/components/{game}/Game.jsx")

    with open(board_path, "w") as f:
        f.write(f"""import React from 'react';

function Board() {{
    return <div>{game.capitalize()} Board Placeholder</div>;
}}

export default Board;
""")

    with open(game_path, "w") as f:
        f.write(f"""import React from 'react';
import Board from './Board';

function Game() {{
    return (
        <div>
            <h2>{game.capitalize()} Game Component</h2>
            <Board />
        </div>
    );
}}

export default Game;
""")

# -------------------------
# HomePage.jsx
# -------------------------
home_path = os.path.join(ROOT, "frontend/src/pages/HomePage.jsx")
with open(home_path, "w") as f:
    f.write("""import React from 'react';

function HomePage() {
    return (
        <div>
            <h1>BoardMind Home</h1>
            <p>Select a game to play or watch AI.</p>
        </div>
    );
}

export default HomePage;
""")

print("All files populated with minimal boilerplate!")
