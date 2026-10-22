
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None

def Initailization(head , value):
# or insert at end
    new_node = Node(value)

    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next
    current.next = new_node

    return head


def printing(head):
    current = head

    while current:
        print(f"{current.data}",end="->")
        current = current.next

    print("None")


def Merging( head , second):
    dummy = Node(0)
    current = dummy

    while( head and second):
        if(head.data <= second.data ):
            current.next = head
            head = head.next

        else:
            current.next = second
            second= second.next
        current = current.next

    current.next = head if head else second
    return dummy.next



head = None
Second = None

chances = int(input("Enter no.of values you want to input in linked list 1 :"))
chances2 = int(input("Enter no.of values you want to input in linked list 2 :"))

for i in range(chances):
    user_input = int(input("enter data : "))
    head = Initailization(head , user_input)

for i in range(chances):
    user_input = int(input("enter data : "))
    Second = Initailization(Second, user_input)

print("\nlinked list1:")
printing(head)

print("\nLinked list2: ")
printing(Second)

print("\nMerge list: ")
new = Merging(head , Second)
printing(new)