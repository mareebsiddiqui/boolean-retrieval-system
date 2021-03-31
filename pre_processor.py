import os
import re
import json
import string
from pattern3.text.en import singularize

DATASET_DIR = './ShortStories'
STOPWORDS_FILE = './Stopword-List.txt'

'''
  Fetches all the stopwords in a global stopwords array
'''
stopwords = []
with open(STOPWORDS_FILE) as file:
  stopwords = file.read()
  stopwords = stopwords.split("\n")
  stopwords = [stopword for stopword in stopwords if stopword]

index = {'*': []}
word_doc_ptr = {}
simple_index = {}
printable = set(string.printable)

'''
  Receives:
    word: word to add to index,
    doc_id: document to add to against the word,
    i: position to add against that document,
    snippet: snippet of text in which that word appears in the document

  Algorithm:
  1. Check if word is *
  2. If it is, add doc_id to *'s posting
  3. Remove all the non ascii characters from the word
  4. Check if the word is a stopword
  5. Singularize the word
  6. Check if word is in simple_index
  7. If it is, check if doc_id is already in word's simple_index
  8. If not, increment document ptr of word and add document 
     object to the word's index and doc_id to word's simple_index
  9. If it is, add i to word's positions in the index
  10. If word is not in simple_index, add doc_id to word's simple_index
      and document object to word's index. Set doc ptr of word to 0
'''
def index_doc(word, doc_id, i, snippet):
  if word == '*':
    index['*'].append({
      "doc_id": doc_id
    })
  else:
    word = ''.join(filter(lambda x: x in printable, word))
    if(word not in stopwords):
      word = singularize(word)
      if(word and word in simple_index):
        if(doc_id not in simple_index[word]):
          word_doc_ptr[word] += 1
          index[word].append({
            "doc_id": doc_id,
            "doc_snippet": snippet,
            "positions": [i],
          })
          simple_index[word].append(doc_id)
        else:
          doc = index[word][word_doc_ptr[word]]
          doc["positions"].append(i)
      else:
        simple_index[word] = [doc_id]
        index[word] = [{
          "doc_id": doc_id,
          "doc_snippet": snippet,
          "positions": [i]
        }]
        word_doc_ptr[word] = 0

'''
  Iterate over all documents. Read whole file into a variable and clean it.
  Call index_doc on each word with len > 3
'''
for i in range(1, 51):
  with open(os.path.join(DATASET_DIR, str(i)+'.txt')) as file:

    doc_id = file.name.split("/")
    doc_id = doc_id[len(doc_id)-1].split(".")
    doc_id = int(doc_id[0])

    words = file.read()
    words = re.sub(r'\n|--', r' ', words)
    words = re.sub(r'“|”|’|‘|;|,|!|:|\.|\?|\)|\(|\*', r'', words)
    words = words.lower()
    words = re.split(r" |-|\u2014", words)
    words = [word for word in words if word]

    index_doc('*', doc_id, None, None)

    for i, word in enumerate(words):
      snippet = ' '.join(words[max(i-7, 0):i+7])
      if(len(word) >= 3):
        index_doc(word, doc_id, i, snippet)

print("Vocabulary: " + str(len(index.keys())))

with open('./index.json', 'w') as file:
  file.write(json.dumps(index))