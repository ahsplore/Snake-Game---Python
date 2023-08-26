from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Verdana', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.updated_scoreboard()

    # def game_over(self):
        # self.goto(0, 0)
        # self.write('Game Over...', align=ALIGNMENT, font=FONT)

    def score_reset(self):
    if self.score > self.high_score:
        with open('data.txt', mode='w') as f:
            f.write(str(self.score))
        self.high_score = self.score
    self.score = 0
    self.updated_scoreboard()
