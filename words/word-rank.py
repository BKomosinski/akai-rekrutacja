import re
from collections import Counter

# Zbieramy wejściowe teksty od użytkownika
texts = []
while True:
    text = input("Wprowadź tekst (wpisz 'stop' aby zakończyć): ")
    if text == 'stop':
        break
    texts.append(tekst)

# Łączymy teksty w jedną długą ciągłą, usuwamy znaki interpunkcyjne i konwertujemy litery na małe
alltext = re.sub(r'[^\w\s]', '', ' '.join(texts).lower())

# Rozbijamy tekst na słowa i zliczamy wystąpienia każdego słowa
words_counter = Counter(alltext.split())

# Tworzymy listę (słowo, liczba wystąpień) i sortujemy ją po liczbie wystąpień
wordlist = [(word, number) for word, number in words_counter.items()]
wordlist.sort(key=lambda x: x[1], reverse=True)

# Wypisujemy ranking najpopularniejszych słów
for i, (word, number) in enumerate(wordlist[:3]):
    print(f"{i+1}. \"{word}\" - {number}")
