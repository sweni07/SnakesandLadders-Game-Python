import random
import time
import turtle
global colour
global sum 
global sum2
global num2
global player2
global player1
board=turtle.Screen()
board.bgcolor("black")
t=turtle.Turtle ()
color=("black", "white")
t.screen.screensize(1000,1000)
t.pencolor("white")
t.penup()
t.setpos(500,-100)
t.pendown()
t.speed(70)
t.penup()
t.right(90)
t.forward(250)
t.left(90)
t.pendown()
t.forward(50)
t.left(180)
t.forward(750)
for i in range(3):
  t.right(90)
  t.forward(750)
for i in range (5):
  t.right(90)
  t.forward(75)
  t.right(90)
  t.forward(750)
  t.left(90)
  t.forward(75)
  t.left(90)
  t.forward(750)
t.left(180)
for i in range(5):
  t.forward(75)
  t.right(90)
  t.forward(750)
  t.left(90)
  t.forward(75)
  t.left(90)
  t.forward(750)
  t.right(90)
t.pencolor("black")
t.right(90)
t.forward(10)
t.right(90)
t.forward(20)
t.left(90)
num=101
for i in range(5):
  for i in range(10): 
    num=num-1
    t.begin_fill
    t.color("white")
    t.write(num, font=("Arial", 10, "normal"))
    t.end_fill
    t.pencolor("black")
    t.forward(75)
  t.right(90) 
  t.forward(75) 
  t.right(90) 
  t.forward(75)
  for i in range(10):
    num=num-1
    t.begin_fill
    t.color("white")
    t.write(num, font=("Arial", 10, "normal"))
    t.end_fill
    t.pencolor("black")
    t.forward(75)
  t.left(90)
  t.forward(75)
  t.left(90) 
  t.forward(75)
t2=turtle.Turtle()
t2.speed(70)
t2.screen.screensize(1000,1000)
t2.pencolor("yellow")
t2.penup()
t2.setpos(500,-100)
t2.pendown()
t2.penup()
t2.right(180)
t2.forward(527)
t2.left(90)
t2.forward(225)
t2.pendown()
t2.left(200)
t2.forward(230)
t2.penup()
t2.right(110)
t2.forward(30)
t2.right(70)
t2.pendown()
t2.forward(230)
t2.left(180)
for i in range(3):
  t2.forward(35)
  t2.left(90)
  t2.forward(28)
  t2.right(90)
  t2.forward(35)
  t2.right(90)
  t2.forward(28)
  t2.left(90)
t2.hideturtle()
  
t3=turtle.Turtle() 
t3.speed(70)
t3.pencolor("yellow")
t3.screen.screensize(1000,1000)
t3.penup()
t3.setpos(500,-100)
t3.pendown()
t3.penup()
t3.right(180)
t3.forward(77)
t3.left(90)
t3.forward(225)
t3.pendown()
t3.left(157)
t3.forward(175)
t3.penup()
t3.right(67)
t3.forward(30)
t3.pendown()
t3.right(112)
t3.forward(175)
t3.right(180)
for i in range(2):
  t3.forward(35)
  t3.left(90)
  t3.forward(28)
  t3.right(90)
  t3.forward(35)
  t3.right(90)
  t3.forward(28)
  t3.left(90)
t3.hideturtle()
  
t4=turtle.Turtle()
t4.pencolor("yellow")
t4.screen.screensize(1000,1000)
t4.penup()
t4.setpos(500,-100)
t4.pendown()
t4.speed(70)
t4.penup()
t4.right(180)
t4.forward(150)
t4.right(45)
t4.pendown()
t4.forward(635)
t4.right(135)
t4.penup()
t4.forward(40)
t4.pendown()
t4.right(45)
t4.forward(635)
t4.right(180)
for i in range(7):
  t4.forward(45)
  t4.left(90)
  t4.forward(28)
  t4.right(90)
  t4.forward(45)
  t4.right(90)
  t4.forward(28)
  t4.left(90)
t4.hideturtle()

t5=turtle.Turtle()
t5.pencolor("yellow")
t5.screen.screensize(1000,1000)
t5.penup()
t5.setpos(500,-100)
t5.pendown()
t5.speed(70)
t5.penup()
t5.right(180)
t5.forward(685)
t5.right(115)
t5.pendown()
t5.forward(180)
t5.right(65)
t5.penup()
t5.forward(35)
t5.pendown()
t5.right(115)
t5.forward(180)
t5.right(180)
for i in range(2):
  t5.forward(35)
  t5.left(90)
  t5.forward(31)
  t5.right(90)
  t5.forward(35)
  t5.right(90)
  t5.forward(31)
  t5.left(90)
