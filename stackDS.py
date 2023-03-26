stackList = []
listSize = int(input("Enter the stack size : "))
for i in range(listSize):
    stackList.append(input(f"list item {i+1} :"))
print(stackList)
while True:
    if input("Do you want to pop data? y/n : ") !='y':
        break
    else:
        if len(stackList)==0:
            print("stack is Empty! Nothing to remove")
        else:
            stackList.pop()
            print(stackList)

while True:
    if input("Do you want to add item to the stack? y/n :") !='y':
        break
    else:
        addData = input("Enter the data you want to add :")
        stackList.append(addData)
        print(stackList)