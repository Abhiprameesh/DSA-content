# Given two integers N1 and N2, find their greatest common divisor.
def find_gcd(n1, n2):
    while n2!=0:
        temp = n2
        n2 = n1 % n2
        n1 = temp
    return n1

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

gdc = find_gcd(n1, n2)
print("The greatest common divisor of", n1, "and", n2, "is:", gdc)