t5.hideturtle()

  
t6=turtle.Turtle()
t6.pencolor("yellow")
t6.screen.screensize(1000,1000)
t6.penup()
t6.setpos(500,-100)
t6.pendown()
t6.speed(70)
t6.penup()
t6.left(90)
t6.forward(150)
t6.pendown()
t6.left(70)
t6.forward(250)
t6.penup()
t6.right(90)
t6.forward(35)
t6.right(90)
t6.pendown()
t6.forward(250)
t6.right(180)
for i in range(3):
  t6.forward(35)
  t6.left(90)
  t6.forward(35)
  t6.right(90)
  t6.forward(35)
  t6.right(90)
  t6.forward(35)
  t6.left(90)
t6.hideturtle()
  
t7=turtle.Turtle()
t7.pencolor("yellow")
t7.screen.screensize(1000,1000)
t7.penup()
t7.setpos(500,-100)
t7.pendown()
t7.speed(70)
t7.penup()
t7.left(90)
t7.forward(310)
t7.left(90)
t7.forward(225)
t7.pendown()
t7.right(45)
t7.forward(220)
t7.penup()
t7.right(90)
t7.forward(35)
t7.right(90)
t7.pendown()
t7.forward(220)
t7.right(180)
for i in range(3):
  t7.forward(30)
  t7.left(90)
  t7.forward(35)
  t7.right(90)
  t7.forward(30)
  t7.right(90)
  t7.forward(35)
  t7.left(90)
t7.hideturtle()
  
t8=turtle.Turtle()
t8.pencolor("blue")
t8.screen.screensize(1000,1000)
t8.penup()
t8.setpos(500,-100)
t8.pendown()
t8.width(5)
t8.speed(70)
t8.penup()
t8.right(90)
t8.forward(65)
t8.right(90)
t8.forward(445)
t8.pendown()
t8.circle(8)
t8.penup()
t8.width(7)
t8.left(90)
t8.forward(8)
t8.left(90)
t8.forward(8)
t8.pendown()
t8.forward(115)
t8.penup()
t8.right(70)
t8.pendown()
t8.forward(75)
t8.left(50)
t8.pendown()
t8.forward(70)
t8.right(30)
t8.forward(50)
t8.hideturtle()

t9=turtle.Turtle()
t9.pencolor("blue")
t9.screen.screensize(1000,1000)
t9.penup()
t9.setpos(500,-100)
t9.pendown()
t9.width(7)
t9.speed(70)
t9.penup()
t9.right(180)
t9.forward(225)
t9.pendown()
t9.right(45)
t9.forward(15)
t9.right(90)
t9.forward(70)
t9.left(90)
t9.forward(70)
t9.right(90)
t9.forward(45)
t9.width(5)
t9.penup()
t9.right(45)
t9.forward(8)
t9.pendown()
t9.circle(8)
t9.hideturtle()

t10=turtle.Turtle()
t10.pencolor("blue")
t10.screen.screensize(1000,1000)
t10.penup()
t10.setpos(500,-100)
t10.pendown()
t10.width(7)
t10.speed(70)
t10.penup()
t10.right(180)
t10.forward(675)
t10.right(90)
t10.forward(180)
t10.pendown()
t10.right(90)
t10.forward(85)
t10.left(45)
t10.forward(35)
t10.right(35)
t10.forward(80)
t10.left(35)
t10.forward(30)
t10.penup()
t10.right(55)
t10.forward(8)
t10.pendown()
t10.circle(8)
t10.hideturtle()

t11=turtle.Turtle()
t11.pencolor("blue")
t11.screen.screensize(1000,1000)
t11.penup()
t11.setpos(500,-100)
t11.pendown()
t11.width(7)
t11.speed(70)
t11.penup()
t11.right(180)
t11.forward(590)
t11.right(90)
t11.forward(10)
t11.right(90)
t11.left(65)
t11.pendown()
t11.forward(165)
t11.right(45)
t11.forward(170)
t11.left(45)
t11.forward(170)
t11.penup()
t11.right(45)
t11.forward(8)
t11.pendown()
t11.circle(8)
t11.hideturtle()

t12=turtle.Turtle()
t12.pencolor("blue")
t12.screen.screensize(1000,1000)
t12.penup()
t12.setpos(500,-100)
t12.pendown()
t12.speed(70)
t12.width(7)
t12.penup()
t12.right(180)
t12.right(90)
t12.forward(225)
t12.pendown()
t12.left(40)
t12.forward(155)
t12.right(45)
t12.forward(75)
t12.left(45)
t12.forward(50)
t12.right(45)
t12.penup()
t12.forward(8)
t12.pendown()
t12.circle(8)
t12.hideturtle()

