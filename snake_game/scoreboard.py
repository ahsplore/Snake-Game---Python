from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Verdana', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updated_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over...', align=ALIGNMENT, font=FONT)