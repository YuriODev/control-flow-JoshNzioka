# Your solution to Exercise 8
num = int(input("Enter a three digit integer: "))
check_num = int(input("Enter a digit to check for: "))

if num // 100 == check_num:
  print(True)

elif num //10 %10 == check_num:
  print(True)

elif num %10 == check_num:
  print(True)

else:
  print(False)