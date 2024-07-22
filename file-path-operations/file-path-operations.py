class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath

    def extension(self):
        return self.filepath.split(".")[1]
        
    def filename(self):
        path = self.filepath.split(".")[0]
        return path.split("/")[-1]
        
    def dirpath(self):
        path = self.filepath.split(".")[0]
        return "/".join(path.split("/")[:-1]) + "/"
 