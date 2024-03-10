from array import *
size = 5
tos = 0
stack = array('i',[])
while(True):
    print(f"\nCurrent Stack:{stack}\n")
    choice = int(input("\n1.push\n2.pop\n3.Exit\n"))
    if(choice == 1):
        a = int(input("\nEnter number:"))
        if(len(stack) == size):
            print("Stack Overflow")
        else:
            stack.append(a)
            tos += 1
            print(f"\nAdded:{a}")
            print(f"TOS:{stack[tos-1]}")
    if(choice == 2):
        try:
            if(len(stack) == 0):
                print("Stack Underflow")
            else:
                tos-=1
                print(f"\nPopped {stack.pop()}")
                print(f"\nTOS:{stack[tos-1]}")
        except(IndexError):
            print("Stack Underflow")

    if(choice == 3):
        break
