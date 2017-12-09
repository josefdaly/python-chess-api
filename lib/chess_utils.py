import chess, random


PLAYER_HUMAN = 'player'
PLAYER_COMPUTER = 'computer'


# super simple for now
# ideally, this will be performed by a smart third party AI, because I don't really want to
#   implement a Chess AI from scratch. This will be fine for now.
def make_ai_move(board):
    move = random.choice([move.uci() for move in board.legal_moves])
    board.push_san(move)
    return board, move


def process_moves(moves, board):
    for move in moves:
        board.push_san(move)
    return board
    # if not board.is_game_over():
    #     move = random.choice([move.uci() for move in board.legal_moves])
    #     board.push_san(move)
    #     if board.is_game_over():
    #         return 'I win'
    #     return move
    # return 'you win'


def run_game(moves):
    board = process_moves(moves, chess.Board())
    if board.is_game_over():
        return {'move': None, 'winner': PLAYER_HUMAN}
    board, move = make_ai_move(board)
    if board.is_game_over():
        return {'move': move, 'winner': PLAYER_COMPUTER}
    return {'move': move, 'winner': None}
