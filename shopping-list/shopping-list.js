function shoppingListCost(arr) {
  var tot = 0
  console.log(groceries)
  arr.forEach(a=>! groceries[a[0]]["bogof"] ? tot+=groceries[a[0]]["price"]*a[1]*(1-groceries[a[0]]["discount"]/100):
   tot+=groceries[a[0]]["price"]*((a[1]-a[1]%2)/2+a[1]%2)*(1-groceries[a[0]]["discount"]/100) )
  return Math.round(tot * 100) / 100
}