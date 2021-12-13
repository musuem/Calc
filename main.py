##imports
import turtle as trtl
import math
import random as rand

##initialization
t = trtl.Turtle()
t.ht()
loading = trtl.Turtle()
loading.ht()
cover = trtl.Turtle()
cover.ht()
wn = trtl.Screen()
graph = trtl.Turtle()
graph.speed('fastest')
graph.pensize(3)
graph.ht()
global line_list
line_list = []
global line_list11
line_list1 = []
graphwriter = trtl.Turtle()
graphwriter.ht()
global printed
printed= True    
cover.ht()

t.penup()
t.ht()
t.pencolor('white')
t.goto(195, 150)
t.pendown()

#Used to cover 0
cover.speed(0)
cover.penup()
cover.goto(225, 280)
cover.pendown() 
cover.stamp()


# TEMPORARY
def xadd():
    line_list1.append(str('x'))
    graphwriter.clear()
    writegraph(''.join(line_list1))   
def multiply():
    line_list1.append(str('*'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))   
def one():
    line_list1.append(str('1'))    
    graphwriter.clear()
    writegraph(''.join(line_list1)) 
def two():
    line_list1.append(str('2'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))  
def three():
    line_list1.append(str('3'))    
    graphwriter.clear()
    writegraph(''.join(line_list1)) 



def four():
    line_list1.append(str('4'))    
    graphwriter.clear()
    writegraph(''.join(line_list1)) 



def five():
    line_list1.append(str('5'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))   
def six():
    line_list1.append(str('6'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))  
def seven():
    line_list1.append(str('7'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))  
def eight():
    line_list1.append(str('8'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))  
def nine():
    line_list1.append(str('9'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))
def zero():
    line_list1.append(str('0'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))  
def add():
    line_list1.append(str('+'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))  
def divo():
    line_list1.append(str('/'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))  
def sub():
    line_list1.append(str('-'))    
    graphwriter.clear()
    writegraph(''.join(line_list1))
def delete1():
    try:
      line_list1.pop()  
    except:
      pass
    graphwriter.clear()
    writegraph(''.join(line_list1))

def writegraph(char):
  graphwriter.pencolor('white')
  graphwriter.speed(0)
  graphwriter.pu()
  graphwriter.goto(-260,-340)
  graphwriter.pd()
  graphwriter.write(char, font=("Arial", 30, "bold"))


##Operator Function
def write(list):
    mult = 0
    for char in reversed(list):
        for wt in reversed(char):
            t.pu()
            t.goto(195 - 55*mult, 150)
            t.pd() 
            t.write(wt, font=("Arial", 74, "bold"))
            mult += 1

def screen_check(mult):
  if 195 - 55*mult < -300:
    return True
  else:
    return False
#With thise code we can evalute a factorial
def calc_factorial(char):
  while char > 0:
    return char * calc_factorial(char - 1)
  return 1
#This code indentifies which trigonometry operator is being used and then manipulates the string to grab the sin/cos/tan part, and it will then assign it to its corresponding trigonometry type and solve
def trigonomtry(equation, arithmetic, char):
    trig = eval(str(equation.split(char)[1]))
    trigtoinsert = arithmetic.index(char)
    arithmetic.pop(int(trigtoinsert))
    if char == 'sin':
        trig = str(round(math.sin(float(trig)),5))
    elif char == 'cos':
        trig = str(round(math.cos(float(trig)),5))
    elif char == 'tan':
        trig = str(round(math.tan(float(trig)),5))
    arithmetic.insert(trigtoinsert,str(trig))
    return equation, arithmetic

#Works as an On and Off Switch. If equal sign is present, pop it out so error does not occur.
def calculate(arithmetic, bool):

    if bool == True:
        arithmetic.pop()

    #Used for factorial. String manipulation.
    #With this code, we initally split the ! into 2 parts, and then reverse index the 1st portion of the split to determine the factorial coefficient 
    if '!' in arithmetic:
        stringclone = ''.join(arithmetic)
        for chars in arithmetic:
            if chars == '!':
                tempolist = ''.join(arithmetic).split('!')
                tempolist = list(tempolist[0])
                for char in reversed(tempolist):
                    try:    
                        int(char)
                    except:
                        tempolist = ''.join(tempolist).split(char)
                        break
    
        sum =  str(calc_factorial(int(tempolist[(len(tempolist)-1)])))
        stringclone = stringclone.replace(tempolist[(len(tempolist)-1)] + '!',sum )
        answer = eval(stringclone)
        print(answer)
        arithmetic = stringclone
    #Our final portion of the evaluation block allows us to finalize and convert any raw equations to fit the requirements of an eval function
    equation = ''.join(arithmetic)
    print(arithmetic)
    trig = ['sin', 'cos', 'tan']
    for char in trig:
        print(char)
        if char in arithmetic:
            print(char)
            equation, arithmetic = trigonomtry(equation, arithmetic, char)
            print(equation, arithmetic)
    print(equation, arithmetic)
    equation = ''.join(arithmetic)

    try:
        print(equation)
        equation = str(eval(equation))
        t.clear()
        write(equation)
    except Exception:
        t.clear()
        t.pu()
        t.goto(0, 150)
        t.pendown()
        t.pencolor('red')
        t.write('Error', font=("Arial", 74, "bold"))
        t.pencolor('white')

