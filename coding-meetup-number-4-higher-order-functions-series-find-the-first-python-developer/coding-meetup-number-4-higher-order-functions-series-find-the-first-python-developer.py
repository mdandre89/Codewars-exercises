def get_first_python(users):
    for j in users:
        if "Python" in j.values():        
            return j.get("first_name") +", "+ j.get("country")
    return "There will be no Python developers"