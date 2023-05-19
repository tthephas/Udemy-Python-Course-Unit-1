# python pig latin project
# using loops, data structures and lists

# happy >>> appyHay
# glove >>> oveGlay

# get sentence from user
original = input("What sentence would you like to change to pig latin?: ").strip().lower()

# split sentence into words
words = original.split()

# loop thru the words and convert to pig latin
new_words = []

for word in words:
    # if start with vowel, just add 'yay'
    if word[0] in 'aeiou':
        new_word = word + 'yay'
        new_words.append(new_word)
    # otherwise , move first consanant cluster to end and end 'ay'
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + 'ay'
        new_words.append(new_word)     

# put words back together
output = " ".join(new_words)

# outpu the final string
print(output)       


