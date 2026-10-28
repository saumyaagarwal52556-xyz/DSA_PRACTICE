
class ListNode:
    def __init__(self , val=0 , next = None):
        self.val = val
        self.next = next

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

def RemoveElement(head , k):
    dummy = ListNode(0,head)
    curr = dummy
    while(curr.next):
        if(curr.next.val == k):
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next


head = None

chances = int(input("Enter no of values to be inserted in linked list : "))

for i  in range(chances):
    val = int(input("enter data: "))
    head = Initialization(head , val)

print("Linked List :")
Printing(head)

result = RemoveElement(head , 7)
print("\nRemove 6")
Printing(result)