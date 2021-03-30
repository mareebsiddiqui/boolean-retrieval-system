from set_utils import intersect, union
from search_utils import search

def conjunct(term1, term2):
  lists = []
  words = []

  if(type(term1) != type(())):
    docs, terms = search(term1)
    words.append(terms)
    lists.append(docs)
  else:
    docs, terms = term1
    lists.append(docs)
  
  if(type(term2) != type(())):
    p2, terms = search(term2)
    words.append(terms)
    lists.append(p2)
  else:
    docs, terms = term2
    lists.append(docs)

  return intersect(lists), words
    

def disjunct(term1, term2):
  lists = []
  words = []
  
  if(type(term1) != type(())):
    p1, terms = search(term1)
    words.append(terms)
    lists.append(p1)
  else:
    docs, terms = term1
    lists.append(docs)
  
  if(type(term2) != type(())):
    p2, terms = search(term2)
    words.append(terms)
    lists.append(p2)
  else:
    docs, terms = term2
    lists.append(docs)

  return union(lists), words