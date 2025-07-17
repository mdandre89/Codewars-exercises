var Complex = function(real, imag) { 
  this.real = real;
  this.imag = imag || 0 ;
};
Complex.prototype.modulus = function() { 
  return Math.sqrt(this.real**2 + this.imag**2)
};
Complex.prototype.add = function(c) {
  if(typeof c === "number"){
    return new Complex(c + this.real,this.imag)
  }else{
    return new Complex(c.real + this.real, c.imag + this.imag)
  }
};
Complex.prototype.multiply = function(c) { 
  if(typeof c === "number"){
    return new Complex(c * this.real, c*this.imag)
  }else{
    return new Complex(c.real*this.real - c.imag*this.imag, c.real*this.imag + c.imag*this.real)
  }
};