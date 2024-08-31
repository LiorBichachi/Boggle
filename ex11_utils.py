from typing import List, Tuple, Iterable, Optional
import boggle_board_randomizer
Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    word = ""
    for i, coord in enumerate(path):
        row = coord[0]
        col = coord[1]
        if i > 0:
            prev_coord = path[i - 1]
            if abs(row - prev_coord[0]) > 1 or (col - prev_coord[1]) > 1:
                return
        if row < 0 or row >= len(board) or col < 0 or col >= len(board):
            return
        word += board[row][col]
    if word in words:
        return word
    else:
        return


def in_board (coo, height, width):
    if -1 < coo[0] < height and -1 < coo[1] < width:
        return True
    else:
        return False

def coo_neighbors (coo,board):
    neighbors = []
    height = len(board)
    width = len(board[0])
    for r in range(-1, 2):
        for k in range(-1, 2):
            new_coo = (coo[0] + r, coo[1] + k)
            if in_board(new_coo, height, width) :
                neighbors.append(new_coo)
    return neighbors

def subsets(words):
    all_subsets = set()
    for word in words:
        for i in range(1,len(word)+1):
            all_subsets.add(word[:i])
    return all_subsets


def helper_paths(n, board, words, coo, subset, path=[], paths=[]):
    if not is_valid_path(board, path, subset):
        return paths
    if n == 1:
        if is_valid_path(board, path, words):
            paths.append(path.copy())
            # Make a copy of the path before appending
        return paths
    for neighbor in coo_neighbors(coo,board):
            if neighbor in path:
                continue
            path.append(neighbor)
            helper_paths(n - 1, board, words, neighbor, subset, path, paths)
            path.pop()  # Remove the last coordinate from the path after recursive call
    return paths


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    words = set(words)
    all_paths = []
    height = len(board)
    width = len(board[0])
    subset = subsets(words)
    for i in range(height):
        for j in range(width):
            coo = (i, j)
            path = ([(i, j)])
            all_paths.extend(helper_paths(n, board, words, coo, subset, path, []))
    return all_paths


def helper_words(n, board, words, coo, org_n, subset, word, path=[], paths=[]):
    if not is_valid_path(board, path, subset):
        return paths
    if word == org_n:
        if is_valid_path(board, path, words):
            paths.append(path.copy())  # Make a copy of the path before appending
        return paths
    if word > org_n:
        return
    for neighbor in coo_neighbors(coo, board):
        if neighbor in path:
            continue
        path.append(neighbor)
        word += len(board[neighbor[0]][neighbor[1]])
        helper_words(n - 1, board, words, neighbor, org_n, subset, word, path, paths)
        path.pop()  # Remove the last coordinate from the path after recursive call
        word -= len(board[neighbor[0]][neighbor[1]])

    return paths


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    n_len_words = {word for word in words if len(word) == n}
    all_paths = []
    height = len(board)
    width = len(board[0])
    subset = subsets(n_len_words)
    for i in range(height):
        for j in range(width):
            coo = (i, j)
            path = [(i, j)]
            word = len(board[i][j])
            all_paths.extend(helper_words(n, board, n_len_words, coo, n, subset, word, path, []))
    return all_paths


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    words = set(words)
    paths_list = []
    for i in range(len(board)*len(board[0])+1):
        paths_list.extend(find_length_n_paths(i, board, words))
    paths_dic ={}
    for path in paths_list:
        paths_dic[is_valid_path(board, path, words)] = path
    sum_lst = list(paths_dic.values())
    return sum_lst


