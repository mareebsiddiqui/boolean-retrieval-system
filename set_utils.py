from search_utils import search

def intersect_two(l1, l2):
  ptr1 = 0
  ptr2 = 0

  relevant_docs = []

  while ptr1 < len(l1) and ptr2 < len(l2):
    doc1 = l1[ptr1]
    doc2 = l2[ptr2]
    if(doc1["doc_id"] == doc2["doc_id"]):
      relevant_docs.append(doc1)
      ptr2 += 1
      ptr1 += 1
    elif(doc1["doc_id"] < doc2["doc_id"]):
      ptr1 += 1
    else:
      ptr2 += 1
  
  return relevant_docs

def intersect(lists):
  n = len(lists)
  if(n > 1):
    i = 2
    intersection = intersect_two(lists[0], lists[1])
    while i < n:
      intersection = intersect_two(intersection, lists[i])
      i += 1
    return intersection
  else:
    return lists[0]

def union_two(l1, l2):
  ptr1 = 0
  ptr2 = 0

  relevant_docs = []

  while ptr1 < len(l1) and ptr2 < len(l2):
    doc1 = l1[ptr1]
    doc2 = l2[ptr2]
    if(doc1["doc_id"] == doc2["doc_id"]):
      relevant_docs.append(doc1)
      ptr2 += 1
      ptr1 += 1
    elif(doc1["doc_id"] < doc2["doc_id"]):
      relevant_docs.append(doc1)
      ptr1 += 1
    else:
      relevant_docs.append(doc2)
      ptr2 += 1
  
  while ptr1 < len(l1):
    relevant_docs.append(l1[ptr1])
    ptr1 += 1

  while ptr2 < len(l2):
    relevant_docs.append(l2[ptr2])
    ptr2 += 1

  return relevant_docs

def union(lists):
  n = len(lists)
  if(n > 1):
    i = 2
    unioned = union_two(lists[0], lists[1])
    while i < n:
      unioned = union_two(unioned, lists[i])
      i += 1
    return unioned
  else:
    return lists[0]

def complement(term):
  docs = []
  
  if(type(term) != type(())):
    docs, _ = search(term)
  else:
    docs, _ = term
  
  all_docs, _ = search('*')

  if(len(docs) < 1):
    return all_docs, []
  else:
    ptr1 = 0
    ptr2 = 0

    relevant_docs = []

    while ptr1 < len(docs) and ptr2 < len(all_docs):
      doc1 = docs[ptr1]
      doc2 = all_docs[ptr2]
      if(doc1["doc_id"] > doc2["doc_id"]):
        relevant_docs.append(doc2)
        ptr2 += 1
      elif(doc1["doc_id"] == doc2["doc_id"]):
        ptr2 += 1
        ptr1 += 1
    
    while ptr2 < len(all_docs):
      relevant_docs.append(all_docs[ptr2])
      ptr2 += 1
    
    return relevant_docs, []