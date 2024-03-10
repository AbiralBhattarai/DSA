MyList = [1,2,3,4,5,6,7,8,9]
MyQueue =[]
#enque
for i in MyList:
    MyQueue.append(i)
    print(f"\n{MyQueue}\n")

#deque
for i in range(len(MyQueue)):
    print(f"\n{MyQueue.pop(0)}\n")
    print(f"\n{MyQueue}\n")