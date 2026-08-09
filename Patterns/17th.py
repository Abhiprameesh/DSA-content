class Solution:
    def pattern2(self, n):

        for i in range(n):

            # Spaces
            for j in range(n - i - 1):
                print(" ", end="")

            # Increasing letters
            for j in range(i + 1):
                print(chr(65 + j), end="")

            # Decreasing letters
            for j in range(i - 1, -1, -1):
                print(chr(65 + j), end="")

            print()