#This graphing function will switch the calculator mode to graphing and conduct all graphing operations
def Graphing(x,y):
    global line_list1
    wn.onkey(xadd, 'x')
    wn.onkey(multiply, '*')
    wn.onkey(one, '1')
    wn.onkey(two, '2')
    wn.onkey(three, '3')
    wn.onkey(four, '4')
    wn.onkey(five, '5')
    wn.onkey(six, '6')
    wn.onkey(seven, '7')
    wn.onkey(eight, '8')
    wn.onkey(nine, '9')
    wn.onkey(zero, '0')
    wn.onkey(add, '+')
    wn.onkey(sub, '-')
    wn.onkey(divo, '/')
    wn.onkey(delete1,'BackSpace')
    wn.listen()
    if -290 < y< -240:
        if -290 < x<-100:
            wn.bgpic('calc.png')
            wn.onclick(button_pressed)
            graph.clear()
            graphwriter.clear()
    if -290 + 115*4 < x < -290 + 115*5:
        if 46 - 55*6 > y > 46 - 55*7:
          graph.pencolor('orange')
          graphing_equation = ''.join(line_list1)

          for things in line_list1:
            if str(things) == '**2':
              graph.pencolor('green')
            if str(things) == '***3':
              graph.pencolor('pink')
          for x in range(-40, 40):
            graphing_equation = ''.join(line_list1)
            replace  = '(' + str(x) + ')'
            graphing_equation = graphing_equation.replace('x', replace)
            try:
              y = 5*eval(graphing_equation)
            except:
              continue
            if x == -40:
              graph.penup()
              graph.goto(x*5, y*5)
              graph.pendown()
            graph.goto(x*5, y*5)
          line_list1 = []


#The code below is mimicking the layout of a rectangle divided by x lines on heigh and width. It then multiplys y by the row level and x but the colum level. 
# After we determine and classify the button click and its position, we assign the button click to a value which corresponds to its click
def button_pressed(x, y):
    global button, line_list, printed
    printed = True
    NotEval = True
    if 50 < y< 100:
        if -270<x<-130:
            button = 'SwitchTrig'
            NotEval = False
            printed = False
            wn.bgpic('graphingcalc.png')
            graph.pencolor('white')
            graph.penup()
            graph.goto(-200,0)
            graph.pendown()
            graph.goto(200,0)
            graph.penup()
            graph.goto(0,-200)
            graph.pendown()
            graph.goto(0,200)
            wn.onclick(Graphing)
            line_list.clear()
            t.clear()
    if 46 - 55*0 > y > 46 - 55*1:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '1/x'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = '**(1/2)'
        elif -290 + 115*2 < x < -290 + 115*3:
            button = '**(1/3)'
        elif -290 + 115*3 < x < -290 + 115*4:
            button = 'Clear'
            printed = False
        elif -290 + 115*4 < x < -290 + 115*5:
            button = 'Delete'
            printed = False

    if 46 - 55*1 > y > 46 - 55*2:
        if -290 + 115*0 < x < -290 + 115*1:
            button = 'sin'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = 'cos'
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
            button = '*' #Multiplication

    if 46 - 55*4 > y > 46 - 55*5:
        if -290 + 115*0 < x < -290 + 115*1:
            button = '**2' #Ten to the power of x
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
            button = 'x'
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
            button = '**'
        elif -290 + 115*1 < x < -290 + 115*2:
            button = '-' #Negative
        elif -290 + 115*2 < x < -290 + 115*3:
            button = 0
        elif -290 + 115*3 < x < -290 + 115*4:
            button = '.' #Decimal
        elif -290 + 115*4 < x < -290 + 115*5:
            button = '=' #Equal
    #We use a check/if statement to check for button clicks that should not be written like clear or delete
    if printed != False:
        line_list.append(str(button))
    t.clear()

    #writes characters clicked on screen.

    write(line_list)

      #if characters go off screen:
    #With thise code, we can check and verify that the inputted equation does not go off of the screen, and if it does, the equation will be forced to be evaulted
    screencheck = screen_check(len(line_list))
    if screencheck == True:
        t.clear()
        equation = ''.join(line_list)
        line_list = []
        try:
          equation = str(eval(equation))
        except SyntaxError:
          t.pu()
          t.goto(0, 150)
          t.pendown()
          t.pencolor('red')
          t.write('Error', font=("Arial", 74, "bold"))
          t.pencolor('white')
          print(equation)
        write(line_list)


    #Special signs.

    ##With the following code we can filter out functions that we do not want evaluted as python's builtin eval function only accepts strings
    if NotEval == True:
        if button == '=':
            calculate(line_list, True)
            line_list = []
    #This button is used to clear the table and screen
    if button == 'Clear':
        t.clear()
        line_list = []
    #We can delete the previous input with this button, and it works by popping the most recently added index, clearing the screen, and rewriting the new list
    if button == 'Delete':
        t.clear()
        print(line_list)
        line_list.pop()
        print(line_list)
        write(line_list)

    

# Fix 1280+
import time
time.sleep(5)
loading.speed(0)
loading.ht()
loading.shape('circle')
rand = rand.randint(1, 50)
for i in range(1, rand):
    loading.penup()
    loading.fd(50)
    loading.pendown()
    loading.stamp()
    loading.penup()
    loading.goto(0, 0)
    loading.pendown()
    loading.right(36)
    rem = i%10
    if rem == 0:
        loading.clear()
loading.clear()


wn.bgpic('calc.png')
wn.setup(570, 696)

wn.addshape('return_to_calc.gif')

cover.ht()

t.penup()
t.ht()
t.pencolor('white')
t.goto(195, 150)
t.pendown()


graph.speed(0)

#Used to cover 0
cover.speed(0)
cover.penup()
cover.goto(225, 280)
cover.pendown() 
cover.stamp()

wn.onclick(button_pressed)

wn.mainloop()       