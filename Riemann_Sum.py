######################################################################
# Author: Thy H. Nguyen
# Username: nguyent2
#
# Final Project P01: Riemann Sum of Linear functions from -5 to 5
#
#
# Purpose: A class for drawing a line graph and showing interactive with riemann sums and the definite integrals.
#  This program also demonstrate how turtle object responds to key press events.
#   the left arrow would draw the left-handed Riemann sum
#   the right arrow would draw the right-handed Riemann sum
#   the up arrow would delete (or erase) the left-handed Riemann sum and the calculation of the sum.
#   the down arrow would delete (or erase) the right-handed Riemann sum and the calculation of the sum.
#   the "i" key would calculate the integral of the function.
#   the "l" key would calculate the left-handed Riemann Sum of the function.
#   the "r" key would calculate the right-handed Riemann Sum of the function.
#   the "d" key would show the definition of the Definite Integrals.
#   the "g" key would show the gridlines for the graph.
#   the "h" key would show the guidlelines of all of the keys.
#   the "b" key would show the background back to lightgreen.
#   the "q" key would quit the application

######################################################################
# Acknowledgements:
# Calculus : Single And Multivariable
# by Hughes-Hallett, Deborah, McCallum, William G., Gleason, Andrew M., Flath, Daniel E., Lock, Patti Frazer
#
####################################################################################

import turtle

