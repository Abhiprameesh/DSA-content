class Solution:
    def pattern8(self, n):
        for i in range(n):

            # spaces
            for j in range(i):
                print(" ", end="")

            # stars
            for j in range(2 * (n - i) - 1):
                print("*", end="")

            print()