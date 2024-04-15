def get_number_from_string(string):
    return int("".join([i for i in string if i.isdigit()]))