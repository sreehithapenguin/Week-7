import turtle,random

sc=turtle.Screen()
sc.setup(500,500)
sc.bgcolor("#d911aa")

ted= turtle.Turtle()
ted.shape("turtle")
ted.color("pink")
ted.speed(0)
ted.turtlesize(2)

ted.up()
ted.goto(-200,100)
ted.down()
ted.setheading(-90)
ted.pensize(5)
ted.fd(200)

ted.up()
ted.goto(150,0)
ted.down()
ted.circle(50)
ted.up()
ted.goto(165,-20)
ted.write("end", font=("Comic Sans MS",20))

ted.up()
ted.setheading(0)
ted.goto(-235,0)
ted.speed(2)
ted.color("purple")

def quiz():
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    guess=int(input("What is"+str(num1)+"plus"+str(num2)))
    if guess==num1+num2:
        print("Correct")
        return True
    else:
        print("Wrong")


while True:
    go=quiz()
    if go==True:
        ted.fd(100)
    if ted.xcor()>=150:
        print("YOU WIN WOO HOO!")
        break

