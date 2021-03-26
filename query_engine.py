import os
import json
from pattern3.text.en import singularize

index = None
with open('./index.json', 'r') as f:
  index = json.load(f)

def search(term):
  term = singularize(term)
  result = []
  if term in index:
    for doc in index[term]:
      result.append({
        "doc_id": doc["doc_id"],
        "doc_name": doc["doc_name"],
        "doc_snippet": doc["doc_snippet"],
        "positions": doc["positions"]
      })
  return result

def intersect(results):
  intersection = []
  n = len(results)
  if n > 1:
    results = [item for result in results for item in result]
    freqs = {}
    for doc in results:
      if doc["doc_id"] in freqs:
        freqs[doc["doc_id"]] += 1
        if(freqs[doc["doc_id"]] == n):
          intersection.append(doc)
      else:
        freqs[doc["doc_id"]] = 1
  else:
    intersection = [item for result in results for item in result]

  return intersection

def proximity_search(k, terms):
  k += 1
  result = []
  l1 = index[singularize(terms[0])]
  l2 = index[singularize(terms[1])]
  p1 = 0
  p2 = 0

  while p1 < len(l1) and p2 < len(l2):
    if(l1[p1]["doc_id"] == l2[p2]["doc_id"]):
      l = []
      pp1 = 0
      pp2 = 0
      pos_pairs = []
      while pp1 < len(l1[p1]["positions"]):
        while pp2 < len(l2[p2]["positions"]):
          if abs(l1[p1]["positions"][pp1]["position"] - l2[p2]["positions"][pp2]["position"]) == k:
            l.append(l2[p2]["positions"][pp2])
          elif l2[p2]["positions"][pp2]["position"] > l1[p1]["positions"][pp1]["position"]:
            break
          
          pp2 += 1
        while l and abs(l[0]["position"] - l1[p1]["positions"][pp1]["position"]) > k:
          l.remove(l[0])
        for position in l:
          pos_pairs.append([l1[p1]["positions"][pp1], position])
        pp1 += 1
      
      if pos_pairs:
        result.append({
          "doc_id": l1[p1]["doc_id"],
          "positions": pos_pairs
        })

      p1 += 1
      p2 += 1
    elif l1[p1]["doc_id"] < l2[p2]["doc_id"]:
      p1 += 1
    else:
      p2 += 1
  
  return result

def query(query):
  and_terms = query.split(" and ")
  
  results = []
  
  for term in and_terms:
    term = term.split(" /")
    if len(term) > 1:
      proximity = int(term[1])
      proximity_terms = term[0].split(" ")
      results.append(proximity_search(proximity, proximity_terms))
    else:
      term = term[0]
      if("not " in term):
        term = term.split("not ")[1]
        docs = search(term)
        all_ids = [i for i in range(1, 51)]
        for doc in docs:
          if doc["doc_id"] in all_ids:
            all_ids.remove(doc["doc_id"])
        
        relevant_docs = [{"doc_id": i} for i in all_ids]
        results.append(relevant_docs)
      else:
        results.append(search(term))

  return intersect(results)


  # print(results)