class Riemann_Sum:
    """
    A class to manufacture Riemann Sum and Line objects.
    """

    def __init__(self):
        """
         Initialize the screen and the interactive key press
        """

        self.wn = turtle.Screen()  # Get a reference to the window
        self.wn.setup(1300, 700)  # Determine the window size
        self.wn.title("Riemann Sum!")  # Change the window title
        self.wn.bgcolor("#ffff66")  # Set the background color


        self.draw_Ox_and_Oy()
        self.ask_function()
        self.write_function()
        self.draw_line()

        self.wn.onkey(self.draw_left_hand_sum,"Left")
        self.wn.onkey(self.draw_right_hand_sum, "Right")
        self.wn.onkey(self.undo_turtle_left, "Up")
        self.wn.onkey(self.undo_turtle_right, "Down")
        self.wn.onkey(self.integral, "i")
        self.wn.onkey(self.quit, "q")
        self.wn.onkey(self.sum_of_LHS,"l")
        self.wn.onkey(self.sum_of_RHS,"r")
        self.wn.onkey(self.definition,"d")
        self.wn.onkey(self.gridlines,"g")
        self.wn.onkey(self.guidelines,"h")
        self.wn.onkey(self.green_background,"b")

        self.wn.listen()
        self.wn.mainloop()



    def set_up_the_turtle(self, turtles):
        """
        This function sets up the turtle to initiate the coordinate axis
        :param turtles: the name of the coordinate axis
        Ox: the horizontal axis
        Oy: the vertical axis
        :return: None
        """
        turtles.pensize(2)
        turtles.speed(0)
        turtles.penup()
        turtles.goto(30, -20)  #Move the normal coordinate to 30 right, 20 down
                                # This means that the new (-6,0) is the old (30,-20)
        turtles.pendown()

    def draw_each_coordinate(self, turtles):
        """
        This function draws each coordinate
        :param turtles: the coordinate axis to draw
        :return: None
        """
        turtles.pensize(2)
        turtles.speed(0)
        turtles.left(180)
        turtles.stamp()
        turtles.right(180)
        for i in range(11):
            turtles.forward(50)
            turtles.left(90)
            turtles.forward(2)
            turtles.forward(-4)
            turtles.penup()
            turtles.forward(12)
            turtles.pendown()
            turtles.write(-5+i)
            turtles.penup()
            turtles.forward(-10)
            turtles.pendown()
            turtles.right(90)
        turtles.forward(50)
        turtles.stamp()

    def draw_Ox_and_Oy(self):
        """
        This funciton draws the Ox and Oy axis (horizontal axis and vertical axis respectively)
        :return: None
        """
        Ox = turtle.Turtle()
        Ox.pensize(2)
        self.set_up_the_turtle(Ox)
        self.draw_each_coordinate(Ox)
        Oy = turtle.Turtle()
        Oy.pensize(2)
        self.set_up_the_turtle(Oy)
        Oy.forward(300)
        Oy.left(90)
        Oy.forward(-300)
        self.draw_each_coordinate(Oy)

    def ask_function(self):
        """
        This function pops up a screen asking for the user's input for the function
        :return: None
        """
        wn = turtle.Screen()
        self.a = wn.numinput("The line equation Ax+By=C ", "         What is the value of A?             ")
        self.b = wn.numinput("The line equation Ax+By=C", "         What is the value of B?             ")
        self.c = wn.numinput("The line equation Ax+By=C", "         What is the value of C?             ")

    def write_function(self):
        """
        This function writes the function on the screen
        :return: None
        """
        turtles = turtle.Turtle()
        turtles.pensize(2)
        turtles.hideturtle()
        turtles.speed(0)
        turtles.color("#4d3399")
        turtles.penup()
        turtles.goto(-50, 20)
        turtles.pendown()


        if self.a == 0 and self.b==0:
            turtles.write("This value of A, B, and C does not make a line.",
                          move=False, align="left", font=("Arial", 16, "normal"))
        elif self.b == 0:
            x_coor = str(round((self.c / self.a),4))
            turtles.write("x = " + x_coor, move=False, align="left", font=("Arial", 16, "normal"))

        elif self.a ==0:
            x_coor = str(round((self.c / self.b), 4))
            turtles.write("y = " + x_coor, move=False,align="left",font=("Arial",16,"normal"))

        else:
            x_coor = str(round((-self.a / self.b), 4))
            y_coor = str(round((self.c / self.b), 4))
            turtles.write("y = " + x_coor + " x + " + y_coor, move=False,align="left",font=("Arial",16,"normal"))


    def draw_line(self):
        """
        Instantiates a Turtle object and draws the line on the Screen
        :return: None
        """
        turtles = turtle.Turtle()
        turtles.pensize(2)
        turtles.speed(0)
        turtles.shape("circle")
        turtles.shapesize(0.25, 0.25)
        turtles.color("#4d3399")

        if self.a == 0 and self.b ==0:
            turtles.hideturtle()
            turtles.write("This is not a valid function.",
                      move=False, align="left", font=("Arial", 12, "normal"))

        elif self.b==0:
            x = self.c/self.a
            if -5 <= x <= 5:
                turtles.penup()
                turtles.goto(30+(6+x)*50, - 20-50*5) #Go to the x position of y=-5
                turtles.stamp()
                turtles.pendown()
                turtles.goto(30+(6+x)*50, -20+50*5) #Go to the x position of y=5
                turtles.stamp()

            else:
                turtles.hideturtle()
                turtles.write("There is no x-value between -5 and 5 to draw.",
                      move=False, align="left", font=("Arial", 12, "normal"))

        elif self.a == 0:
            y = self.c / self.b
            if -5 <= y <= 5:
                turtles.penup()
                turtles.goto(30 + 50, y * 50 - 20)  # Go to the x position of y=-5
                turtles.stamp()
                turtles.pendown()
                turtles.goto(30 + 11 * 50, y * 50 - 20)  # Go to the x position of y=5
                turtles.stamp()

            else:
                turtles.hideturtle()
                turtles.write("There is no y-value between -5 and 5 to draw.",
                              move=False, align="left", font=("Arial", 16, "normal"))

        else:

            #The below is the revised code that makes sure that all points on the line are between -5 and 5 (Both the
            #y-value and the x-value). In mathematical terms, it is called that the function is only
            # mapping from [-5,5] to [-5.5]
            #However, since the riemann sum was based on the x-axis, the y-axis may exceed above 5 and below -5

            x1=0
            x2=0
            x3 = 0
            #Get 2 points to draw a line
            y1 =float(-self.a/self.b)*(x1)+float(self.c/self.b)
            y2 = float(-self.a / self.b) * (x2) + float(self.c / self.b)
            y3 = float(-self.a / self.b) * (x3) + float(self.c / self.b)

            if -5<=y1<=5:
                turtles.penup()
                turtles.goto(30 + (6 + x1) * 50, y1 * 50 - 20)
                turtles.pendown()
            while -5<=y2<=5 and -5<=x2<=5:
                turtles.goto(30 + (6 + x2) * 50, y2 * 50 - 20)
                x2 = x2-0.1
                y2 = float(-self.a / self.b) * (x2) + float(self.c / self.b)
            while -5<=y3<=5 and -5<=x3<=5:
                turtles.goto(30 + (6 + x3) * 50, y3 * 50 - 20)
                x3 += 0.1
                y3 = float(-self.a / self.b) * (x3) + float(self.c / self.b)


    def definition(self):
        """
        This function changes the background of the screen to the photo of the Definition of the definite integrals
        :return: None
        """
        wns = turtle.Screen()
        wns.bgpic("image/Definition_Of_Definite_Integral.png")

    def green_background(self):
        """
        This function changes the background of the screen to light green
        :return: None
        """
        wns = turtle.Screen()
        wns.bgpic("image/Light_green_background.png")

    def guidelines(self):
        """
        This function changes the background of the screen to the guidelines table of keys
        :return: None
        """
        wns = turtle.Screen()
        wns.bgpic("image/Guidelines.png")

    def gridlines(self):
        """
        This function changes the background of the screen to the gridlines
        :return: None
        """
        wns = turtle.Screen()
        wns.bgpic("image/Gridlines.png")

    def undo_turtle_left(self):
        """
        This function deletes (or erases) the left riemann sum (both the drawing and the calculation)
        :return: None
        """
        try:
            self.turtles2.undo()
            for i in range(10):
                self.turtles.undo()
            self.turtles2.hideturtle()
        except AttributeError:
            pass
    def undo_turtle_right(self):
        """
        This function deletes (or erases) the Right Riemann sum (both the drawing and the calculation)
        :return: None
        """
        try:
            self.turtles3.undo()
            for i in range(10):
                self.turtles1.undo()
            self.turtles3.undo()
        except AttributeError:
            pass

    def ask_rectangles(self):
        """
        This function asks for the number of rectangles (with equal width) to be divided into
        :return: None
        """

        wns=turtle.Screen()
        n = wns.numinput("Input for number of rectangles", " How many rectangles are you divided into?    ")
        return n

    def draw_right_hand_sum(self):
        """
        This function draws the rectangles of right-handed sum
        :return: None
        """
        self.n1 = self.ask_rectangles()
        self.n1=int(self.n1)
        self.wn.listen()
        self.turtles1 = turtle.Turtle()
        self.turtles1.pensize(2)
        self.turtles1.hideturtle()
        self.turtles1.pencolor("red")
        if self.b == 0:
            self.turtles1.write("There are no rectangles can be made.",
                              move=False, align="left", font=("Arial", 16, "normal"))
        else:
            self.turtles1.speed(0)
            self.turtles1.penup()
            self.turtles1.goto(30 + 50, -20)
            self.turtles1.pendown()

            for i in range(self.n1):
                self.turtles1.left(90)
                x = -5 + (10 / self.n1) * (i+1)
                height = (self.c - self.a * (x)) / self.b
                self.turtles1.forward(height * 50)
                self.turtles1.right(90)
                self.turtles1.forward(50*(abs(10/self.n1)))
                self.turtles1.right(90)
                self.turtles1.forward(height * 50)
                self.turtles1.left(90)

    def draw_left_hand_sum(self):
        """
        This function draws the rectangles of left-handed sum
        :return: None
        """
        self.n=self.ask_rectangles()
        self.n=int(self.n)
        self.wn.listen()
        self.turtles = turtle.Turtle()
        self.turtles.pensize(2)
        self.turtles.hideturtle()
        self.turtles.hideturtle()
        self.turtles.color("blue")

        if self.b ==0:
            self.turtles.penup()
            self.turtles.goto(-400,-300)
            self.turtles.write("There are no rectangles can be made.",
                                move=False, align="left", font=("Arial", 16, "normal"))

        else:


            self.turtles.speed(0)
            self.turtles.penup()
            self.turtles.goto(30 + 50,-20)
            self.turtles.pendown()
            for i in range(self.n):
                self.turtles.left(90)
                x = -5 + (10 / self.n) * (i)
                height = (self.c - self.a * (x)) / self.b
                self.turtles.forward(height * 50)
                self.turtles.right(90)
                self.turtles.forward(50*(abs(10/self.n)))
                self.turtles.right(90)
                self.turtles.forward(height * 50)
                self.turtles.left(90)

    def F(self,x1):
        """
        This function calculates the function F(x) such that the derivative of F(x) is f(x) at x
        :param x1: the point x to take the derivative
        :return: the value of F(x)
        """
        if self.a ==0 or self.b ==0:
            pass
        if self.b != 0:
            y1 = float(-self.a / self.b) * (x1*x1) * (1/2) + float(self.c / self.b)* x1
        return y1

    def integral(self):
        """
        This function calculates the integral
        :return: None
        """
        turtles = turtle.Turtle()
        turtles.pensize(2)
        turtles.penup()
        turtles.goto(-500,-100)
        turtles.pendown()
        if self.a == 0 or self.b ==0:
            turtles.write("This function is not in the form y=Ax+B (with A and B not qual to 0) to calculate the integral",
                          move=False, align="left", font=("Arial", 16, "normal"))
        if self.b != 0:
            integral = self.F(5)-self.F(-5)
            turtles.write("The integral from -5 to 5 of this function is " + str(integral),
                  move=False, align="left", font=("Arial", 16, "normal"))
        turtles.hideturtle()

    def sum_of_LHS(self):
        """
        This functions calculates the sum of the left-handed sum
        :return: None
        """
        self.turtles2 = turtle.Turtle()
        self.turtles2.pensize(2)
        self.turtles2.penup()
        self.turtles2.goto(-400, -200)

        if self.b ==0:
            self.turtles2.write("The left hand sum is 0, since there is no left hand sum.",
                            move=False, align="left", font=("Arial", 16, "normal"))

        else:
            sum = 0
            for i in range(self.n):
                x = -5 + (10 / self.n) * (i)
                height = (self.c - self.a * (x)) / self.b
                print("height",height)
                sum = sum + height
            lhs=sum*(10/self.n)


            self.turtles2.write("The left hand sum is " + str(lhs),
                      move=False, align="left", font=("Arial", 16, "normal"))
            self.turtles2.hideturtle()

    def sum_of_RHS(self):
        """
        This functions calculates the sum of the right-handed sum
        :return: None
        """
        self.turtles3 = turtle.Turtle()
        self.turtles3.pensize(2)
        self.turtles3.penup()
        self.turtles3.goto(-400, -250)

        if self.b ==0:
            self.turtles3.write("The right hand sum is 0, since there is no right hand sum.",
                            move=False, align="left", font=("Arial", 16, "normal"))

        else:
            sum = 0
            for i in range(self.n1):
                x = -5 + (10 / self.n1) * (i+1)
                height = (self.c - self.a * (x)) / self.b
                sum = sum + height

            rhs = sum * (10 / self.n1)

            self.turtles3.write("The right hand sum is " + str(rhs),
                      move=False, align="left", font=("Arial", 16, "normal"))
            self.turtles3.hideturtle()

    def quit(self):
        """
        This function helps quit the program
        :return: None
        """
        self.wn.bye()  # Close down the turtle window
