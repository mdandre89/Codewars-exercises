def reverse(num):
    Reverse = 0
    while(num > 0):
        Reminder = num %10
        Reverse = (Reverse *10) + Reminder
        num = num //10
    return Reverse