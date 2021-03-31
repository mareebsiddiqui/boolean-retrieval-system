from set_utils import intersect, union
from search_utils import search

'''
  item: Refers to a list of documents. 
'''

'''
  Receives: 2 items
  Returns: Intersection of the 2 items

  If a term is provided, the item is queried to get a list of documents.
'''
def conjunct(item1, item2):
  lists = []
  words = []

  if(type(item1) != type(())):
    docs, items = search(item1)
    words.append(items)
    lists.append(docs)
  else:
    docs, items = item1
    lists.append(docs)
  
  if(type(item2) != type(())):
    p2, items = search(item2)
    words.append(items)
    lists.append(p2)
  else:
    docs, items = item2
    lists.append(docs)

  return intersect(lists), words
    
'''
  Receives: 2 items
  Returns: Union of the 2 items

  If a term is provided, the item is queried to get a list of documents.
'''
def disjunct(item1, item2):
  lists = []
  words = []
  
  if(type(item1) != type(())):
    p1, items = search(item1)
    words.append(items)
    lists.append(p1)
  else:
    docs, items = item1
    lists.append(docs)
  
  if(type(item2) != type(())):
    p2, items = search(item2)
    words.append(items)
    lists.append(p2)
  else:
    docs, items = item2
    lists.append(docs)

  return union(lists), words