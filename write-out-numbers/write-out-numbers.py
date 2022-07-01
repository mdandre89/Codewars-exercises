dictio = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",
13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"} 
decimal = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
def number2words(n):    
    if n < 20:
        return dictio[n]
    if n < 100:
        return decimal.get(n//10,"")+"-"+dictio[n%10] if n%10 != 0 else decimal[n//10]
    if n < 1000:
        if n % 100 == 0:
            return dictio[n//100]+" hundred"
        return dictio[n//100]+" hundred "+number2words(int(str(n)[-2:]))
    if n < 1000000:   
        if n % 1000 == 0:
            return number2words(int(str(n)[:len(str(n))-3]))+" thousand"
        return  number2words(int(str(n)[:len(str(n))-3]))+" thousand "+ number2words(int(str(n)[-3:]))