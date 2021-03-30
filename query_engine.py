import os
import re
import string
from search_utils import search, proximity_search
from boolean_utils import conjunct, disjunct
from set_utils import complement

def is_operand(op):
  operators = ['and', 'or', 'not', '(', ')', '/']
  return op not in operators

priority = {
  '/': 4,
  'not': 3,
  'and': 2,
  'or': 1,
  '(': 0
}
def get_postfix(infix):
  infix = re.sub(r'\(', r'( ', infix)
  infix = re.sub(r'\)', r' )', infix)
  infix = re.sub(r'/', r'/ ', infix)
  infix = infix.split(" ")
  stack = []
  postfix = []

  for term in infix:
    if is_operand(term):
      postfix.append(term)
    else:
      if term == '(':
        stack.append(term)
      elif term == ')':
        operator = stack.pop()
        while operator != '(':
          postfix.append(operator)
          operator = stack.pop()
      else:
        while len(stack) > 0 and priority[term] <= priority[stack[-1]]:
          postfix.append(stack.pop())
        stack.append(term)

  while len(stack) > 0:
    postfix.append(stack.pop())
    
  return postfix

punctuation = list(set(string.punctuation))
punctuation.remove('/')
punctuation.remove('(')
punctuation.remove(')')
def query(query):
  query = query.lower()
  query = ''.join(filter(lambda x: x not in punctuation, query))
  query = re.sub(r'-', r'', query)

  postfix = get_postfix(query)

  if len(postfix) > 1:

    stack = []
    results = []

    while len(postfix) > 0:
      term = postfix.pop(0)
      if is_operand(term):
        stack.append(term)
      else:
        if term == 'and':
          t2 = stack.pop()
          t1 = stack.pop()
          stack.append(conjunct(t1, t2))
        elif term == 'or':
          t2 = stack.pop()
          t1 = stack.pop()
          stack.append(disjunct(t1, t2))
        elif term == '/':
          k = int(stack.pop())
          t2 = stack.pop()
          t1 = stack.pop()
          stack.append(proximity_search(k, [t1, t2]))
        elif term == 'not':
          t1 = stack.pop()
          stack.append(complement(t1))

    return stack.pop()
  else:
    return search(query)