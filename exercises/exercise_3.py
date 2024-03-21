# Your solution to Exercise 3
num = int(input("Enter a number: "))
colour = ""
if num == 0:
  colour = "Green"
elif num < 11 and num % 2 == 0:
  colour = "Black"
elif  num % 2 != 0:
  colour = "Red"
elif num <= 18 and num % 2 ==0:
  colour = "Red"
elif num <= 18 and num % 2 !=0:
  colour = "Black"
elif num < 28 and num % 2 == 0:
  colour ="Black"
elif num < 28 and num % 2 != 0:
  colour = "Red"
elif num <= 36 and num % 2 ==0:
  colour = "Red"
elif num <= 36 and num != 0:
  colour ="Black"

print(colour)

if num > 36: 
  print ("The ball will not play")