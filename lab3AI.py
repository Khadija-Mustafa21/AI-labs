
#1
for num in range(1500,2701):
    if num%7==0 and num%5==0:
      print(num)
#2
temp=float(input("enter temp in fahrenheit:"))
num=((temp-32)*5)/9
print("Temp in celsius is:",num)
#3
num=int(input("enter a number between 1 to 9:"))

if(num>=1 and num<=9):
    print("Well guessed!")
else:
    while  not( num>=1 and num<=9):
        num=int(input("enter a number between 1 to 9:"))
    else:
        print("Well guessed!")
#4
k=0
for i in range(9):
    if(i<=4):
        for j in range(i+1):
            print("*" ,end="")
        print("")
    else:    
        for j in range(i+1-(k+2)):
            print("*",end="")
        print("") 
        k=k+2
#5
word=input("Enter a word:")

word=word[::-1]
print(word)
#6
num=(1,2,3,4,5,6,7,8,9)
c1,c2=0,0
for item in num:
      if(item%2==0):
            c1+=1
      else:
            c2+=1
print("number of even digits is ",c1 ,"number of odd digits is ",c2)
#7

data=[1,2.3,1+2j,True,'w3resource',(0,-1),[5,12],{"class":"Six"}]

for i in range(len(data)):
      print(data[i]," of datatype ",type(data[i]))
#8
for i in range(7):
    if(i==3 or i==6):
        continue
    else:
        print(i,end=" ")
#9
n1=0
n2=1

print(n1,n2,end=" ")

while (n1+n2<=50):
    temp=n2
    n2=n1+n2
    n1=temp
    print(n2,end=" ") 
#10
for i in range (51):
    if(i==0):
        continue
    elif(i%3==0 and i%5!=0):
        print("fizz")
    elif (i%5==0 and i%3!=0):
        print("Buzz") 
    elif (i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)
#11
m=int(input("Enter the number of rows:"))
n=int(input("Enter the number of columns:"))

nested_list = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        nested_list[i][j]=i*j

print(nested_list)
#12
str1=""
str2=input("Enter a line:")
while (str2!=""):
    str1=str1+str2
    str2=input("Enter a line:")

print(str1.lower())
#13
binary_numbers = input("Enter comma-separated 4 digit binary numbers: ").split(",")

divisible_by_5=[]

for binary in binary_numbers:
    decimal=int(binary,2)
    if (decimal % 5 == 0):
        divisible_by_5.append(binary)
    else:
        pass

print(",".join(divisible_by_5))
#14
text = input("Enter a string: ")
letters = 0
digits = 0

#Loop through each character in the string
for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print("Letters:", letters)
print("Digits:",digits)
pswd=input("Enter your password:")

if len(pswd) < 6 :
    print("minimum length is 6")
if(len(pswd) > 16) :
  print("maximum length is 16")

for char in pswd:
    if char.isdigit()==True:
        break
else:
    print("at least one digit is required")
for char in pswd:
    if char.isalpha()==True:
        if char.isupper()==True:
            break
else:
    print("at least one uppercase letter is required")
for char in pswd:
    if char.isalpha()==True:
        if char.islower()==True:
            break
else:
    print("at least one lowercase letter is required")
for char in pswd:
    if char=='$' or char=='#' or char =='@':
        break
else:
    print("at least one  special character (  $  or  #   or   @) is required")

