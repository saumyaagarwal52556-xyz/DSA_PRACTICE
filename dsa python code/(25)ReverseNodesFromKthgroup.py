
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

def reverseKthgroup(head , k):

    # check for k group existence
    temp = head
    for _ in range(k):
        if temp == None:
            return head
        temp = temp.next

    # recursion call
    prev = reverseKthgroup(temp , k)

    # reversing begins
    temp = head
    for _ in range(k):
        nextnode = temp.next
        temp.next = prev
        prev = temp
        temp = nextnode

    return prev



head = None

chances = int(input("Enter no of values to be inserted in linked list : "))

for i  in range(chances):
    val = int(input("enter data: "))
    head = Initialization(head , val)

print("Linked List :")
Printing(head)

print("\nreversed k group list : ")
result = reverseKthgroup(head , 2)
Printing(result)