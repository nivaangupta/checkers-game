from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(board, depth, max_player, game):

    """ board -> The current board & the root node
        depth -> numeric value will be decremented
        max_player -> boolean value telling the algo to maximise or minimise score
        game -> game object that we will get from the basic game"""

    if depth == 0 or board.winner() is not None:
        return board.evaluate(), board

    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_all_moves(board, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_all_moves(board, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = move
        return min_eval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color, game):
    moves = []  # [[new_board, piece_moved] | if we move the piece the resulting board will look like board]
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


