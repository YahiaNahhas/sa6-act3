#Problem 1: Sum of Digits
number = 19735
sum_of_digits = lambda x: sum(int(digit) for digit in str(x))
result = sum_of_digits(number)
print(result)