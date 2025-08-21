# Vowel checker

print('Vowel Checker')

words = ('learn', 'program', 'language', 'python', 'course', 'free', 'study', 'practice', 'work', 'market', 'programmer', 'future', 'dynamax', 'zmove', 'terastal', 'mega evolution', 'paradox', 'pokemon')

for w in words:
    print(f'\n In the word {w.upper()} we have ', end='')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')