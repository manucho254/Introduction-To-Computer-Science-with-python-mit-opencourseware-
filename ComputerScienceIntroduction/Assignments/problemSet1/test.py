secret_word = "apple"
letters_guessed = ["a", "b", "p", "l", "v"]
values = [x for x in secret_word if x in letters_guessed]


current_word = []
for i in secret_word:
    if i in letters_guessed:
        current_word.append(i)
    else:
        current_word.append("_ ")
        
print("".join(current_word))

import string

print("".join([x for x in string.ascii_lowercase if x not in letters_guessed]))