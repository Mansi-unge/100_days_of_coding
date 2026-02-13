# **Write a program for Binary to Decimal to conversion**

# This problem asks to convert a binary number (base 2) to its decimal (base 10) equivalent.

# - Each digit in a binary number represents a power of 2, and the decimal value is the sum of these powers.
# - **For example:**
#     - Binary 101 is equal to Decimal 5 because:1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5.



def binary_to_decimal(binary):
  decimal = 0
  power = 0

  for digit in binary[::-1]:
      decimal += int(digit) * (2 ** power)
      power += 1

  return decimal



binary_num = input("enter any binary number : ")
result = binary_to_decimal(binary_num)
print("Decimal number is : ",result)



