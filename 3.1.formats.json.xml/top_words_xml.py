import xml.etree.ElementTree as ET


tree = ET.parse('newsafr.xml')
items = tree.findall('channel/item')
all_words = []
top_words = dict()
for item in items:
    description = item.find('description')
    for word in description.text.split(' '):
        if len(word) > 6:
            all_words.append(word)
for word in all_words:
    top_words[word] = all_words.count(word)
i = 0
sorted_alphabet = []
for key, value in sorted(top_words.items(), key=lambda item: item[1], reverse=True):
    i += 1
    sorted_alphabet.append((key, value))
    if i > 10:
        break
    print(f'{i}. {key} - {value}')
sorted_alphabet.sort()
print(sorted_alphabet)