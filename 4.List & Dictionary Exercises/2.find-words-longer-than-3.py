def long_words(limit_length,str):
    ## This should find the words longer than 3 from the input string
    ## and return the words as List
    #limit_length = 3
    word_len = []
    txt = str.split()
    #print(txt)
    for x in txt:
        if len(x) > limit_length:
            word_len.append(x)
    return word_len	

print(long_words(4,"The quick brown fox jumps over the lazy dog"))