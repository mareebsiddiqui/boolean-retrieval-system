import os
import json
from pattern3.text.en import singularize

index = None
with open('./index.json', 'r') as f:
  index = json.load(f)

def search(term):
  term = singularize(term)
  if term in index:
    return index[term], term
  else:
    return [], ""

def intersect_two(l1, l2):
  p1 = 0
  p2 = 0

  relevant_docs = []

  while p1 < len(l1):
    while p2 < len(l2):
      if(l1[p1]["doc_id"] == l2[p2]["doc_id"]):
        relevant_docs.append(l2[p2])
        break
      elif(l1[p1]["doc_id"] < l2[p2]["doc_id"]):
        break
      p2 += 1
    p1 += 1
  
  return relevant_docs

def intersect(results):
  n = len(results)
  if(n > 1):
    i = 2
    intersection = intersect_two(results[0], results[1])
    while i < n:
      intersection = intersect_two(intersection, results[i])
      i += 1
    return intersection
  else:
    return results[0]

def proximity_search(k, terms):
  k += 1
  result = []
  proximities = []
  t1 = singularize(terms[0])
  t2 = singularize(terms[1])
  l1 = index[t1]
  l2 = index[t2]
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
          if abs(l1[p1]["positions"][pp1] - l2[p2]["positions"][pp2]) == k:
            l.append(l2[p2]["positions"][pp2])
          elif l2[p2]["positions"][pp2] > l1[p1]["positions"][pp1]:
            break
          
          pp2 += 1
        while l and abs(l[0] - l1[p1]["positions"][pp1]) > k:
          l.remove(l[0])
        for position in l:
          pos_pairs.append([l1[p1]["positions"][pp1], position])
        pp1 += 1
      
      if pos_pairs:
        result.append({
          "doc_id": l1[p1]["doc_id"],
          "doc_name": l1[p1]["doc_name"],
          "doc_snippet": l1[p1]["doc_snippet"],
          "positions": l1[p1]["positions"]
        })
        t1_pos = l1[p1]["doc_snippet"].find(t1)
        t2_pos = l1[p1]["doc_snippet"].find(t2)
        proximities.append(l1[p1]["doc_snippet"][t1_pos:t2_pos+len(t2)])

      p1 += 1
      p2 += 1
    elif l1[p1]["doc_id"] < l2[p2]["doc_id"]:
      p1 += 1
    else:
      p2 += 1
  
  return result, proximities

def get_complement(search_fn, params):
  docs, terms = search_fn(*params)
  all_docs, terms = search('*')

  if(len(docs) < 1):
    return all_docs
  else:
    p1 = 0
    p2 = 0

    relevant_docs = []

    while p1 < len(docs):
      while p2 < len(all_docs):
        if(docs[p1]["doc_id"] > all_docs[p2]["doc_id"]):
          relevant_docs.append(all_docs[p2])
        elif(docs[p1]["doc_id"] == all_docs[p2]["doc_id"]):
          p2 += 1
          break
        p2 += 1
      p1 += 1
    
    while p2 < len(all_docs):
      relevant_docs.append(all_docs[p2])
      p2 += 1
    
    return relevant_docs

def query(query):
  and_terms = query.split(" and ")
  
  results = []
  words = []
  
  for term in and_terms:
    term = term.split(" /")
    if len(term) > 1:
      proximity = int(term[1])
      if("not " in term[0]):
        proximity_terms = term[0].split("not ")[1]
        proximity_terms = proximity_terms.split(" ")
        results.append(get_complement(proximity_search, [proximity, proximity_terms]))
      else:
        proximity_terms = term[0].split(" ")
        search_results, terms = proximity_search(proximity, proximity_terms)
        results.append(search_results)
        words.append(terms)
    else:
      term = term[0]
      if("not " in term):
        term = term.split("not ")[1]
        results.append(get_complement(search, [term]))
      else:
        search_results, terms = search(term)
        words.append(terms)
        results.append(search_results)

  return intersect(results), words


  # print(results)