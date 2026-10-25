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

def length(head):
    leng = 0
    curr = head
    while curr:
        leng += 1
        curr = curr.next

    return leng

def Intersection(first , second):
    lenA = length(first)
    lenB = length(second)
    

    firstcopy = first
    secondcopy = second

    if lenA < lenB:
        for _ in range(lenB - lenA):
            secondcopy = secondcopy.next

    else:

        for _ in range(lenA - lenB):
            firstcopy = firstcopy.next

    #now the intersection begins

    while firstcopy and secondcopy:
        if firstcopy == secondcopy:
            return firstcopy
        firstcopy = firstcopy.next
        secondcopy = secondcopy.next


    return None


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

result = Intersection(First , Second)
print("\nIntersection:")
printing(result)