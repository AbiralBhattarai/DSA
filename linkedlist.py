#create linked list
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def add(self,new = None):
        self.new = new
        newnode = Node(new)
        temp = self.head
        newnode.next = temp
        self.head = newnode

    #adding elements
    def insertstart(self,new = None):
        self.new = new
        newnode = Node(new)
        newnode.next = self.head
        self.head = newnode
    
    def insertend(self,new=None):
        self.new = new
        newnode = Node(new)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newnode

    def insertmid(self,data,x):
        self.data = data
        self.x = x
        temp = self.head
        newnode = Node(data)
        while(temp):
            if(temp.data == x):
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next

    #deleting values
    def delete(self,value):
        temp = self.head
        while(temp != None):
            if(temp.data == value):
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    #searching value in Linked List
    def search(self,value):
        temp = self.head
        while(temp!=None):
            if(temp.data == value):
                print(f"\nfound {temp.data}\n")
                break
            temp = temp.next

        



    #printing elements
    def List(self,first = None):
        self.first = first
        first = self.head
        while(first):
            print(f"\n{first.data}\n")
            first = first.next

    #sorting data in linked list

    def srt(self):
        temp = self.head
        a = []
        while(temp!=None):
            a.append(temp.data)
            temp = temp.next
        a.sort()
        a.reverse()
        new = LinkedList()
        for i in a:
            new.add(i)
        new.List()



obj = LinkedList()
obj.insertstart(20)
obj.insertstart(30)
obj.insertend(50)
obj.insertmid(40,30)
obj.List()
obj.search(50)
obj.srt()

