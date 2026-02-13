n = 5

for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for l in range(1, n + 1):
    for m in range(l - 1):
        print(" ", end="")
    
    for o in range(2 * (n - l) + 1):
        print("*", end="")
    
    print()

