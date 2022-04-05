import random
import turtle

turtle.speed(0)
turtle.pensize(3)

turtle.Screen().bgcolor("black")

def pen(red):
    turtle.color(red)  
pen ('red')


    
def firework1(size):
    for num in range(20):
        turtle.forward(size)
        turtle.right(180-(360/20))
        
        

firework1(150)
    
        
        


def move():
    turtle.penup()
    x=random.randint(-150,150)
    y=random.randint(-150,150)
    turtle.goto(x,y)
    turtle.pendown()
    
    

move()
pen('yellow')
firework1(30)
move()
pen('blue')
firework1(57)
move()
pen('purple')
firework1(80)
move()
pen('lightblue')
firework1(120)
move()
pen('pink')
firework1(100)
move()
pen('orange')
firework1(54)
move()
pen('violet')
firework1(33)
move()
pen('green')
firework1(30)


move()
pen('magenta')
firework1(78)
move()
pen('chrome yellow')
firework1(65)
move()
pen('indigo')
firework1(150)
move()
pen('orange')
firework1(110)
move()
pen('red')
firework1(120)
move()
pen('gold')
firework1(65)
move()
pen('sprint green')
firework1(98)
move()
pen('aqua')
firework1(30)

move()
pen('magenta')
firework1(78)
move()
pen('chrome yellow')
firework1(65)
move()
pen('indigo')
firework1(150)
move()
pen('orange')
firework1(110)
move()
pen('red')
firework1(120)
move()
pen('gold')
firework1(65)
move()
pen('sprint green')
firework1(98)
move()
pen('aqua')
firework1(30)




