#a reusable block of code-function
def greet():
    print("hello world")
greet() 
#functions with parameters or arguments
def greetings(name):
    print("hello "+name)
greetings("joy")
greetings("mary")   

def add(a,b,c):
    print(a+b+c)
add(5,7,9) 

#function with return value
def calculate_total(price,tax):
    return price+tax
total_amount=calculate_total(500,100)
print(total_amount)

def area(l,w):
    return l*w
result=area(5,2)
print(result)

#function with default values
def say_hello(name="joy"):
    print("hello "+name)
say_hello()
say_hello("john")