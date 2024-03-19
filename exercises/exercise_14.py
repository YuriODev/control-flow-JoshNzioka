# Your solution to Exercise 14
num = int((input("Enter a four digit integer: ")))

thou = num //1000#
hund = (num %1000)//100
tens = (num %100)//10
ones = num%10

print(thou == ones and tens == hund)