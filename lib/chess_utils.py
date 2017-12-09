import chess, random


PLAYER_HUMAN = 'player'
PLAYER_COMPUTER = 'computer'


# super simple for now
def make_ai_move(board):
    move = random.choice([move.uci() for move in board.legal_moves])
    board.push_san(move)
    return board, move


def process_moves(moves, board):
    for move in moves:
        board.push_san(move)
    return board


def run_game(moves):
    board = process_moves(moves, chess.Board())
    if board.is_game_over():
        return {'move': None, 'winner': PLAYER_HUMAN}
    board, move = make_ai_move(board)
    if board.is_game_over():
        return {'move': move, 'winner': PLAYER_COMPUTER}
    return {'move': move, 'winner': None}
