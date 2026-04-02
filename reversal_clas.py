class string:
    def __init__(self, value):
        self.value = value

    def reverse(self):
        return self.value[::-1]
str = input("Enter a string: ")
str_obj = string(str)
reversed_str = str_obj.reverse()
print("Reversed string:", reversed_str)