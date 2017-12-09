import pytest, chess

from lib.chess_utils import process_moves


class TestProcessMoves(object):

    def test_process_moves_basic_case(self):
        processed_board = process_moves(['e2e4'], chess.Board())

        control_board = chess.Board()
        control_board.push_san('e2e4')

        assert sorted([move.uci() for move in processed_board.legal_moves]) == sorted([move.uci() for move in control_board.legal_moves])
