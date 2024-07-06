# WAP to input a sentence and count the frequency of all characters.
sentence = input("Enter a sentence: ")
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
for char in char_frequency:
    print(f"'{char}': {char_frequency[char]}",end=' ')
