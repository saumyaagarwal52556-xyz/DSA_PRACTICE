
class ListNode:
    def __init__(self , val):
        self.val = val
        self.next = None

def Initailization(head , value):
# or insert at end
    new_node = ListNode(value)

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
        print(f"{current.val}",end="->")
        current = current.next

    print("None")

def Remove(head , targetindx):

    current = head
    len = 0
    while(current):
        current = current.next
        len += 1
    if(len <=1 and targetindx ==1):
        return None
    if len == targetindx:
        return head.next
    
    temp = head
    count = 1
    while(temp and count < (len - targetindx )):
        temp = temp.next
        count += 1

    if temp and temp.next:
        temp.next = temp.next.next

        return head
    else:
        temp.next = None
        return head


head = None
chances = int(input("Enter no.of values you want to input in linked list 1 :"))

for i in range(chances):
    user_input = int(input("enter data : "))
    head = Initailization(head , user_input)

print("\nlinked list1:")
printing(head)

Remove(head , 1)
printing(head)

