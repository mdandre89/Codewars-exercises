function validate(passwo) {
 if(passwo.length>=6 && /[A-Z]+/g.test(passwo)&&/\d+/g.test(passwo)&& /[a-z]+/g.test(passwo)&& !/[^A-Za-z0-9]+/g.test(passwo)){return true}
 return false;
}