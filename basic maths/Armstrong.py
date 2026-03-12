#An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
number = int(input("Enter a number: "))
length = len(str(number))
sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10
if number == sum:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")