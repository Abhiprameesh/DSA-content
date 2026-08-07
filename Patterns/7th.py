class Solution:
    def print_pattern(self, n):
        for i in range(n):
            for j in range(n - 1 - i):
                print(" ", end="")
            for j in range( 2 * i + 1):
                print("*", end="")
            print()

# class Solution:
#     def pattern2(self, n):
#         for i in range(n):
#             spaces = ' ' * (n - i - 1)
#             stars = '*' * (2 * i + 1)
#             print(spaces + stars)