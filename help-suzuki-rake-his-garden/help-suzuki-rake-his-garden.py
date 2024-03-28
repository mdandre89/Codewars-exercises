def rake_garden(garden):
    return " ".join(["gravel" if i not in "rockgravel" else i for i in garden.split()])