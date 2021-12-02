##imports
import turtle as trtl
import math


##initialization
t = trtl.Turtle()
cover = trtl.Turtle()
wn = trtl.Screen()
global line_list
line_list = []

wn.bgpic('Group 1 (1).png')
wn.setup(570, 696)
cover.ht()
t.penup()
t.ht()
t.pencolor('white')
t.goto(-250, 150)
t.pendown()

#Used to cover 0 when button pressed.
#wn.addshape('cover.gif')
#cover.shape('cover.gif')
cover.speed(0)
cover.penup()
cover.goto(225, 225)
cover.pendown() 
#cover.stamp()

##Operator Function

def addition(request):
    t.clear()
    for i in range(len(request)):
        request[i] = str(request[i])
        
    request = ''.join(request)
    request = request.split('+')
    length = len(request)
    length = length-1
    int2 = ''.join(request[length]).split('=')[0]
    total = 0
    for i in range(0,length,1): 
        total =int(total) + int(request[i])
    print('table is')
    print(total)
    print(int2)
    total = total + int(int2)
    t.pu()
    t.goto(140,150)
    t.pendown()
    if int(len(list(str(total)))) >= 3:
        turtlereset = 140
        for i in range(len(list(str(total)))):
            t.pu()
            t.goto(turtlereset,150)
            t.pendown()
            turtlereset -= 50
    t.write(str(total), font=("Arial", 74, "bold"))


def subtraction(request):
    t.clear()
    for i in range(len(request)):
        request[i] = str(request[i])    
    request = ''.join(request)
    request = request.split('-')
    length = len(request)
    length = length-1
    int2 = ''.join(request[length]).split('=')[0]
    total = int(request[0]) - int(int2[0])



    t.pu()
    t.goto(140,150)
    t.pendown()
    if int(len(list(str(total)))) >= 3:
        turtlereset = 140
        for i in range(len(list(str(total)))):
            t.pu()
            t.goto(turtlereset,150)
            t.pendown()
            turtlereset -= 50
    
    t.write(str(total), font=("Arial", 74, "bold"))
def multiplication(request):
    t.clear()
    for i in range(len(request)):
        request[i] = str(request[i])    
    request = ''.join(request)
    request = request.split('x')
    int2 = ''.join(request[1]).split('=')
    total = int(request[0]) * int(int2[0])







    t.pu()
    t.goto(140,150)
    t.pendown()
    if int(len(list(str(total)))) >= 3:
        turtlereset = 140
        for i in range(len(list(str(total)))):
            t.pu()
            t.goto(turtlereset,150)
            t.pendown()
            turtlereset -= 50    
    t.write(str(total), font=("Arial", 74, "bold"))


def division(request):
    t.clear()
    for i in range(len(request)):
        request[i] = str(request[i])    
    request = ''.join(request)
    request = request.split('/')
    int2 = ''.join(request[1]).split('=')
    total =round(int(request[0]) / int(int2[0]),2)




    t.pu()
    t.goto(140,150)
    t.pendown()
    if int(len(list(str(total)))) >= 3:
        turtlereset = 140
        for i in range(len(list(str(total)))):
            t.pu()
            t.goto(turtlereset,150)
            t.pendown()
            turtlereset -= 50
    t.write(str(total), font=("Arial", 74, "bold"))


def write(button):
    t.write(button, font=("Arial", 74, "bold"))
    t.penup()
    t.fd(55)
    t.pendown() 

def find_operation(line_list):
    print(line_list)
    for char in line_list:
        if char == '+':
            addition(line_list)
        elif char == '-':
            subtraction(line_list)
        elif char == 'x':
            multiplication(line_list)
        elif char == '/':
            division(line_list)

    
def button_pressed(x, y):
    global button
    if 46 - 55*0 > y > 46 - 55*1:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '1/x'
            
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 'Natural Logarithim'
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 'log'
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 'Clear'
        elif -290 + 115*4 < x < -290 + 115*5:
            button = 'Delete'

    if 46 - 55*1 > y > 46 - 55*2:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'sin'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 'cosin'
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 'tan'
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 3.14
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '%' #Modulus
  
    if 46 - 55*2 > y > 46 - 55*3:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '|x|'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = '(' #Open Paranthesis
        elif -290 + 115*2 < x < -290 + 115*3:
            button = ')' #Closed Parenthesis
        elif -290 + 115*3 < x < -290 + 115*4:
            button = '!' #Factorial
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '/' #Division

    if 46 - 55*3 > y > 46 - 55*4:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'e' #exponent
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 7
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 8
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 9
        elif -290 + 115*4 < x < -290 + 115*5:
            button = 'x' #Multiplication

    if 46 - 55*4 > y > 46 - 55*5:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'x^2' #Ten to the power of x
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 4
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 5
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 6
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '-' #subtraction

    if 46 - 55*5 > y > 46 - 55*6:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '+'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 1
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 2
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 3
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '+' #Addition
  
    if 46 - 55*6 > y > 46 - 55*7:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'Natural Logarithm'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = '-' #Negative
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 0
        elif -290 + 115*3 < x < -290 + 115*4:
            button = '.' #Decimal
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '=' #Equal
            
    try:
        line_list.append(button)
        
    except NameError:
        print('')

    write(button)
    for char in line_list:
        if char == '=':
            find_operation(line_list)


wn.onscreenclick(button_pressed)
wn.mainloop()
