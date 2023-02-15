def solution(roman):
    dictio = {"I":1,"V":5,"X":10,"L":50,"C":100,"M":1000,"D":500}
    t=0
    if "IV" in roman:
        roman = roman.replace("IV","")  
        t+=4
    if "XL" in roman:
        roman = roman.replace("XL","")  
        t+=40
    if "IX" in roman:
        roman = roman.replace("IX","") 
        t+=9
    if "CM" in roman:
        roman = roman.replace("CM","") 
        t+=900
    if "CD" in roman:
        roman = roman.replace("CD","") 
        t+=400    
    for i in roman:
        t+=dictio[i]
    return t