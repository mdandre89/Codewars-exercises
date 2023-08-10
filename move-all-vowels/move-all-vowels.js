function moveVowel(input) {
return (input.match(/[^aeiou]/g)||[]).join("") + (input.match(/[aeiou]/g)||[]).join("")
}