def sort_vowels_consonants(s):
    vowels = []
    consonants = []
    
    s = s.lower().replace(" ", "")
    
    for char in s:
        if char in 'aeiou':
            vowels.append(char)
        else:
            consonants.append(char)
    
    vowels_sorted = ''.join(sorted(vowels, key=lambda x: s.index(x)))
    consonants_sorted = ''.join(sorted(consonants, key=lambda x: s.index(x)))
    
    return vowels_sorted, consonants_sorted

s = input("Input one line of words (S) : ")

vowels_sorted, consonants_sorted = sort_vowels_consonants(s)
print("Vowel Characters :")
print(vowels_sorted)
print("Consonant Characters :")
print(consonants_sorted)
