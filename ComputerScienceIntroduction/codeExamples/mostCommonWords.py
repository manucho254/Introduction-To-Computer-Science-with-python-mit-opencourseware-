def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    
    words = []
    
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
            
    return (words, best)

vals = {'moses': 4, 'mwanafunzi': 1, 'tero': 1}

print(most_common_words(vals))