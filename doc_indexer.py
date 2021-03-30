import os
import json

DATASET_DIR = './ShortStories'

doc_index = {}

for i in range(1, 51):
  with open(os.path.join(DATASET_DIR, str(i)+'.txt')) as file:
    doc_id = file.name.split("/")
    doc_id = doc_id[len(doc_id)-1].split(".")
    doc_id = int(doc_id[0])

    doc_name = file.readline().strip()

    doc_index[doc_id] = doc_name

with open('./doc_index.json', 'w') as file:
  file.write(json.dumps(doc_index))