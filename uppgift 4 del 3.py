import turtle
#impoterar turtple
def rita_svenska_flaggan():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-45, 50)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
    turtle.end_fill()

def rita_danska_flaggan():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
    turtle.end_fill()

def rita_norska_flaggan():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-50, 20)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()
#dessa funktioner andvänder turtle.penup() och turtle.pendown för att guida pennan
#den flyttar start posetionen och bäljer färgern som är angiven och börjar fylla i med turtle.begin.fill()
#sen avslutas det med turtle.end_fill
#vi lägger in olika riktmärken med hjälp av .goto  
# Huvudprogram
val = input("Vilken flagga vill du rita? (svenska/danska/norska): ")

turtle.speed(2)  # Justera hastigheten på sköldpaddan

if val.lower() == "svenska":
    rita_svenska_flaggan()
elif val.lower() == "danska":
    rita_danska_flaggan()
elif val.lower() == "norska":
    rita_norska_flaggan()
else:
    print("Ogiltigt val av flagga!")

turtle.done()
#här frågar vi vilken av flaggorna vi ska rita via input vi har satt hastigheten till 2 med turple.speed(2) sen avslutas funktionen med turtle.done