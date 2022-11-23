from mostCommonWords import most_common_words

def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
            
    return result
    
vals = {'moses': 4, 'mwanafunzi': 2, 'tero': 1}
print(words_often(vals, 2))