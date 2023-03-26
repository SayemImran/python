queueList = []
sizeOfList = int(input(" Enter the size of you QUEUE : "))
for i in range(sizeOfList):
    queueList.append(input(f"Enter item {i+1} :"))
print(queueList)
while True:
    if input("Do you want to remove item from the queue? y/n : ") !='y':
        break
    else:
        if len(queueList)==0:
            print(" Queue is EMPTY! nothing to remove 🚫")
        else:
            queueList.pop(0)
            print(queueList)
while True:
    if input("Do you want to add item to QUEUE ? y/n : ") != 'y':
        break
    else:
        addData = input("Enter the data you want to add to QUEUE : ")
        queueList.append(addData)
        print(queueList)