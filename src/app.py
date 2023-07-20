from flask import Flask, request, make_response
from utils import Moves, getMoves

app = Flask(__name__)


@app.route('/chess/<name>', methods = ["POST"])
def moves(name):
    try:
        positions = request.get_json()['positions']
        possible_moves = set()
        required_pos = set()
        for key, position in positions.items():
            func = getattr(Moves, key.lower())
            moves = func(position)
            
            if key.lower() != name:
                possible_moves = possible_moves.union(moves)
            else:
                required_pos = moves

        res = required_pos-possible_moves

        valid_moves = getMoves(res)
        return {'valid_moves': valid_moves}
    except Exception as e:
        resp = make_response({"error": "Internal Server Error!!!!!"})
        resp.status_code = 500

        return resp

# Run the Flask application
if __name__ == '__main__':
    app.run(host="0.0.0.0")