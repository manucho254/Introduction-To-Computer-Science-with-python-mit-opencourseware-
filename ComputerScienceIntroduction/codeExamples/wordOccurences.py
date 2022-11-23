def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
            
    return myDict


song = ["moses" , "mwanafunzi", "tero", "moses", "moses", "moses"]

print(lyrics_to_frequencies(song))

def dups(lyrics):
    
    for i in lyrics:
        while lyrics.count(i) > 2:
            lyrics.remove(i)
    
    return lyrics

print(dups([1, 2, 1, 1, 3, 4]))