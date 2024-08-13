import turtle

t=turtle.Turtle()

t.goto(0,0)
arr=[50,75,100]
for i in arr:
    for j in range(4):
        t.circle(i)
        t.left(360/4)
    
  
turtle.exitonclick()
