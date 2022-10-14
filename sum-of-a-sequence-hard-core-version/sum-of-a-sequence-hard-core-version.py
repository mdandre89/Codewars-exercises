from decimal import * 
def sequence_sum(beg, end, step):
    max = Decimal((end - beg)//step)
    return (Decimal(max)+1)*Decimal(beg)+Decimal(step)*(max)*(max+1)/2 if (end-beg)*step>0 else 0