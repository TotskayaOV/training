

chess_board =[]


def checking_quarters(ferz_pos):
    """
    проверяет диагональное пересечние
    """
    global chess_board
    step = ferz_pos[1]
    if ferz_pos[0] != 0 and ferz_pos[1] != (len(chess_board)-1):
        for i in range(ferz_pos[0]-1, 0, -1):    # 1
            step += 1
            if chess_board[i][step] == 1:
                return False
            if step == len(chess_board)-1:
                break
    step = ferz_pos[1]
    if ferz_pos[0] != (len(chess_board)-1) and ferz_pos[1] != (len(chess_board)-1):
        for i in range(ferz_pos[0]+1, len(chess_board), 1):    # 4
            step += 1
            if chess_board[i][step] == 1:
                return False
            if step == len(chess_board)-1:
                break
    step = ferz_pos[1]
    if ferz_pos[0] != 0 and ferz_pos[1] != 0:
        for i in range(ferz_pos[0]-1, 0, -1):    # 2
            step -= 1
            if chess_board[i][step] == 1:
                return False
            if step == 0:
                break
    step = ferz_pos[1]
    if ferz_pos[0] != (len(chess_board) - 1) and ferz_pos[1] != 0:
        for i in range(ferz_pos[0] + 1, len(chess_board), 1):  # 3
            step -= 1
            if chess_board[i][step] == 1:
                return False
            if step == 0:
                break
    return True


def check_position(pos_queens):
    """
    проверяет вертикальное и горизонтальное пересечение
    """
    global chess_board
    if sum(chess_board[pos_queens[0]]) >= 1:
        return False
    for i in range(len(chess_board)):
        if chess_board[i][pos_queens[1]] == 1:
            return False
    return checking_quarters(pos_queens)


def creating_chessboard(len_board: int, list_placement: list):
    """
    создает матрицу с расстановкой ферзей
    """
    global chess_board
    chess_board = list_ = [[0 for _ in range(len_board)] for _ in range(len_board)]
    for elem in list_placement:
        i, j = elem
        chess_board[i-1][j-1] = 1


def checking_placement_queens(list_placement: list) -> bool:
    """
    поочередно проверяет каждую позицию
    """
    global chess_board
    for elem in list_placement:
        i, j = elem
        chess_board[i - 1][j - 1] = 0
        if check_position((i - 1, j - 1)) is False:
            return False
        else:
            chess_board[i - 1][j - 1] = 1
    return True

def start_pr(len_board: int, list_placement: list) -> bool:
    creating_chessboard(len_board, list_placement)
    return checking_placement_queens(list_placement)
