def printname(n):
    if n == 0:
        return
    
    print("Abhinand")
    printname(n - 1)

printname(int(input("enter a number: ")))