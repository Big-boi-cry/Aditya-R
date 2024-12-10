import turtle

t = turtle.Turtle()
t3 = turtle.Turtle()
t2 = turtle.Turtle()
t2.hideturtle()


screen = turtle.Screen()

screen.screensize(200,200,)



turtle.addshape("gaming.gif")
turtle.addshape("sarangi1.gif")
turtle.addshape("sarngi2.gif")
turtle.addshape("singham1.gif")
turtle.addshape("singham2.gif")
turtle.addshape("sleeping.gif")
turtle.addshape("soccer.gif")
turtle.addshape("youtube.gif")
turtle.addshape("volleyball.gif")
turtle.addshape("watching.gif")










screen.bgcolor("gold")

t.penup()

t.goto(0,150)

t.penup()
t3.penup()

t.write("INTRO", font=("silly monkey", 24, "bold"), align="center")

t3.fillcolor("orange")

t3.goto(80,50)
t3.begin_fill()
t3.pendown()
t3.forward(50)
t3.left(90)
t3.forward(50)
t3.left(90)
t3.forward(50)
t3.left(90)
t3.forward(50)
t3.end_fill()
t3.penup()


t.goto(0,125)


t.write("Aditya Ranapaily", font=("silly monkey", 12, "bold"), align= "center")

t.goto(0,100)

t.goto(0,0)


t.penup()

enter = input("Press enter to flip the page")






t.clear()
t3.clear()


t3.penup()
t3.goto(0,0)
t3.pendown()
t3.fillcolor("red")
t3.begin_fill()
t3.forward(100)
t3.left(90)
t3.forward(50)
t3.left(90)
t3.forward(100)
t3.left(90)
t3.forward(50)
t3.end_fill()



screen.bgcolor("green")

t.goto(0,175)

t.write("Favorite Foods", font=("silly monkey", 24, "bold"), align = "center")

turtle.addshape("cookie.gif")

turtle.addshape("momofood.gif")

turtle.addshape("somosa.gif")

t2.penup()

t2.goto(-200,75)

t2.shape("cookie.gif")

t2.stamp()

t.goto(-200,60)
t.write("cookie", font=("silly monkey", 12, "bold"), align= "center")

t2.shape("momofood.gif")

t2.goto(200,150)

t2.stamp()

t.goto(200,75)

t.write("momo food", font=("Times New Roman", 12, "bold"), align= "center")

t2.shape("somosa.gif")


t2.goto(0,-125)

t2.stamp()

t.goto(0,-200)

t.write("somosa", font=("silly monkey", 12, "bold"), align= "center")


enter = input("Press enter to flip the page")
t.clear()
t2.clear()
t3.clear()


screen.bgcolor("blue")

t.goto(0,175)
t.write("Hobbies", font=("Times New Roman", 24, "bold"), align = "center")

t2.showturtle()
t2.goto(-150,-50)
t2.shape("watching.gif")
t2.stamp()

t.goto(-50,-100)
t.write("watching movie", font=("silly monkey", 12, "bold"), align= "center")


t2.goto(-150,-150)
t2.shape("sleeping.gif")
t2.stamp()

t.goto(-50,-150)
t.write("sleeping", font=("silly monkey", 12, "bold"), align= "center")

t2.goto(-150,-250)
t2.shape("volleyball.gif")
t2.stamp()

t.goto(-50,-250)
t.write("volleyball", font=("silly monkey", 12, "bold"), align= "center")

t2.goto(-150,-0)
t2.shape("gaming.gif")
t2.stamp()

t.goto(-50,-0)
t.write("game", font=("silly monkey", 12, "bold"), align= "center")

t3.penup()

t3.pendown()
t3.fillcolor("yellow")
t3.begin_fill()
t3.circle(30,90)
t3.end_fill()
t3.penup()











enter = input("Press enter to flip the page")
t.clear()
t2.clearstamps()
t2.clear()

screen.bgcolor("light green")
t.goto(0,175)
t.write("Favorite Movie", font=("Times New Roman", 24, "bold"), align = "center")
t2.shape("sarangi1.gif")
t2.goto(0,-100)
t2.stamp()
t2.shape("sarngi2.gif")
t2.goto(100,-100)
t2.stamp()
t.goto(0,0)
t.write("Sarangi Nepali Movie", font=("Times New Roman", 24, "bold"), align = "center")



enter = input("Press enter to flip the page")
t.clear()
t2.clearstamps()
t3.clear()
screen.bgcolor("orange")
t.goto(0,175)
t.write("Fvorite Sport", font=("Times New Roman", 24, "bold"), align = "center")

t2.penup()
t2.goto(100,100)
t2.shape("volleyball.gif")
t2.stamp()
t.goto(100,150)
t.write("Volleyball", font=("Times New Roman", 24, "bold"), align = "center")
t2.shape("soccer.gif")
t2.goto(-100,100)
t2.stamp()
t.goto(-100,150)
t.write("Soccer", font=("Times New Roman", 24, "bold"), align = "center")


t.pendown()
t.fillcolor("green")
t.begin_fill()
t.circle(50)
t.end_fill()




turtle.done()








































