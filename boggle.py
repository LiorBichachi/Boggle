import model
import gui
from boggle_board_randomizer import *


BOARD = randomize_board()
gui.BOARD = BOARD
model.board = BOARD

class Controller:
    def __init__(self, words_dict):
        self._gui = gui.Gui()
        self.board = BOARD
        self._model = model.BoggleModel(self.board, words_dict)

        for button in self._gui.total_buttons:
            if button == "PLAY AGAIN":
                action = self.play_again
                self._gui.set_button_cmd(button, action)
            else:
                action = self.create_button_action(button)
                self._gui.set_button_cmd(button, action)

    def create_button_action(self, button_text):
        def fun():
            self._model.type_in(button_text)
            self._gui.set_score_display(self._model.get_score())
            if self._gui.total_seconds != 0:
                self._gui.set_display(self._model.get_cur_word())
            self._gui.set_collected_words(self._model.get_collected_words())

        return fun

    def play_again(self):
        self.board = randomize_board()
        self._gui.set_board(self.board)
        self._model.set_collected(self.board)
        self._gui.create_buttons()
        self._model.clear()
        self._gui.set_display(self._model.get_cur_word())
        self._gui.play_again()
        for button in self._gui.total_buttons:
            if button == "PLAY AGAIN":
                action = self.play_again
                self._gui.set_button_cmd(button, action)
            else:
                action = self.create_button_action(button)
                self._gui.set_button_cmd(button, action)
        self._gui.run()


    def run(self):
        self._gui.run()


def dict2set (file_name):
    with open(file_name) as f:
        words = f.readlines()
        words_set = set(word.strip() for word in words)
    return words_set



def main():
    words_dict = dict2set("boggle_dict.txt")
    cont = Controller(words_dict)
    cont.run()

main()
