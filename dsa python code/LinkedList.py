class Node:
    def __init__(self ,data):
        self.data = data
        self.next = None

def insert_beggining(head , value):

    new_node = Node(value)
    new_node.next = head
    head = new_node

    return head


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

def insertAtSpecificIndex(head , value , target):
    new_node = Node(value)

    count = 0
    current = head
    while current and count != (target -1):
        current = current.next
        count += 1

    temp = current.next
    current.next = new_node
    new_node.next = temp

    return head


def printing(head):
    current = head

    while current:
        print(f"{current.data}",end="->")
        current = current.next

    print("None")



# main calling begins
head = None

chances = int(input("Enter no.of values you want to input in linked list :"))

for i in range(chances):
    user_input = int(input("enter data : "))
    head = Initailization(head , user_input)

print("\nlinked list:")
printing(head)

head = insert_beggining(head , 60)
print("\nadding at the begging :")
printing(head)

head = insertAtSpecificIndex(head , 100,3)
print("\ninsert at specific index :")
printing(head)