import turtle

#Backgorund color
turtle.bgcolor("black")

turtle.pensize(2)
#Maximum speed
turtle.speed(0)


for colours in ["red","yellow","purple","white"]:
	for i in range(25):
		turtle.speed(0)
		turtle.color(colours)
		turtle.circle(100+(i*20))
		turtle.left(20)



turtle.hideturtle()
turtle.done()