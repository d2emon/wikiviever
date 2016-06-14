import os

def read_file(filename):
    if not os.path.isfile(filename):
        return False
    f = open(filename, "r")
    data = f.read()
    return data


class Wiki:
    def __init__(self, root):
        self.root = root
        self.path = []
        self.opt = ""
        self.text = ""
        self.items = []

    def subitem(self, id):
        if id < 0:
            if self.path:
                self.path.pop()
                return True
            return False
        else:
            subitem = self.items[id]
            self.path.append(subitem)
            return True

    def filepath(self, filename=""):
        patharr = [self.root] + self.path + [filename]
        return os.path.join(*patharr)

    def loadopt(self):
        self.opt = read_file(self.filepath("__page.opt"))

    def loadtxt(self):
        self.text = read_file(self.filepath("__page.text"))

    def loadsub(self):
        subpath = self.filepath()
        try:
            self.items = next(os.walk(subpath))[1]
        except StopIteration:
            self.items = []
        self.items = list(filter(lambda f: not f.startswith('.') and not f.startswith('_'), self.items))
        self.items.sort()

    def load(self):
        self.loadsub()
        self.loadopt()
        self.loadtxt()
