# Print the below Pattern using Single loops

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
n = int(input("Enter the number of rows: "))

# Take input for starting number
s = int(input("Enter the starting number: "))

# Single loop runs for both upper and lower halves
# Total rows = 2 * n
for i in range(2 * n):

    # -------- UPPER HALF --------
    # When i is less than n, numbers and count increase
    if i < n:
        # s + i  -> decides the number to print
        # i + 1  -> decides how many times to print it
        # str(...) is used because string repetition creates the pattern
        print(str(s + i) * (i + 1))

    # -------- LOWER HALF --------
    # When i is greater than or equal to n, pattern decreases
    else:
        # (2*n - i - 1) -> reverses the number sequence
        # (2*n - i)     -> reverses the count
        print(str(s + (2*n - i - 1)) * (2*n - i))
