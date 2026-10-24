
class ListNode:
    def __init__(self , val):
        self.val = val
        self.next = None

def Initialization(head , val):
    newNode = ListNode(val)

    if not head:
        return newNode

    current = head
    while current.next:
        current = current.next

    current.next = newNode

    return head

def Printing(head):
    current = head

    while current:
        print(current.val , end="->")
        current = current.next

    print("None")

def RemoveDuplicate(head):
    curr = head
    while curr and curr.next:
        if(curr.val == curr.next.val):
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


head = None

chances = int(input("Enter no of values to be inserted in linked list : "))

for i  in range(chances):
    val = int(input("enter data: "))
    head = Initialization(head , val)

print("Linked List :")
Printing(head)

result1 = RemoveDuplicate(head)
print("\nRemove duplicate: ")
Printing(result1)