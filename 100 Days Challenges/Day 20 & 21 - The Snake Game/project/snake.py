# here we have all the classes required for the game initilized

import turtle as t
import random as rng

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MAX_AXIS = (300, -300)

class Snake:
    def __init__(self):
        ''' create the snake during initializtion, in my opinion, that is better.'''
        self.seg_1 = t.Turtle('square')
        self.seg_2 = t.Turtle('square')
        self.seg_3 = t.Turtle('square')
        self.snake = [self.seg_1, self.seg_2, self.seg_3]

        for part in self.snake:
            part.color('white')

        for seg in self.snake:
            seg.penup()

        # the starting position of the snake and the subsequent increased segements
        for seg in range(len(self.snake) + 1):
            if seg + 1 < len(self.snake):
                self.snake[seg + 1].setpos(self.snake[seg].pos()[0] - 20, self.snake[seg].pos()[1])

    def move(self):
        ''' keeps the snake moving foward without stopping'''
        for seg in range(len(self.snake) - 1 , 0, -1): # we use the range function to manipulate the loop to start from the last element of our list.
            x_cor = self.snake[seg - 1].xcor()
            y_cor = self.snake[seg - 1].ycor()
            self.snake[seg].goto(x_cor, y_cor) # we move the last segment to the postion of the second to last segment, and the second to last to the first
        self.snake[0].forward(MOVE_DISTANCE)

    # the below are the movement methods.
    def up(self):
        if self.snake[0].heading() == DOWN:
            pass
        else:
            self.snake[0].setheading(UP)
    def down(self):
        if self.snake[0].heading() == UP:
            pass
        else:
            self.snake[0].setheading(DOWN)
    def left(self):
        if self.snake[0].heading() == RIGHT:
            pass
        else:
            self.snake[0].setheading(LEFT)
    def right(self):
        if self.snake[0].heading() == LEFT:
            pass
        else:
            self.snake[0].setheading(RIGHT)

    def grow(self):
        new_seg = t.Turtle('square')
        new_seg.penup()
        new_seg.color('white')
        new_seg.speed('fastest')
        new_seg.goto(self.snake[-1].position()) # place it on the current tail so it doesn't show up at (0, 0) first
        self.snake.append(new_seg)

    def head_in_tail(self):
        for seg in self.snake[2:]:
            if self.seg_1.distance(seg) < 10:
                return True

class Food(t.Turtle):   # the food class inherets from the turtle class, but why is that needed?
    def __init__(self):
        '''we are inhereting from the super class, making us able to used the turtle class's methods in our constructor of the food class.
        remember that the init functino will always be called when an instance of the class is created.'''

        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid= 1)
        self.color('deepskyblue')
        self.speed('fastest')
        self.location()

    def location(self):
        '''sets and changes the food location after collision.'''
        rand_x = rng.randint(MAX_AXIS[1] // MOVE_DISTANCE + 1, MAX_AXIS[0] // MOVE_DISTANCE - 1) * MOVE_DISTANCE
        rand_y = rng.randint(MAX_AXIS[1] // MOVE_DISTANCE + 1, MAX_AXIS[0] // MOVE_DISTANCE - 1) * MOVE_DISTANCE
        self.goto(rand_x, rand_y)
        

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.update_scoreboard()        

    def update_scoreboard(self):
        self.write(f'the score is: {self.score}', align= 'center', font=('Arial', '18', 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f'the game is over, your score is {self.score}. ggs!', align= 'center', font= ('Arial', '24', 'normal'))


def main():
    pass
if __name__ == '__main__':
    main()
