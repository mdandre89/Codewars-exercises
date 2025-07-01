function countSmileys(arr) {
var t = arr.join("d")
return (t.match(/(:|;)(-|~)?(\)|D)/g)||[]).length
}