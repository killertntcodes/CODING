class bird  :
    def __init__(self):
        print("the bird is ready")
    def whosdis(self):
        print("bird")
    def swim(self):
        print("swim faster")
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
    def whosdis(self):
        print("penguin")
    def run(self):
        print("run faster")
peggy = penguin()
peggy.whosdis()
peggy.swim()
peggy.run()