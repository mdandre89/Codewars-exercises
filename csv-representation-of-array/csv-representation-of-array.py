def to_csv_text(array):
    return "\n".join( ','.join(str(i) for i in ls)  for ls in array)