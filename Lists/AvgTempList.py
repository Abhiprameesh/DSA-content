#the below program will ask the user for the number of days, then ask for the high temperature for each day. It will then calculate the average temperature and display how many days were above average.
#finds the days above average temperature
numDays = int(input("Enter the number of days: "))
total = 0
temp = [] 
for i in range( numDays ):
    nextDay = int(input("Day" + str(i + 1) + "'s high temp: "))
    temp.append(nextDay)
    total += temp[i]

avg = round(total / numDays, 2)
print("\nAverage = " + str(avg))

above = 0 
for i in temp:
    if i > avg:
        above += 1
print(str(above) + " days were above average.")