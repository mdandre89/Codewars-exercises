function isValidTree (rootNode) {
  if(rootNode.color!=='yellow' && rootNode.ornament==='star'){
    return false
  }
  const nodes = [rootNode]
  while(nodes.length > 0) {
    const node = nodes.shift()
    if(node.left) {
      nodes.push(node.left)
    }
    if(node.right) {
      nodes.push(node.right)
    }
    
    if( (!node.right && !node.left && node.ornament!=='star') && node.color !== 'blue' ){
      return false
      break
    }
    
    if( (node.right || node.left) && node.color !== 'red' && rootNode.ornament!=='star'){
      return false
      break
    }
  }
  return true;
}