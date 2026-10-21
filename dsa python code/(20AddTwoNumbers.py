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


def add(first , second):
    dummy = ListNode(0)
    carry = 0
    current = dummy

    while(first or second or carry):
        val1 = first.val if first else 0
        val2 = second.val if second else 0
        temp =val1 + val2 + carry 
        carry = temp // 10
        digit = temp % 10

        current.next = ListNode(digit)
        if first:
            first = first.next
        if second:
            second = second.next

        current = current.next

    return dummy.next



First = None
Second = None

chances = int(input("Enter no.of values you want to input in linked list1 :"))
chances2 = int(input("Enter no.of values you want to input in linked list2 :"))

for i in range(chances):
    user_input = int(input("enter data : "))
    First = Initailization(First , user_input)

for i in range(chances2):
    user_input = int(input("enter data : "))
    Second = Initailization(Second , user_input)

print("\nlinked list1:")
printing(First)

print("\nlinked list2:")
printing(Second)

print("\n add two list: ")
result = add(First , Second)
printing(result)