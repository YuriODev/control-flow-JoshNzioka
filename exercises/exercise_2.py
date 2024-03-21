# Your solution to Exercise 2
Age = int(input("Enter your age: "))

if Age <= 1:
  print("You are an infant")
elif Age < 13:
  print("You are a child")
elif Age < 20:
  print("You are a teenager")
else:
  print("You are an adult")
  