t13=turtle.Turtle()
t13.penup()
t13.setpos(-170,-300)
t13.pendown()
t14=turtle.Turtle()
t14.penup()
t14.setpos(-170, -320)
t14.pendown()
def main():
    pick_color()
    dice_roll()  
print("Welcome to Snakes And Ladders!\n", "What colour do you want your piece to be?")
print("This game is just like a classic game of Snakes and Ladders, and requires two people to play it")
print("Just follow the instructions as the game goes along, and try your luck. Get to the 100 before your opponent!")
print("Good Luck, let the games begin!")   
def pick_color():
  global player1
  player1=str(input("Player 1, enter your name:"))
  print(player1 ," pick a color")
  x=1
  while x==1:
      colour=int(input("Enter 1 for blue, 2 for green, 3 for red, and 4 for yellow:"))
      if colour==1:
        t13.begin_fill
        t13.color("blue")
        t13.end_fill
        x=0
      elif colour==2:
        t13.begin_fill
        t13.color("green")
        x=0
      elif colour==3:
        t13.begin_fill
        t13.color("red")
        x=0
      elif colour==4:
        t13.begin_fill
        t13.color("yellow")
        x=0
      else:
        print("Invalid colour, choose one of the following")
        x=0
        pick_color()
      pick_color2(colour)
      print(player1 , "goes first")
            
  #this loops helps run through the turns until either of the players reach 100
sum=1
def dice_roll():
    global player1
    print(player1 , "roll")
    x=1
    global sum
    while x==1:
        roll=int(input("Enter 1 to roll the dice:"))
        if roll==1:
            num=int(random.randint(1,6))
            print("You rolled",num)
            x=0
        else:
            print("Invalid Input. Enter 1 to roll")
            x=1
            x=x-1
            dice_roll()
        if (sum+num) <= 100:
            for i in range(0, num):
                move()
            if sum==3:
                t13.penup()
                t13.left(90)
                t13.forward(220)
                t13.left(90)
                t13.forward(75)
                t13.pendown()
                sum=sum+36
            elif sum==9:
                t13.penup()
                t13.left(90)
                t13.forward(150)
                t13.right(90)
                t13.forward(75)
                t13.pendown()
                sum=sum+21
            elif sum==33:
                t13.penup()
                t13.right(90)
                t13.forward(450)
                t13.left(90)
                t13.forward(450)
                t13.pendown()
                sum=sum+66
            elif sum==40:
                t13.penup()
                t13.right(90)
                t13.forward(150)
                t13.right(90)
                t13.forward(75)
                t13.right(180)
                t13.pendown()
                sum=sum+19
            elif sum==51:
                t13.penup()
                t13.right(90)
                t13.forward(75)
                t13.left(90)
                t13.forward(225)
                t13.right(180)
                t13.pendown()
                sum=sum+16
            elif sum==74:
                t13.penup()
                t13.right(90)
                t13.forward(150)
                t13.left(90)
                t13.forward(150)
                t13.pendown()
                sum=sum+22
            elif sum==93:
                t13.penup()
                t13.left(90)
                t13.forward(225)
                t13.left(90)
                t13.forward(150)
                t13.pendown()
                sum=sum-23
            elif sum==86:
                t13.penup()
                t13.right(90)
                t13.forward(375)
                t13.right(90)
                t13.forward(300)
                t13.pendown()
                sum=sum-47
            elif sum==64:
                t13.penup()
                t13.right(90)
                t13.forward(75)
                t13.right(90)
                t13.forward(225)
                t13.pendown()
                sum=sum-4
            elif sum==54:
                t13.penup()
                t13.left(90)
                t13.forward(150)
                t13.right(90)
                t13.pendown()
                sum=sum-20
            elif sum==24:
                t13.penup()
                t13.right(90)
                t13.forward(150)
                t13.left(90)
                t13.forward(225)
                t13.pendown()
                sum=sum-17
        if sum == 100:
          print("Congratulations", player1, "you won!")
          print("To play again press F5 and run the game again")
          exit()
        if num==6:
          dice_roll()
        else:
          dice_roll2()

#this function is called the number of times the dice is rolled
#this function helps with turns, and determine where to turn, everytime a number is rolled it adds to the sum
def move():
    global sum
    if(sum % 10 == 0):
        if(sum % 20 == 0):
            t13.penup()
            t13.right(90)
            t13.forward(75)
            t13.right(90)
            t13.penup()

        else:
            t13.penup()
            t13.left(90)
            t13.forward(75)
            t13.left(90)
            t13.penup()
    else:
      t13.penup()
      t13.forward(75)
      t13.penup()
    sum = sum + 1
    
