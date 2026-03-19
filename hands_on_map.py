n1=[1, 2, 3]
n2=[3, 4, 5]
result=map(lambda x,y: x+y, n1, n2)
print("addition of two lists - ")
print(list(result))

nums=[1, 2, 3, 4, 5]
def sq(n):
    return n*n
square= list(map(sq, nums))
print("squares of numbers - ")
print(square)