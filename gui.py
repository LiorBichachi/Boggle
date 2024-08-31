
import tkinter as tk
import boggle_board_randomizer


BOARD = boggle_board_randomizer.randomize_board()
BOARD_SIZE = len(BOARD)
REGULAR_COLOR = "slate blue"
GAME_TIME = 3


class Gui:
    total_seconds = GAME_TIME * 60
    total_buttons = dict()

    def __init__(self):
        root = tk.Tk()
        root.title("words game")
        root.geometry("800x600")
        root.resizable(False, False)
        self._main_window = root
        self.BOARD = BOARD
        self.BOARD_SIZE = BOARD_SIZE

        "#the open window"
        self._open_frame = tk.Label(root, bg=REGULAR_COLOR)
        self._open_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self._open_button = tk.Button(self._open_frame, text="START", font=("Arial", 30), command=self.open_main_window)
        self._open_button.pack()

        "#the collected words frame"
        self._collected_words_frame = tk.Frame(root, bg= REGULAR_COLOR, relief=tk.SOLID, borderwidth=1)
        self._title_score = tk.Label(self._collected_words_frame, text="SCORE:", font=("Ariel", 10), bg=REGULAR_COLOR)
        self._title_score.pack()
        self._score_label = tk.Label(self._collected_words_frame, bg=REGULAR_COLOR)
        self._score_label.pack()
        self._title_label = tk.Label(self._collected_words_frame, text="collected words", font=("Ariel", 10), bg=REGULAR_COLOR)
        self._title_label.pack()
        self._collected_label = tk.Label(self._collected_words_frame, bg=REGULAR_COLOR)
        self._collected_label.pack()

        "#the words frame"
        self._word_frame = tk.Frame(root, bg=REGULAR_COLOR, relief=tk.SOLID, borderwidth=1)
        self._display_label = tk.Label(self._word_frame, font=("Arial", 16), bg=REGULAR_COLOR)
        self._display_label.pack()
        self._submit_button = tk.Button(self._word_frame, text="SUBMIT")
        self.total_buttons["SUBMIT"] = self._submit_button
        self._submit_button.pack()
        self._clear_button = tk.Button(self._word_frame, text="CLEAR")
        self.total_buttons["CLEAR"] = self._clear_button
        self._clear_button.pack()

        "#the buttons frame"
        self._buttons_frame = tk.Frame(root)
        self.create_buttons()

        "#the close frame"
        self._close_button = tk.Button(self._collected_words_frame, text="PLAY AGAIN", font=("Arial", 10))
        self.total_buttons["PLAY AGAIN"] = self._close_button

        "# the timer's frame"
        self._time_frame = tk.Frame(root, bg= REGULAR_COLOR, relief=tk.SOLID, borderwidth=1)
        self._timer_value = tk.StringVar()
        self._timer_value.set(f"{GAME_TIME}: 00")
        self._timer_label = tk.Label(self._collected_words_frame, textvariable=self._timer_value)
        self._timer_label.pack(side=tk.BOTTOM)
        self._countdown()

    def open_main_window(self):
        self._open_frame.destroy()
        self._collected_words_frame.pack(side=tk.RIGHT, fill=tk.Y,  padx=10, pady=10)
        self._time_frame.pack(side=tk.TOP, fill=tk.X)
        self._word_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)
        self._buttons_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def close_main_window(self):
        self._close_button.pack(side=tk.BOTTOM)

    def play_again(self):
        self._close_button.forget()
        self._timer_label.forget()
        self.total_seconds = 0
        self.total_seconds = GAME_TIME * 60
        self._timer_label.pack(side=tk.BOTTOM)
        self._countdown()

    def set_board(self, board):
        self.BOARD = board
        self.BOARD_SIZE = len(board)
        self._collected_label["text"] = ""
        self._score_label["text"] = ""

    def create_buttons(self):
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                letter = self.BOARD[i][j]

                button = tk.Button(self._buttons_frame, text=letter, font=("Ariel", 9), borderwidth=4)
                button.grid(row=i, column=j, ipadx=73, ipady=40)
                self.total_buttons[(i, j)] = button

    def _countdown(self):
        minutes = self.total_seconds // 60
        seconds = self.total_seconds % 60
        self._timer_value.set(f"{minutes}:{seconds}")
        if self.total_seconds == 0:
            self.close_main_window()
            self.set_display("")

        if self.total_seconds > 0:
            self.total_seconds -= 1
            self._main_window.after(1000, self._countdown)

    def get_close_button(self):
        return self._close_button

    def get_buttons(self):
        return self.total_buttons

    def set_score_display(self, text):
        self._score_label["text"] = text

    def set_display(self, text):
        self._display_label["text"] = text

    def set_collected_words(self, text):
        self._collected_label["text"] = '\n'.join(text)

    def set_button_cmd(self, button_text, action):
        self.total_buttons[button_text]["command"] = action

    def run(self):
        self._main_window.mainloop()


if __name__ == '__main__':
    cg = Gui()
    cg.run()
