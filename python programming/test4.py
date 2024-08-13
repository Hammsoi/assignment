import turtle
t=turtle.turtles()


num=int(input("Enter the shape(3-tri, 4-rect, 5-penta, 6-hexa): "))


for i in range(num+1):
    for j in range(num):
        #t.move(100)
        t.left(360/num)
    t.left(360/(num+1))


