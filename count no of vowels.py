vowels = 'aeiou'

sentence = "This is a beautiful thing"

sentence = sentence.casefold() #became case insensitive

count = {}.fromkeys(vowels,0)

for char in sentence:
    if char in vowels:
        count[char]+=1

print(count)

