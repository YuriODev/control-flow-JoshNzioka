# Your solution to Exercise 9
num = int(input("Enter a 3 digit integer: "))
first_last_sum = (num//100) + (num %10)
# print(first_last_sum)
second_digit = (num//10) %10

if first_last_sum > second_digit:
  print(">")

elif first_last_sum < second_digit:
  print("<")

else:
  print("=")