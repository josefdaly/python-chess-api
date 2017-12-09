import json

import pytest, chess
from flask import url_for


class TestProcessGameRoute(object):

    def test_basic_case_valid_moves(self, client):
        moves = {
            'moves': ['e2e4']
        }
        res = client.post(url_for('process_game'), data=json.dumps(moves))

        control_board = chess.Board()
        control_board.push_san('e2e4')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data['winner'] is None
        assert data['move'] in [move.uci() for move in control_board.legal_moves]
