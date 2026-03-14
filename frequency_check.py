test_dic={'codingal': 2, 'is': 2, 'the': 2, 'best': 2, 'for': 2, 'coding': 1}
print("the original dictionary : " + str(test_dic))
K=2
res=0
for key in test_dic:
    if test_dic[key] == K:
        res += 1
print("the frequency of the K is : " + str(res))