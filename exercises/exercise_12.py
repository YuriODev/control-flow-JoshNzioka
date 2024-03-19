# Your solution to Exercise 12
num = int(input("Enter a 4 digit number: "))
thousands = num //1000#
hundreds = (num %1000)//100
tens = (num %100)//10
ones = num%10

if thousands % 2 == 0 :
  thousands = "*"

if hundreds % 2 == 0 :
  hundreds= "*"

if tens % 2 == 0:
  tens = "*"

if ones % 2 == 0 :
  ones = "*"

print(thousands,hundreds,tens,ones)