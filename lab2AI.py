count = 0
while(count<3):
  count=count+1
  print("Deeja")

count=0
while(count==0):
    print("hello deeja")
   
#while loop

a=6
while(a<6):
    a=+a
    print("Hello World")
    
#Single Statement while block


#for loop in lists
list=("Me","for","Me")
for i in list:
    print(i)
    
#for loop in tuples
tup=("Me","for","Me")
for i in tup:
    print(i)
    
#iterating over a string
a="Deeja"
for i in a:
    print(i)
    

list=["Me","for","Me"]
for index in  range(len(list)):
   print (list[index])
   
#COUNTINUE STATEMENT
for letter in 'Deeja':
   if letter=='e':
    continue
    print ('Current letter:',letter)
#function 
def my_fun():
    print("This is me")
my_fun()
#parameters
r=3
def my_fun(x):
  y=x+4
  return y
print (my_fun(r))
#default parameter value
def my_fun(country="Pakistan"):
     print("I am from",country)
     my_fun()
my_fun("Norway")
#list as parameters
def my_fun(fruits):
    for x in fruits:
        print(x)
    food=['banana','apple','potato']
    my_fun(food)
#return values
def my_function(x):
 return 5 * x
print (my_function(3))
#keyword arguments
def children(child1,child2,child3):
    print("the youngest child is",child3)
    children(child1="Zain",child2="Rabia",child3="Deeja")
#Class
class Myclass:x=5
#object
p1=Myclass()
print(p1.x)
#init function
class Person:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def myfunc(self):
     print("hello my name is",self.name)

p1=Person("deeja", 20)
print(p1)
p1.myfunc()