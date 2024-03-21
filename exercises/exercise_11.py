
year = int(input("What is the current year we are in "))

if year % 4 == 0 and year % 100 !=0 and year %400 != 0:
  leap_year = True
  print("This year is a leap year")
else:
  print("Ordinary Year")