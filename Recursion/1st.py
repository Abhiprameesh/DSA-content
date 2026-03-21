def printHello(n):
    if n == 0:
        return
    
    print("Hello")
    printHello(n - 1)


printHello(5)