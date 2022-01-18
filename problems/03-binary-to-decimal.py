# Question-2:
# Write a Python program that takes a string as input containing binary 
# numbers separated by multiple whitespaces and creates a dictionary where 
# the keys will be corresponding decimals values of each binary number.
# [You are not allowed to use any built-in conversion function to convert the 
# binary values to its corresponding decimal values.]

# Hint: Here is an example of converting a binary value 101101 to its decimal 
# value:
# Decimal of 101101  = 1(2**5) + 0(24) + 1*(23) + 1(2**2) + 0(21) + 
# 1*(20) = 32 + 8 + 4 + 1 = 45
# ----------------------------------------------------------------
# Sample Input 1:
# 101101    1010      11110  10101        10   101  1111
# Sample Output 1:
# {45: 101101, 10: 1010, 30: 11110, 21: 10101, 2: 10, 5: 101, 15: 1111}
# Explanation1:
# There are 7 numbers in the input string. The dictionary will contain the 
# decimal and binary values of each number in key:value pairs. Since the 
# decimal of 101101 is 45, therefore, in the dictionary 101101 was added as 
# the value of the key 45.
# ----------------------------------------------------------------
# Sample Input 2:
# 1101              11   110010    10110
# Sample Output 2:
# {13: 1101, 3: 11, 50: 110010, 22: 10110}
# Explanation2:
# There are 4 numbers in the input string. The dictionary will contain the 
# decimal and binary values of each number in key:value pairs.

def binary_to_decimal(binary_string: str):
  binaries = binary_string.split()
  decimal_dict = {}

  for binary in binaries:
    current_bit = binary[::-1]
    current_decimal = 0
    for idx, bit in enumerate(current_bit):
      if int(bit):
        current_decimal = current_decimal + 2**idx
    decimal_dict[current_decimal] = current_bit
  print(decimal_dict)

binary_to_decimal('101101    1010      11110  10101        10   101  1111')
binary_to_decimal('1101              11   110010    10110')