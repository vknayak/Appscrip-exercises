# WAP to find the sum of two linked lists using Stack.
# WAP to find the length of a singly linked list.

class value:
    def __init__(self, values):
        self.values = values
        self.next = None  # make None as the default value for next.
        


def count_nodes(head):
    # assuming that head != None
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count

def average(head):
    sum_of_all_values=0
    c=count_nodes(head)
    for i in range(c):
        sum_of_all_values+=head.values
        head=head.next
        
    return "sum of all values",sum_of_all_values
        

valueA = value(6)
valueB = value(3)
valueC = value(4)
valueD = value(2)
valueE = value(1)

valueA.next = valueB
valueB.next = valueC
valueC.next = valueD
valueD.next = valueE



print("This linked list's length is: (should print 5)")
print(count_nodes(valueA))

print(average(valueA))