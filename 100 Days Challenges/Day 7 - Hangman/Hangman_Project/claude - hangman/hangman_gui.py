import customtkinter as ctk

from game_logic import HangmanGame, DIFFICULTY_TIERS
from gallows_canvas import GallowsCanvas

ctk.set_appearance_mode('dark')

BG = '#1a1a1a'
CARD_BG = '#262626'
CARD_HOVER = '#2f2f2f'
ACCENT = '#2dd4bf'
ACCENT_HOVER = '#25a999'
TEXT = '#e5e5e5'
SUBTEXT = '#9ca3af'
ERROR = '#f87171'
SUCCESS = '#4ade80'
WARNING = '#fbbf24'

WINDOW_SIZE = '640x680'


class StartScreen(ctk.CTkFrame):
    def __init__(self, master, on_select):
        super().__init__(master, fg_color=BG)

        title = ctk.CTkLabel(
            self, text='HANGMAN', text_color=ACCENT,
            font=ctk.CTkFont(size=48, weight='bold'),
        )
        title.pack(pady=(90, 10))

        subtitle = ctk.CTkLabel(
            self, text='choose your difficulty', text_color=SUBTEXT,
            font=ctk.CTkFont(size=16),
        )
        subtitle.pack(pady=(0, 50))

        grid = ctk.CTkFrame(self, fg_color='transparent')
        grid.pack()

        for index, label in enumerate(DIFFICULTY_TIERS):
            row, col = divmod(index, 2)
            button = ctk.CTkButton(
                grid, text=label, width=200, height=80,
                corner_radius=16, fg_color=CARD_BG, hover_color=CARD_HOVER,
                border_width=2, border_color=ACCENT,
                text_color=TEXT, font=ctk.CTkFont(size=18, weight='bold'),
                command=lambda label=label: on_select(label),
            )
            button.grid(row=row, column=col, padx=12, pady=12)


