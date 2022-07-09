import turtle

from time import sleep

turtle.bgcolor("black")

pointers = [turtle.Turtle(),turtle.Turtle()]

x = 3

colors = ["red","yellow","purple","white"]


#Inicializacion 
for index, i in enumerate(pointers):
	i.speed(0)
	i.color("black")
	i.shape("circle")
	i.shapesize(0.3)
	i.width(3)
	i.pu()
	i.seth(90)
	i.fd(350)
	i.seth(-180)
	i.pd()

pointers[0].pu()

turtle.delay(0)
turtle.speed(0)
turtle.ht()
sleep(4)


index = 0
for i in colors:
	turtle.color(i)
	for i in range(360):
		pointers[0].fd(x+index)
		pointers[0].lt(1+index)
		turtle.pu()
		turtle.goto(pointers[0].pos())
		turtle.pd()
		pointers[1].fd(2*(x))
		pointers[1].lt(2+index)
		turtle.goto(pointers[1].pos())
	index+=1
turtle.done()
