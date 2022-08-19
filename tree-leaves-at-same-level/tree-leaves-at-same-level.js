function allLeavesAtSameLevel(node) {
  return tree_by_levels(node)
}










function tree_by_levels(root){
    if(!root){
        return []
    }
    let ans = []
    let queue = []
    queue.push(root)

    while(queue && queue.length){
        let currSize = queue.length
        let currList = []

        while(currSize > 0){
            let currNode = queue.shift()
            currSize -= 1
            if(currNode.left){
                queue.push(currNode.left)
            }
            if(currNode.right){
                queue.push(currNode.right)
            }
            if(!currNode.right && !currNode.left){
                currList.push(currNode.data)
            }
        }
        ans.push(currList)
    }
    let result = ans.filter(item=>item.length>0).length == 1
    return result
}