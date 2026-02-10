x= input("enter a word: ")
y= input("enter a character: ")
count=0
i= 0
while i < len(x):
    if x[i] == y:
        count= count+1
    i= i+1
print("number of times", x, " appears in the word is: ", count)