
a=9
b=8
c=sum((a,b))
print(c)

def function1():
    print("Hello you are in function 1")

print(function1())
function1()

def function1(a,b):
    print("Hello you are in function 1",a+b)
function1(5,7)

def function2(a,b):
    average =(a+b)/2
    print(average)
function2(5,7)

v=function2(5,7)
print(v)

def function3(a,b):
    average=(a+b)/2
    print(average)
    return average
v=function3(5,7)
print(v)

def function2(a,b):
   """this is a function which will calculate average of two numbers"""

print(function2.__doc__)