x={1,2,3}
print(x)
x={1.0,"hello",(1,2,3)}
print(x)
x={1,2,3,4,3,2}
print(x)
x=set([1,
2,3,4,5])
print(x,"\n")
y=set([0,1,3,4,5])
print("original set - ",x)
print(y)
y.pop()
print("after removing the first element from said set: ",y)
print(y,"\n")