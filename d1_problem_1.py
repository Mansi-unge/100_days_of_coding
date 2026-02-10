# Print the below Pattern using two loops

# input =  n = 4, s = 3; 

# 3

# 44

# 555

# 6666

# 6666

# 555

# 44

# 3



# Take input for number of rows (half of the pattern)
n = int(input("enter the number to create pattern : "))

# Take input for the starting number of the pattern
s = int(input("enter the starting number : "))

# -------- UPPER HALF --------
# This loop prints the increasing part of the pattern
# i goes from 0 to n-1
for i in range(n):
    # s + i  -> decides which number to print
    # i + 1  -> decides how many times the number is printed
    # str(...) is used because string repetition creates the pattern
    print(str(s + i) * (i + 1))

# -------- LOWER HALF --------
# This loop prints the decreasing part of the pattern
# i goes from n-1 to 0 (reverse order)
for i in range(n - 1, -1, -1):
    # Same logic as upper half, but values decrease
    print(str(s + i) * (i + 1))
