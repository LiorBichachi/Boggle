from ex11_utils import *
from boggle_board_randomizer import *
# ALREADY_COLLECTED = 0
# NEW_WORD = 1
# NO_SUCH_WORD = 2
ILLEGAL_PATH = False
# WORDS_SET = ["word", "car"]
board = randomize_board()


class BoggleModel:

    def __init__(self, board, words):
        self.__board = board
        self.__words_set = words
        self.__cur_word = ""
        self.__cur_path = []
        self.__score = 0
        self.__collected_words = []
        self.__msg = ""

    def get_board(self):
        return self.__board

    def get_words_set(self):
        return self.__words_set

    def get_cur_word(self):
        return self.__cur_word

    def get_cur_path(self):
        return self.__cur_path

    def get_score(self):
        return self.__score

    def get_collected_words(self):
        return self.__collected_words

    def get_letters(self, coo):
        row = coo[0]
        col = coo[1]
        return self.get_board()[row][col]

    def set_collected(self, board):
        self.__collected_words = []
        self.__score = 0
        self.__board = board

    def get_msg (self):
        return self.__msg

    def get_coo_neighbors(self, coo):
        row = coo[0]
        col = coo[1]
        neighbors = []
        height = len(self.__board)
        width = len(self.__board[0])
        for r in range(-1, 2):
            for k in range(-1, 2):
                if -1 < row + r <= height and -1 < col + k <= width and (row + r,col + k) != coo:
                    neighbors.append((row + r, col + k))
        return neighbors

    def path_validation(self, coo):
        while self.__cur_path == []:
            return True
        last_coo = self.__cur_path[-1]
        last_coo_neighbors = self.get_coo_neighbors(last_coo)
        if coo in last_coo_neighbors and coo not in self.__cur_path:
            return True
        else:
            return False

    def collect_letters(self, coo):
        letters = self.get_letters(coo)
        self.__cur_word += letters
        self.__cur_path.append(coo)

    def remove_letters(self, coo):
        letters = self.get_letters(coo)
        last_added = len(letters)
        self.__cur_word = self.get_cur_word()[:-last_added]
        self.__cur_path.pop()

    def clear(self):
        self.__cur_word = ""
        self.__cur_path = []

    def raise_score(self):
        points = len(self.__cur_path) ** 2
        self.__score += points

    def submit(self):
        if self.__cur_word in self.__words_set:
            if self.__cur_word in self.__collected_words:  # if word already collected
                self.clear()
                self.__msg = "you already collected this word"
            else:
                self.__collected_words.append(self.__cur_word)  # if succeed to get new word
                self.raise_score()
                self.clear()
                self.__msg = "good job! you got new word!"
        self.clear()  # if the word is not in dictionary or pressed submit before collecting word
        self.__msg = "there is no such word"

    def type_in(self, user_input):
        self.__msg = ""
        if user_input == "SUBMIT":
            self.submit()
        elif user_input == "CLEAR":
            self.clear()
        else:
            coo = user_input
            if self.__cur_path == []:  # if it's first letter
                self.collect_letters(coo)
            elif coo == self.__cur_path[-1]:  # if player press twice in a row
                self.remove_letters(coo)
            elif self.path_validation(coo):  # if path is legal
                self.collect_letters(coo)
            else:  # if path is illegal
                self.__msg = "path is illegal! you can continue to neighbors only..."

