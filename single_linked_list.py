class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class Singlelinkedlist :
    def __init__(self):
        self.head =None

    def insert_begin(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head= nb

    def insert_end(self,data):
        ne= Node(data)
        temp= self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def insert_pos(self,pos, data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data =data
        np.next= temp.next
        temp.next = np

    def delete_begin(self):
        temp=self.head
        self.head =temp.next
        temp.next = None

    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not  None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delete_pos(self, pos):
        prev = self.head
        temp = self.head.next
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next= temp.next




    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data , "-->" , end="")
                temp= temp.next


sll = Singlelinkedlist()
n=Node(10)
sll.head= n
n1 = Node(20)
n.next = n1
n2= Node(30)
n1.next =n2
n3= Node(40)
n2.next = n3

sll.insert_begin(5)

sll.insert_end(50)

sll.insert_pos(2 ,25)

#sll.delete_begin()

#sll.delete_end()

#sll.delete_pos(2)

sll.display()