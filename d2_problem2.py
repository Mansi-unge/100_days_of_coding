year = int(input( "enter the year : "))

print(f"the year you entered is : {year}")

print( " year is leap year " if (year  % 4 == 0 and year % 100 != 0) or year % 400 == 0
else   "year is not leap year")