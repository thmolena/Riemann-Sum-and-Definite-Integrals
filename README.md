# Riemann Sum of Linear functions from -5 to 5

**Term**: Fall 2019

**Author(s)**: T. H. Molena

**Section**: B

**References**: 
* Assignment T13
* Python » 3.3.7 Documentation » The Python Standard Library » 24. Program Frameworks » at 
https://docs.python.org/3.3/library/turtle.html?highlight=turtle 
* HTML Color Picker at https://www.w3schools.com/colors/colors_picker.asp
* The definition of Definite Integrals from Calculus : Single And Multivariable by Hughes-Hallett, Deborah, McCallum, 
William G., Gleason, Andrew M., Flath, Daniel E., Lock, Patti Frazer


---

## Milestone 1: Setup, Planning, Design

**Project Title**: Riemann Sum of Linear functions from -5 to 5. 

**Purpose**: The program will use Turtles to draw linear functions from Domain = [-5,5] to the Codomain = [-5,5] 
and then evaluate the left-handed Riemann Sum, right-handed Riemann Sum, compare with the Integral from -5 to 5
of the functions.

**Sources**: My final project is based on assignment T13.


**Completed CRC card for the class you will implement**:  
![alt text](/image/Final_CRC_card.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one")

---

## Milestone 2: Code

Updated coding part 1:

**Completion Percentage**: 25%

---

## Milestone 3: Virtual Check-in

Updated coding part 2

**Completion Percentage**: 50%


Updated coding part 3

**Completion Percentage**: 75%


Updated coding part 4

**Completion Percentage**: 100%

---

## Milestone 4: Final Code, Presentation, Demo


### User Instructions

This program is an educational tool helping the students having a smooth transition into Calculus II (from Calculus I
or any lower-level Math class). The program describes the relation between Riemann Sum (both right-handed sum and 
left-handed sum) and the integral (specifically the definite integral). Students (or educators) will have a chance to
input different value of n (which means different numbers of rectangles) and see the difference.

Once hitting the "Run" button, the Screen will pop up drawing the x-y coordinate. The program asks
the users to input for A,B, and C, and it will draw a graph of that linear function. After that, there is a guideline
with different options for the users to choose. Then, according to each user's choice, the program will answer that
question, whether to help the users (with the guidelines), or show the definition of definite integral, or even just 
show the left-handed and right-handed sum. However, the users have to make sure that some steps need to be done before
telling the program to jump into other step (For example, the user has to input the number of rectangles before 
finding the left-handed or right-handed sum).   

The step to step of this program is: The line needs to be drawn first. Then, it is to draw the left and right handed sum. 
After, the sum of the left-handed and right-handed is calculated. The integral of the function from -5 and 5 can also be
calculated at the same time. The next step is to erase (or delete) the old left-handed sum and right-handed sum (both 
the drawing and the calculation). After that, users can draw new left-handed sum and right-handed sum and recalculate
the new estimate of the integral (both new left-handed sum and right-handed sum). 

### Errors and Constraints

One of the technical problems with this program is that if any user clicks the wrong key on the keyboard (for example,
the users would find the sum of the left-handed sum before drawing the left-handed sum), the program will have an error.
The reason is that the users need to follow (strictly) from step to step in order not to cause the error.
The program also has a lot of errors regarding to the order of which step to come up with. The users have to strictly 
follow the step-by step so that the program will not produce any errors. 

Another technical problem is that this code still needs to be refactored. The reason is that there are a lot of similarities between the left handed sum
and the right handed sum and the algorithm in each one. However, currently, each similar step is inside a different
function in python. This makes the code being replicative and redundant too much. This code currently can be working for
different functions at a time. However, users have to run the code multiple times for different functions. No two different
functions can be working on a same screen, with the same coordinate systems, and graphs.

The first constraint from this program is that the turtle is sometimes visible on the screen.
Another constraint from this program is that the range is just from -5 to 5 (This means that the y-value is only from 
-5 to 5). Therefore, the visible errors are that the line just takes only x-value and y-value from -5 to 5. However, 
the riemann sum (both left-handed and right-handed) starts at x equals to -5 and ends at x equals to 5. This means 
that the rectangles actually have more than 90 percent (depends on the functions) that they will go over the line graph. 
The second constraint is that the gridlines are so "ugly", and they are, to some extent, not helpful. 
The gridlines may also make people confused about the points. Once the background of the program is turned
to green, there is also no way to turn the background color back to the initial yellow background.

### Reflection
**Why did you select the project that you did?** 

I have always loved Mathematics so much that I would love to teach other people Math. One specific topic I 
choose in Mathematics is Calculus. In this topic, the Fundamental Theorem of Calculus is such a powerful theorem 
that helps people so much with finding the exact integrals. Therefore, I chose this topic to show other non-math people.
However, as people may not have any background in Math, introducing them directly to the Fundamental Theorem of Calculus
may lead them to more confusion; those people may hate Math more as well. Therefore, I choose the preliminary topic of 
the Fundamental Theorem of Calculus in the Calculus book, which is about the Riemann Sum. Another reason why I choose 
this topic is because I saw that we already have a lot of interactive  books online for computer science, 
but there is not so many of that for mathematics. With those two reasons, I choose  such a math related project to the 
about the Riemann Sum and the Definite integrals.
 
**How closely did your final project reflect your initial design?**

I would love to use Riemann sum to explain for where the integrals and the Fundamental Theorem of Calculus are derived
from. Therefore, it is just the first part (or perhaps, the preliminary) of the integral, which is the definite integral. 
This topic may just have  touched the tip of the iceberg about the integrals topic in math. However, since I am not 
writing a program for all Mathematicians, or for all people who are really good at Math, since personally I think that 
my program is helpful to all students, even to those who do not really like Math. This final project was around 80% 
closely to what I decided to do at the beginning, which was to help those people who hate Math, or who are not good at 
Math have a smooth transition into the specific Calculus II class. With this preliminary step, I hope that non-math 
students will understand the integrals and the Fundamental Theorem of Calculus better.
 
**What did you learn from this process?**

Through this process, I could consolidate my knowledge about mathematics, especially about the Fundamental Theorem of 
Calculus. Then, I could have more practice with Classes and Objects. It was such an interesting process from the initial 
design to finally getting the final product. I learned more about turtles, and object-orientated programming. I also 
got more practice with thinking about the whole picture of coding (both the data structure, and the algorithm) before 
diving too deep into specific detail.   

**What was the hardest part of the final project?**

The hardest part of this final project was actually not coming from the coding part or the procedure to get the product.
The hardest part of this final project was indeed in coming up with the answer for the purpose of this program. At first,
I may have thought this would be the worst program for non-math people. The question "Who cares about the integrals? Who
cares about the Fundamental Theorem of Calculus" was always in my head. However, at the end, I was persistent and 
determined with this project. The reason is that as I  saw a lot of non-math students coming to my TA hours to ask me 
about Calculus, I thought that I needed to do something to help those students who are non-math majors understand, 
hopefully, to some extent of Calculus. 

**What would you do differently next time, knowing what you know now?**

For my next project, I would love to go forward with different theorems in mathematics, which may include the derivatives,
the Rolle's Theorem,  L'hopital's Rules and other topics in Mathematics. Those theorems are always useful for Calculus 
and computation in mathematics. I love to do this, since I did not only use python, but I also used Calculus and 
Mathematics through the process of coming up with the algorithm. I thought that I would not do much differently from
this time. I would still continue with exploring more about theoretical mathematics, pure mathematics and try to turn it
into something easier for non-math majors people who may need to use it in their fields, for example, physicists, or
chemists, or even computer scientists.
