import json
from pattern3.text.en import singularize

index = None
with open('./index.json', 'r') as f:
  index = json.load(f)

doc_index = None
with open('./doc_index.json', 'r') as f:
  doc_index = json.load(f)

def search(term):
  term = singularize(term)
  if term in index:
    return index[term], [term]
  else:
    return [], ""

def proximity_search(k, terms):
  k += 1
  result = []
  proximities = []
  t1 = singularize(terms[0])
  t2 = singularize(terms[1])
  l1 = index[t1]
  l2 = index[t2]
  ptr1 = 0
  ptr2 = 0

  while ptr1 < len(l1) and ptr2 < len(l2):
    doc1 = l1[ptr1]
    doc2 = l2[ptr2]
    if(doc1["doc_id"] == doc2["doc_id"]):
      l = []
      pos_ptr1 = 0
      pos_ptr2 = 0
      pos_pairs = []
      while pos_ptr1 < len(doc1["positions"]):
        while pos_ptr2 < len(doc2["positions"]):
          if abs(doc1["positions"][pos_ptr1] - doc2["positions"][pos_ptr2]) == k:
            l.append(doc2["positions"][pos_ptr2])
          elif doc2["positions"][pos_ptr2] > doc1["positions"][pos_ptr1]:
            break
          
          pos_ptr2 += 1
        while l and abs(l[0] - doc1["positions"][pos_ptr1]) > k:
          l.remove(l[0])
        for position in l:
          pos_pairs.append([doc1["positions"][pos_ptr1], position])
        pos_ptr1 += 1
      
      if pos_pairs:
        result.append({
          "doc_id": doc1["doc_id"],
          "doc_name": doc_index[str(doc1["doc_id"])],
          "doc_snippet": doc1["doc_snippet"],
          "positions": doc1["positions"]
        })
        t1_pos = doc1["doc_snippet"].find(t1)
        t2_pos = doc1["doc_snippet"].find(t2)
        proximities.append(doc1["doc_snippet"][t1_pos:t2_pos+len(t2)])

      ptr1 += 1
      ptr2 += 1
    elif doc1["doc_id"] < doc2["doc_id"]:
      ptr1 += 1
    else:
      ptr2 += 1
  
  return result, proximities