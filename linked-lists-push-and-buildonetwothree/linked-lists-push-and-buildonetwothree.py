class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    if head:
        c =  Node(data)
        c.next = head
        return c
    else:
        return Node(data)

def build_one_two_three():
    one = push(None, 3)
    two =  push(one, 2)
    three = push(two, 1)
    return three