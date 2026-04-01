def sum_of_n(n):
    if n == 0:   # base case
        return 0
    return n + sum_of_n(n - 1)

print(sum_of_n(int(input("Enter a number: "))))