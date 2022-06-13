# Functions

# Define a function
def greet(first_name, last_name):
  print(f"Hi there {first_name}, {last_name}")
  print("Welcome aboard")

# Call the function
greet("Yusuff", "Tope")
greet("Yusuff", "Khairat")

# Types of function
# 1- perform a task
# Example
# code on line 4 to 10
# 2- return a value
# Example
# round(12.3)
def greet(name):
  print(f"Hi {name}")


greet("Tope")
# changing the above code to a return statement
def get_greeting(name):
  return f"Hi {name}"


message = get_greeting("Ridwan")
print(message)

# using return statements
# increment
def increment(number, by):
  return number + by


print(increment(2, by=1))
# by=1 is a keyword argument

# Multiply
def multiply(*numbers):
  total = 1
  for number in numbers:
    total *= number
  return total

print(multiply(2, 3, 4, 5))

# How dictionary works
def save_user(**user):
  print(user)

save_user(id=1, name="John", age=22)

# How to get values of differnt keys in a dictionary
def save_user(**user):
  print(user["id"])

save_user(id=1, name="John", age=22)
def save_user(**user):
  print(user["name"])

save_user(id=1, name="John", age=22)
