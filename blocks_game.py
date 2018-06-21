#Mark Joseph (mmj301)
import turtle
import random
t = turtle.Turtle()
wn = turtle.Screen()
turtle.setworldcoordinates(-250, -250, 250, 250)
wn.tracer(0)
t.hideturtle()

x, y, v, w, h, c, d = -200, -200, 4, 50, 50, 50,50
a,b = 250, 150#a and b are used for falling blocks
color1, color2 = 'blue', 'green'

#draw a rectangle with specific x & y start coordinates, width and height and color
def draw_rect(t, x, y, width, height, color='#7777aa'):
    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(0)
    for i in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def point_in_rectangle(x1,x2,y1,y2,a1,a2,b1,b2):
    if((b2<=y1 and x1>=a1 and x1 <=a2) or (b2<=y1 and x2>=a1 and x2 <=a2)):
        print('hittt')
        return True

def end_game():
    wn.bgcolor('black')

def next_frame():
    global x, v, a, b, w,h,c,d, color1, color2
    x += v#go in the positive x direction
    t.clear()



##################################PLAYER BLOCKS#######################################
    draw_rect(t, x, y, w, h, color1)#player movable one
    #if it hits the right wal go the other way
    if(x > 200):
        print("beyond right side")
        v = -v
    #we hit the eft wall so go other way, off by 50px
    if(x < -250):
        print("beyond left side")
        v = -v

####################################FALLING BLOCKS#######################################
    draw_rect(t, a, b, c, d, color2)
    b = b - 5

    #if we hit the block, we end the game
    if(point_in_rectangle(x, x+w, y, y-h, a, a+c, b, b-d)):
        color1 = 'red'
        end_game()
        return print('GAME OVER!!!!!!!!!!!!!!!!!!!')

    #after the block reaches the bottom of the screen do these things
    if b < -300:
        b = 250
        a = random.randint(-200,200)#change the x axis position of falling block
        c = random.randint(50,300)#change the width of the block

    wn.ontimer(next_frame, 20)
    wn.update()

#when the key is pressed we call this function which sets the axis in the -x direction
def handle_left():
    global v
    print('left pressed')
    v = -4

#when the key is pressed we call this function which sets the axis in the +x direction
def handle_right():
    global v
    print('right pressed')
    v = 4


wn.onkeypress(handle_left, 'Left')
wn.onkeypress(handle_right, 'Right')

next_frame()
wn.listen()
wn.mainloop()