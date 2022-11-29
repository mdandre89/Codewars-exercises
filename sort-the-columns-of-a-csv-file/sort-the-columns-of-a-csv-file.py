def sort_csv_columns(csv_file_content):
    first = csv_file_content.split("\n")[0].split(";")
    l = len(first)
    order = sorted(range(l), key=lambda x: sorted(first,key=lambda s: s.lower()).index(first[x]))
    return "\n".join(list(map(lambda x: ";".join([x.split(";")[i] for i in order]),csv_file_content.split("\n")))) 