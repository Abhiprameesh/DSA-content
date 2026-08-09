class Solution:
    def pattern12(self, n):
        for i in range(n):

    # increasing
            for j in range(i + 1):
                print(j + 1, end="")

    # spaces
            for j in range(2 * (n - i - 1)):
                print(" ", end="")

    # decreasing
            for j in range(i + 1):
                print(i - j + 1, end="")

            print()