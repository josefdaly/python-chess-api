from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/process_game', methods=['POST'])
    def process_game():
        return 'Response'

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
