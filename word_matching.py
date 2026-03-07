def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("The number of words that start and end with the same letter is:", lst)
    return ctr
count = match_words(["abc", "xyz", "aba", "1221"])
print("the number of words that start and end with the same letter is:", count)