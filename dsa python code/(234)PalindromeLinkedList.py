
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

def Palindrome(head):
    copyHead = None
    clone = None 
    second = None  #reversed list

    #clone list
    temp  = head
    while temp:
        newnode = ListNode(temp.val)
        if not copyHead:
            copyHead = newnode
            clone = newnode

        else:
            clone.next = newnode
            clone = newnode
        temp = temp.next

    #reverse the list
    curr =copyHead
    while curr:
        next = curr.next
        curr.next = second
        second = curr
        curr=next
    Printing(second)
    print()

    first = head
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True


head = None

chances = int(input("Enter no of values to be inserted in linked list : "))

for i  in range(chances):
    val = int(input("enter data: "))
    head = Initialization(head , val)

print("Linked List :")
Printing(head)

print("\ncheck palindrome ")
print(Palindrome(head))