class GameScreen(ctk.CTkFrame):
    def __init__(self, master, difficulty_label, on_replay, on_change_difficulty):
        super().__init__(master, fg_color=BG)

        self.on_replay = on_replay
        self.on_change_difficulty = on_change_difficulty
        self.game = HangmanGame(difficulty_label)

        top_bar = ctk.CTkFrame(self, fg_color='transparent')
        top_bar.pack(fill='x', padx=30, pady=(24, 0))

        ctk.CTkLabel(
            top_bar, text=difficulty_label, text_color=SUBTEXT,
            font=ctk.CTkFont(size=15, weight='bold'),
        ).pack(side='left')

        self.lives_label = ctk.CTkLabel(
            top_bar, text=f'Lives: {self.game.lives}', text_color=ACCENT,
            font=ctk.CTkFont(size=15, weight='bold'),
        )
        self.lives_label.pack(side='right')

        self.gallows = GallowsCanvas(self)
        self.gallows.pack(pady=(10, 10))

        self.word_label = ctk.CTkLabel(
            self, text=' '.join('_' for _ in self.game.word),
            text_color=TEXT, font=ctk.CTkFont(size=32, weight='bold'),
        )
        self.word_label.pack(pady=(0, 8))

        self.guessed_label = ctk.CTkLabel(
            self, text='Guessed: —', text_color=SUBTEXT,
            font=ctk.CTkFont(size=13),
        )
        self.guessed_label.pack(pady=(0, 6))

        self.feedback_label = ctk.CTkLabel(
            self, text='Type a letter and press Guess.', text_color=SUBTEXT,
            font=ctk.CTkFont(size=14),
        )
        self.feedback_label.pack(pady=(0, 16))

        input_row = ctk.CTkFrame(self, fg_color='transparent')
        input_row.pack(pady=(0, 10))

        self.entry = ctk.CTkEntry(
            input_row, width=160, height=42, corner_radius=10,
            fg_color=CARD_BG, border_color=ACCENT, text_color=TEXT,
            font=ctk.CTkFont(size=16), justify='center',
        )
        self.entry.pack(side='left', padx=(0, 10))
        self.entry.bind('<Return>', self._on_guess)
        self.entry.focus_set()

        self.guess_btn = ctk.CTkButton(
            input_row, text='Guess', width=100, height=42, corner_radius=10,
            fg_color=ACCENT, hover_color=ACCENT_HOVER, text_color='#0a0a0a',
            font=ctk.CTkFont(size=15, weight='bold'),
            command=self._on_guess,
        )
        self.guess_btn.pack(side='left')

        self.end_panel = ctk.CTkFrame(self, fg_color='transparent')

        self.end_banner = ctk.CTkLabel(
            self.end_panel, text='', font=ctk.CTkFont(size=22, weight='bold'),
        )
        self.end_banner.pack(pady=(10, 16))

        end_buttons = ctk.CTkFrame(self.end_panel, fg_color='transparent')
        end_buttons.pack()

        ctk.CTkButton(
            end_buttons, text='Play Again', width=150, height=44,
            corner_radius=10, fg_color=ACCENT, hover_color=ACCENT_HOVER,
            text_color='#0a0a0a', font=ctk.CTkFont(size=15, weight='bold'),
            command=lambda: self.on_replay(difficulty_label),
        ).pack(side='left', padx=8)

        ctk.CTkButton(
            end_buttons, text='Change Difficulty', width=170, height=44,
            corner_radius=10, fg_color=CARD_BG, hover_color=CARD_HOVER,
            border_width=2, border_color=ACCENT, text_color=TEXT,
            font=ctk.CTkFont(size=15, weight='bold'),
            command=self.on_change_difficulty,
        ).pack(side='left', padx=8)

    def _on_guess(self, event=None):
        if self.game.is_over:
            return

        letter = self.entry.get()
        result = self.game.guess(letter)
        self.entry.delete(0, 'end')

        clean = letter.strip().lower()
        messages = {
            'invalid': (f'Enter a single letter (a-z).', ERROR),
            'already_guessed': (f'You already tried "{clean}".', WARNING),
            'correct': (f'"{clean}" is correct!', SUCCESS),
            'wrong': (f'"{clean}" is wrong.', ERROR),
        }
        text, color = messages[result]
        self.feedback_label.configure(text=text, text_color=color)

        self._refresh_ui()

        if self.game.is_over:
            self._reveal_end_state()

    def _refresh_ui(self):
        self.word_label.configure(
            text=' '.join(letter.upper() for letter in self.game.display)
        )
        self.lives_label.configure(text=f'Lives: {self.game.lives}')
        guessed = ', '.join(sorted(self.game.guessed_letters)).upper()
        self.guessed_label.configure(text=f'Guessed: {guessed or "—"}')
        self.gallows.draw_stage(self.game.wrong_guesses)

    def _reveal_end_state(self):
        self.entry.configure(state='disabled')
        self.guess_btn.configure(state='disabled')

        self.word_label.configure(
            text=' '.join(letter.upper() for letter in self.game.word)
        )

        if self.game.is_won:
            self.end_banner.configure(text='YOU WON!', text_color=SUCCESS)
            self.feedback_label.configure(text='Nicely guessed.', text_color=SUCCESS)
        else:
            self.end_banner.configure(text='YOU LOSE', text_color=ERROR)
            self.feedback_label.configure(
                text=f'The word was "{self.game.word.upper()}".', text_color=ERROR
            )

        self.end_panel.pack(pady=(6, 20))


class HangmanApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Hangman')
        self.geometry(WINDOW_SIZE)
        self.configure(fg_color=BG)
        self.resizable(False, False)

        self.current_frame = None
        self.show_start_screen()

    def _switch_frame(self, frame):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame
        self.current_frame.pack(fill='both', expand=True)

    def show_start_screen(self):
        self._switch_frame(StartScreen(self, on_select=self.start_game))

    def start_game(self, difficulty_label):
        self._switch_frame(GameScreen(
            self, difficulty_label,
            on_replay=self.start_game,
            on_change_difficulty=self.show_start_screen,
        ))


if __name__ == '__main__':
    app = HangmanApp()
    app.mainloop()
