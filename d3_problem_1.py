# Program to check whether a number is an Armstrong number or not

# Step 1: Take input from user
num = int(input("Enter your number: "))
print(f"The number you entered is {num}")

# Step 2: Find number of digits
# Convert number to string to count digits
power = len(str(num))
print(f"Total digits in the number: {power}")

# Step 3: Initialize variables
temp = num      # Temporary variable to store original number
total = 0       # Variable to store sum of powered digits

# Step 4: Extract each digit and calculate power
while temp > 0:
    digit = temp % 10           # Get last digit
    total += digit ** power     # Raise digit to power and add to total
    temp = temp // 10           # Remove last digit

# Step 5: Check if Armstrong number
if total == num:
    print("The given number is an Armstrong number")
else:
    print("The given number is NOT an Armstrong number")