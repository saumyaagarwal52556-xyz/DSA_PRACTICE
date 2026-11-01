
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


def middleNode(head):
    curr = head
    leng = 0
    while curr:
        curr= curr.next
        leng +=1
    if(leng ==1):
        return head
    if(leng <= 0):
        return None
    count = 1
    temp = head
    while temp and count <(leng //2):
        temp = temp.next
        count += 1
    return temp.next

head = None

chances = int(input("Enter no of values to be inserted in linked list : "))

for i  in range(chances):
    val = int(input("enter data: "))
    head = Initialization(head , val)

print("Linked List :")
Printing(head)

