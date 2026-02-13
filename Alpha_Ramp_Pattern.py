n = 5

for i in range(1, n + 1):
    letter = chr(65 + i - 1)
    for j in range(i):
        print(letter, end=" ")
    print()
