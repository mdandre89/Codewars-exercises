function finalAttackValue(x,monsterList){
monsterList.forEach(a => x>=a ?x=a+x:x=x + gcd(x,a))
return x
}

var gcd = function(a, b) {
    if ( ! b) {
        return a;
    }

    return gcd(b, a % b);
};