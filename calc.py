##imports
import turtle as trtl
import math

##initialization
t = trtl.Turtle()
wn = trtl.Screen()
operation_list = ['+', '-', '*', '/']
wn.setup(1.0, 1.0)
##First Number
num_one = input('num 1: ' )
def exponents(x,y):
  answer = x^y
def sin(x):
  answer = math.sin(x)
def cosin(x):
  answer = math.cosin(x)
def tan(x):
  answer = math.tan(x)
def add(x,y):
  sum = x+y
def subtract(x,y):
  difference = x-y
def multiplication(x,y):
  product = x*y
def division(x,y):
  quotient = x/y
def factorial(x):
  total = x
  for i in range(1, x+1, 1):
    total = total*(x-1)
    x=-1
#sin(num_one)
num_one = str(num_one)
for char in operation_list:
  try:
    num_one = num_one.split(char)
    if num_one:
      print(char)
  except Exception:
    ''





'''
##Find operation
for char in operation_list:
    try:
        result = num_one.find(char)
        if result >= 0:
            num_one = num_one.split(char)
            num_one[1] = char
    except AttributeError:
        break
'''
