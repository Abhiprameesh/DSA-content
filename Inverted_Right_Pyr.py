n = int(input("Enter the number of rows: "))
for i in range(1,n):
    for j in range(n - i):        
        print("*", end="")
    print()
   
