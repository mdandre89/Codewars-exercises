class Dinglemouse {

  constructor( firstName, lastName ){
    this.firstName = firstName;
    this.lastName = lastName;
  }
  
  getFullName() {
    if(this.firstName && this.lastName) {
        return this.firstName + " " + this.lastName
    }
    
    return (this.firstName) ? this.firstName : this.lastName; 
  }
  
}