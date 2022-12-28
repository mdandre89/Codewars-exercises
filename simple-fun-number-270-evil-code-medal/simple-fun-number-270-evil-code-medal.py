def evil_code_medal(user_time, gold, silver, bronze):
    if user_time >= bronze:
        return "None"
    if user_time >= silver:
        return "Bronze"
    if user_time >= gold:
        return "Silver"
    return "Gold"