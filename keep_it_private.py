class myClass:
    _private_var = 27
    def _privMeth(self):
        print("im inside class myClass")
    def hello(self):
        print("Private variable value ", myClass._private_var)
foo = myClass()
foo.hello()
foo._privMeth