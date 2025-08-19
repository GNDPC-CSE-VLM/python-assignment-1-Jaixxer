# Assignment 1 – Section B
# Write your answers below each question

# Q11: Swap variables

#Using a temporary variable
a =10
b=20
print("Value of a before swapping: ",a)
print("Value of b before swapping: ",b)
temp = a
a= b
b= temp
print("Value of a after swapping: ",a)
print("Value of b after swapping: ",b)

#Without using a temporary variable
a =10
b=20
print("Value of a before swapping: ",a)
print("Value of b before swapping: ",b)
a += b
b =a -b
a-=b
print("Value of a after swapping: ",a)
print("Value of b after swapping: ",b)


# Q12: Number pattern
value = "6 "
for i in range(0,6):
  print(value*6)


# Q13: Factorial OR Password System
number = int(input("Enter the number: "))
factorial = 1
for i in range (1, number+1):
  factorial *= i
print(f"The factorial of {number} is {factorial}")


#Password System
attempt = 0
password = "admin123"
logged_in = False

while attempt < 3:
  login = input("Please enter the password: ")
  if login == password:
    print("Access Granted")
    logged_in = True
    break
  else:
    attempt+=1

if logged_in == False:
  print("Access Denied")