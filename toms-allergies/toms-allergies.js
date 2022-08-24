function Allergies(score){
   if(typeof score!= "number"||score==null||score % 1 !== 0){throw new TypeError()}

  this.ALLERGY_SCORES = ["eggs","peanuts","shellfish","strawberries","tomatoes","chocolate","pollen","cats"]
    
  this.isAllergicTo=function(allergen){
    return this.allergies(score).join().indexOf(allergen)==-1? false:true}
      
  this.allergies=function(){
    var t = []
    var j = (score%256).toString(2).split("").reverse().join("")
    for(var i=0;i<j.length;i++){
    if(j[i]==1){ t.push(this.ALLERGY_SCORES[i]) }   }  
    return t.sort()
  }
}