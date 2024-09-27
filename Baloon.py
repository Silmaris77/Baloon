from turtle import *

diameter = 40
pop_diameter = 100

def draw_baloon():
    color("red")
    dot(diameter)

def inflate_baloon():
       global diameter
       diameter = diameter + 10
       draw_baloon()

       if diameter >= pop_diameter:
            clear()
            diameter = 40
            write("POP!")
    
draw_baloon()

onkey(inflate_baloon, "Up")
listen()
done()
