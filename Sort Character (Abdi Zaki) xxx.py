vocal = ['a', 'i', 'u', 'e', 'o']
vocals = []
consonant = []

word = input("Input one line of words (S) :")
list_word = list(word)

for words in list_word:
    if words in vocal:
        vocals.append(words)
    else: consonant.append(words)

vocals.sort()
print('Vowel Characters :')
print(''.join(vocals))
print('Consonant Characters :')
print(''.join(consonant).replace(' ', '').lower())