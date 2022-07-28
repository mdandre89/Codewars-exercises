function validPass(s){
return /^(?=.*[0-9])(?=.*[a-zA-Z])\w{3,20}$/i.test(s) ? "VALID" : "INVALID"
}