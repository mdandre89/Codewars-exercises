function extractIds(data){
  let idsList = []
  const traverse = (obj) =>{
    for (const [key, value] of Object.entries(obj)) {
      if(key == 'id'){
        idsList.push(value)
      }
      
      if(key == 'items'){
        for (let item of value){
          traverse(item)
        }
      }

    }
  }
  traverse(data)
  return idsList
}