def pick_color2(colour):
    global player2
    player2=str(input("Player 2, enter your name:"))
    print(player2, " pick a color")
    x=1
    while x==1:
        colour2=int(input("Enter 1 for blue, 2 for green, 3 for red, and 4 for yellow:"))
        if colour2==1:
          t14.begin_fill
          t14.color("blue")
          t14.end_fill
          x=0
        elif colour2==2:
          t14.begin_fill
          t14.color("green")
          x=0
        elif colour2==3:
          t14.begin_fill
          t14.color("red")
          x=0
        elif colour2==4:
          t14.begin_fill
          t14.color("yellow")
          x=0
        else:
            print("Invalid colour, choose one of the following")
            x=1
            x=x-1
            pick_color2(colour)
        if colour2==colour:
          print("Colour picked by Player 1, pick another color")
          x=1
          x=x-1
          pick_color2(colour)   
    dice_roll()
sum2=1
def dice_roll2():
    global player2
    print(player2 , "roll")
    x=1
    global sum2
    while x==1:
        roll2=int(input("Enter 1 to roll the dice:"))
        if roll2==1:
            num2=int(random.randint(1,6))
            print("You rolled",num2)
            x=0
        else:
            print("Invalid Input. Enter 1 to roll")
            x=1
            x=x-1
            dice_roll2()
        if (sum2+num2)<=100:
            for i in range(0, num2):
                move2()
            if sum2==3:
                t14.penup()
                t14.left(90)
                t14.forward(220)
                t14.left(90)
                t14.forward(75)
                t14.pendown()
                sum2=sum2+36
            elif sum2==9:
                t14.penup()
                t14.left(90)
                t14.forward(150)
                t14.right(90)
                t14.forward(75)
                t14.pendown()
                sum2=sum2+21
            elif sum2==33:
                t14.penup()
                t14.right(90)
                t14.forward(450)
                t14.left(90)
                t14.forward(450)
                t14.pendown()
                sum2=sum2+66
            elif sum2==40:
                t14.penup()
                t14.right(90)
                t14.forward(150)
                t14.right(90)
                t14.forward(75)
                t14.right(180)
                t14.pendown()
                sum2=sum2+19
            elif sum2==51:
                t14.penup()
                t14.right(90)
                t14.forward(75)
                t14.left(90)
                t14.forward(225)
                t14.right(180)
                t14.pendown()
                sum2=sum2+16
            elif sum2==74:
                t14.penup()
                t14.right(90)
                t14.forward(150)
                t14.left(90)
                t14.forward(150)
                t14.pendown()
                sum2=sum2+22
            elif sum2==93:
                t14.penup()
                t14.left(90)
                t14.forward(225)
                t14.left(90)
                t14.forward(150)
                t14.pendown()
                sum2=sum2-23
            elif sum2==86:
                t14.penup()
                t14.right(90)
                t14.forward(375)
                t14.right(90)
                t14.forward(300)
                t14.pendown()
                sum2=sum2-47
            elif sum2==64:
                t14.penup()
                t14.right(90)
                t14.forward(75)
                t14.right(90)
                t14.forward(225)
                t14.pendown()
                sum2=sum2-4
            elif sum2==54:
                t14.penup()
                t14.left(90)
                t14.forward(150)
                t14.right(90)
                t14.pendown()
                sum2=sum2-20
            elif sum2==24:
                t14.penup()
                t14.right(90)
                t14.forward(150)
                t14.left(90)
                t14.forward(225)
                t14.pendown()
                sum2=sum2-17
        
        if sum2 == 100:
          print("Congratulations", player2, "you won!")
          print("To play again press F5 and run the game again")
          exit()
        if num2==6:
          dice_roll2()
        else:
            dice_roll()

def move2():
    global sum2
    if(sum2 % 10 == 0):
        if(sum2 % 20 == 0):
            t14.penup()
            t14.right(90)
            t14.forward(75)
            t14.right(90)
            t14.penup()

        else:
            t14.penup()
            t14.left(90)
            t14.forward(75)
            t14.left(90)
            t14.penup()
    else:
      t14.penup()
      t14.forward(75)
      t14.penup()
    sum2 = sum2 + 1

            
main()

"""def check():
    global sum
    t13.forward(0)
    for i in range(0, num):
        t13.penup()
        t13.backward(75)
        t13.pendown()
        sum=sum-1
        print(sum)""" 

