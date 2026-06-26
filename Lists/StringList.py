a = 'spam spam spam'
b = a.split()
print(b)#splits into a list, the string gets split into a list of words, using whitespace as the delimiter.

a = 'spam-spam1-spam2'#its different from the previous example, here we are using a different delimiter to split the string into a list.
delimiter = 'a'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))#joins the list back into a string, using the specified delimiter.

myList = [2,4,3,1,5,7]
sorted(myList)
print (myList)#so this will not change the original list, it will return a new sorted list. If you want to sort the original list, you can use the sort() method.