import re

text = '''
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# Step 1: Fix "iz" на "is",
text = re.sub(r'\biz\b', 'is', text, flags=re.IGNORECASE)

# Step 2. Normalize the sentence and create new

sentences = text.split(".")

normalized_sentences = []
last_words = []

for i in range(len(sentences)):
    sentence = sentences[i]
    if sentence.strip():
        match = re.search(r"[a-zA-Z0-9]", sentence)
        index = match.start()  # position
        char = match.group()  # symbol
        sentence = sentence[:index] + char.upper() + sentence[index + 1:].lower() # capitalize every first letter in sentences
        normalized_sentences.append(sentence + ".")
        words = sentence.split(" ")
        last_words.append(words[-1].strip())
    else:
        normalized_sentences.append(sentence)

summary_sentence = ' '.join(last_words).capitalize() + '.'

normalized_sentences.append(summary_sentence)
normalized_text = ''.join(normalized_sentences)

# Step 3. Calculate number of whitespace characters in this text
matches_space = re.findall(r"\s", normalized_text)

# Result
print("Normalized text:\n")
print(normalized_text)
print("\nWhitespace characters count:", len(matches_space))