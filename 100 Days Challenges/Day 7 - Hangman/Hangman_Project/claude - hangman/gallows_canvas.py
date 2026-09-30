import tkinter as tk


class GallowsCanvas(tk.Canvas):
    BG = '#1a1a1a'
    LINE_COLOR = '#3f3f3f'
    FIGURE_COLOR = '#2dd4bf'
    LINE_WIDTH = 5

    def __init__(self, master, width=260, height=300, **kwargs):
        super().__init__(master, width=width, height=height,
                          bg=self.BG, highlightthickness=0, **kwargs)
        self.draw_stage(0)

    def draw_stage(self, wrong_guesses):
        wrong_guesses = max(0, min(6, wrong_guesses))
        self.delete('all')
        self._draw_gallows_structure()
        if wrong_guesses >= 1:
            self._draw_head()
        if wrong_guesses >= 2:
            self._draw_torso()
        if wrong_guesses >= 3:
            self._draw_left_arm()
        if wrong_guesses >= 4:
            self._draw_right_arm()
        if wrong_guesses >= 5:
            self._draw_left_leg()
        if wrong_guesses >= 6:
            self._draw_right_leg()

    def _draw_gallows_structure(self):
        self.create_line(40, 290, 160, 290, fill=self.LINE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)
        self.create_line(70, 290, 70, 30, fill=self.LINE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)
        self.create_line(70, 30, 180, 30, fill=self.LINE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)
        self.create_line(180, 30, 180, 60, fill=self.LINE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)

    def _draw_head(self):
        self.create_oval(155, 60, 205, 110, outline=self.FIGURE_COLOR,
                          width=self.LINE_WIDTH)

    def _draw_torso(self):
        self.create_line(180, 110, 180, 200, fill=self.FIGURE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)

    def _draw_left_arm(self):
        self.create_line(180, 140, 150, 180, fill=self.FIGURE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)

    def _draw_right_arm(self):
        self.create_line(180, 140, 210, 180, fill=self.FIGURE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)

    def _draw_left_leg(self):
        self.create_line(180, 200, 155, 250, fill=self.FIGURE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)

    def _draw_right_leg(self):
        self.create_line(180, 200, 205, 250, fill=self.FIGURE_COLOR,
                          width=self.LINE_WIDTH, capstyle=tk.ROUND)
