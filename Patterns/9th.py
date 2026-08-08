class Solution:
    def pattern2(self, n):

        # Top pyramid
        for i in range(n):
            spaces = " " * (n - i - 1)
            stars = "*" * (2 * i + 1)
            print(spaces + stars)

        # Bottom inverted pyramid
        for i in range(1, n):
            spaces = " " * i
            stars = "*" * (2 * (n - i) - 1)
            print(spaces + stars)


# class Solution:
#     def pattern2(self, n):

#         # Top half
#         for i in range(n):

#             # Print spaces
#             for j in range(n - i - 1):
#                 print(" ", end="")

#             # Print stars
#             for j in range(2 * i + 1):
#                 print("*", end="")

#             print()

#         # Bottom half
#         for i in range(1, n):

#             # Print spaces
#             for j in range(i):
#                 print(" ", end="")

#             # Print stars
#             for j in range(2 * (n - i) - 1):
#                 print("*", end="")

#             print()