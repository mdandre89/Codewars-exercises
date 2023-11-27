function missingWord(nums, str) {
  var str = str.match(/[a-z]/gi) 
  var nums = nums.sort((a,b)=>a-b)
  var l = str.length
  var n = nums.reduce((a,b)=>Math.max(a,b))
  return n>l? "No mission today" : nums.map((i)=>str[i].toLowerCase()).join("")
}