from time import sleep
from turtle import *


speed(10) #speed
color('green') #color circle
bgcolor('black') #color fount
hideturtle()
circle(1, 1, 1) #size
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1
done() #done

# github link: https://github.com/HappyRogelio7/PythonProyectCircletv1/
