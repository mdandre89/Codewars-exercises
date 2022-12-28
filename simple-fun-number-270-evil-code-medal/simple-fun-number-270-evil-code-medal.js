function evilCodeMedal(userTime, gold, silver, bronze) {
if(userTime >= bronze){return "None"}
if(userTime >= silver){return "Bronze"}
if(userTime >= gold){return "Silver"}
return "Gold"
}