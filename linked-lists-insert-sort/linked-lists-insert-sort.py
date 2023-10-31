class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_sort(head):
    if not head:
        return head
    
    l = length(head)
        
    ls = []
    for i in range(l):
        ls.append(head.data)
        head = head.next

    new_ls = sorted(ls)

    one = head
    for index, value in enumerate(new_ls[::-1]):
        if index == 0:
            one = push(None, value)
        else:
            one = push(one, value)
    return one
        
        
        
def length(node):
    if not node:
        return 0
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng