class T:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def is_bst(node):
    ls = inorderTraversal(node)
    sorted_ls = sorted(ls)
    return ls == sorted_ls or ls == sorted_ls[::-1]
    
def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer

def inorderTraversalUtil(root, answer):

    if root is None:
        return

    inorderTraversalUtil(root.left, answer)
    answer.append(root.value)
    inorderTraversalUtil(root.right, answer)
    return