import json

from flask import Flask, request, jsonify

from lib.chess_utils import run_game


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/process_game', methods=['POST'])
    def process_game():
        move_sequence = json.loads(request.data)['moves']
        return jsonify(run_game(move_sequence))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
