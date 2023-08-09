length = int(input("Enter list lenght : "))
list = []

for i in range(length):
    temp = int(input("Enter list item : "))
    list.append(temp)

count = list.count(4)
print("number 4 occurs ", count , "times")