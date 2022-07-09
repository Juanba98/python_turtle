import turtle
from time import sleep


turtle.bgcolor("black")

pointers = [turtle.Turtle(),turtle.Turtle()]
colors = ["#4C3A8E","#EED8E4","#8A6342"]
c = [1, 3]

turtle.tracer(20)
turtle.ht()


sleep(10)
#Inicializacion 
for index, i in enumerate(pointers):
	i.ht()
	i.width(3)
	i.pu()
	i. seth(90)
	i.bk(120* (c[index]))
	i.seth(0)
	i.pd()

for i in colors :
	pointers[0].color(i)
	pointers[1].color (i)
	turtle.color(i)
	for _ in range(360):
		for _ in range(13):
			pointers[0].fd(2)
			pointers[0].lt(1)
		turtle.pu()
		turtle.goto(pointers[0].pos())
		pointers[1].fd(c[1] * 2)
		pointers[1].lt(1)
		turtle.pd()
		turtle.goto(pointers[1].pos())


turtle.done()
