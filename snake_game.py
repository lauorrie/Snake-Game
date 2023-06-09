#importing libraries
import turtle
import random
import time


#creating turtle screen
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('white')



##creating a border for the game
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score system
score = 0
delay = 0.1


#making the actual snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'


#creating food yummy
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(30,30)

old_foods=[]



#scoring system pt2
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Courier",24,"bold"))


#how the sak gae moves
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_right():
    if snake.direction != "left":
        snake.direction = "right"
    
'''if_paused = False

def toggle_pause():
    global is_paused
    if if_paused == True:
        is_paused = False
    else:
        is_paused == True'''



def snake_moving():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    


# Keyboard bindings
screen.listen()
screen.onkeypress(snake_up, "Up")
screen.onkeypress(snake_down, "Down")
screen.onkeypress(snake_left, "Left")
screen.onkeypress(snake_right, "Right")
'''screen.onkeypress(toggle_pause, 'Escape')'''


#main game loop
while True:
        screen.update()
        
        #snake and fruits coliisions
        if snake.distance(food)< 20:
                x = random.randint(-290,270)
                y = random.randint(-240,240)
                food.goto(x,y)
                scoring.clear()
                score+=1
                scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
                delay-=0.001
                
                
                ## creating new_ball
                new_foods = turtle.Turtle()
                new_foods.speed(0)
                new_foods.shape('circle')
                new_foods.color('red')
                new_foods.penup()
                old_foods.append(new_foods)
                

        #adding ball to snake
        for index in range(len(old_foods)-1,0,-1):
                a = old_foods[index-1].xcor()
                b = old_foods[index-1].ycor()

                old_foods[index].goto(a,b)
                                     
        if len(old_foods)>0:
                a= snake.xcor()
                b = snake.ycor()
                old_foods[0].goto(a,b)
        snake_moving()


        ##snake and border collision    
        if snake.xcor()>280 or snake.xcor()< -300 or snake.ycor()>240 or snake.ycor()<-240:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('white')
                scoring.goto(0,0)
                scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        ## snake collision
        for foods in old_foods:
            if foods.distance(snake) < 20:
                time.sleep(1)
                screen.clear()
                screen.bgcolor('white')
                scoring.goto(0,0)
                scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))


        
   
        time.sleep(delay)

turtle.Terminator()
