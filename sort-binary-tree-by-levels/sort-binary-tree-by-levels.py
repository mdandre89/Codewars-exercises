import collections
def tree_by_levels(root):
    if not root:
        return []
    
    ans = []
    queue = collections.deque()
    queue.append(root)

    while queue:
        currSize = len(queue)
        currList = []

        while currSize > 0:
            currNode = queue.popleft()
            currList.append(currNode.value)
            currSize -= 1

            if currNode.left is not None:
                queue.append(currNode.left)

            if currNode.right is not None:
                queue.append(currNode.right)

        ans = ans + currList

    return ans