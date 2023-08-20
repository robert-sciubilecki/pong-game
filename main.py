from turtle import Screen
from paddle import Paddle
from ball import Ball
from board import BoardPainter
import time
from score import Scoreboard, Info

WIDTH, HEIGHT = 1400, 600
PADDLE_LEFT_X, PADDLE_RIGHT_X = (WIDTH/2 - 50) * -1, (WIDTH/2 - 50)

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('pong')
screen.tracer(0)

board_painter = BoardPainter()
top_border, bottom_border = board_painter.paint_borders(WIDTH, HEIGHT)

paddle_right = Paddle(x=PADDLE_RIGHT_X, y=0, top_border=top_border, bottom_border=bottom_border)
paddle_left = Paddle(x=PADDLE_LEFT_X, y=0, top_border=top_border, bottom_border=bottom_border)

paddles = [paddle_left, paddle_right]

score_board_left = Scoreboard(-50)
score_board_right = Scoreboard(50)
info = Info(WIDTH, HEIGHT)

screen.listen()

screen.onkey(paddle_right.up, 'Up')
screen.onkey(paddle_right.down, 'Down')

screen.onkey(paddle_left.up, 'a')
screen.onkey(paddle_left.down, 'z')
# CAPS LOCK PROOF
screen.onkey(paddle_left.up, 'A')
screen.onkey(paddle_left.down, 'Z')

ball = Ball()


def animation(paddle, movement):
    if movement in range(1, 41):
        paddle.down(animation=True)
    elif movement in range(-40, 1):
        paddle.up(animation=True)
    paddle.decrease_movement()


def score(sleep=True):
    score_board_right.display_score()
    score_board_left.display_score()
    ball.reset_ball()
    paddle_left.reset_paddle()
    paddle_right.reset_paddle()
    if sleep:
        time.sleep(1)


game_on = True


def game():
    score_board_left.display_score()
    score_board_right.display_score()
    screen.update()
    time.sleep(1)
    screen.onkey(reset, 'r')
    screen.onkey(reset, 'R')

    screen.onkey(quit_game, 'q')
    screen.onkey(quit_game, 'Q')
    while game_on:
        if paddle_right.movement:
            animation(paddle_right, paddle_right.movement)
        if paddle_left.movement:
            animation(paddle_left, paddle_left.movement)

        ball.fly()
        time.sleep(0.0001)

        screen.update()

        ball_x, ball_y = ball.coordinates()
        if ball_x < PADDLE_LEFT_X + 30:
            if ball.contact(paddle_left):
                ball.bounce()
            if ball_x < PADDLE_LEFT_X - 20:
                score_board_right.increase_score()
                score()

        elif ball_x > PADDLE_RIGHT_X - 30:
            if ball.contact(paddle_right):
                ball.bounce()
            if ball_x > PADDLE_RIGHT_X + 20:
                score_board_left.increase_score()
                score()

        if ball_y == bottom_border:
            ball.bounce()
        elif ball_y == top_border:
            ball.bounce()


def reset():
    score_board_left.score = 0
    score_board_right.score = 0
    score(sleep=False)
    screen.update()
    game()


def quit_game():
    global game_on
    game_on = False


game()
