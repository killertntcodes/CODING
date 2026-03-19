s1={2,3,1}
s2={'a','b','c'}
s3=list(zip(s1,s2))
print("zipped list - ",'\n',s3)

list1=[10,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks = ['reliance', 'tcs', 'infosys']
prices = [2175, 1127, 2750]
new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print('\n'.format(new_dict))