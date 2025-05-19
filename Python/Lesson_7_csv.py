import csv
from collections import Counter

words = Counter()
letter = Counter()

# Read file
with open("news_feed.txt", "r") as file:
    text = file.read()

# Calculate number of words
words = text.lower().split()
word_counter = Counter(words)

# Calculate letters
for char in text:
    if char.isalpha():  # исключаем пробелы и знаки препинания
        key = char.lower()
        if key in letter:
            letter[key] = (letter[key][0] + 1, letter[key][1])
        else:
            letter[key] = (1, 0)
        if char.isupper():
            letter[key] = (letter[key][0], letter[key][1] + 1)

# Create statistics
letter_stat = []
for i, (l_all, l_upper) in letter.items():
    percent = round((l_upper / l_all) * 100, 2)
    letter_stat.append([i, l_all, l_upper, percent])

# Write words
with open('word_count.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['word', 'count'])
    for word, count in word_counter.items():
        writer.writerow([word, count])

# Write statistics
with open('letter_count.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['letter', 'count_all', 'count_uppercase', 'percentage'])
    for row in letter_stat:
        writer.writerow(row)



