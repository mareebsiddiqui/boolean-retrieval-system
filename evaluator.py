import query_engine

with open('./ShortStories.txt', 'r') as f:
  data = f.read().split("\n")
  data = [line for line in data if line]

  for i in range(0, len(data), 2):
    query = data[i].split(":")[1].strip()
    result = data[i+1].split(":")[1].strip().split(",")

    query_results, terms = query_engine.query(query)
    print("Query {i}".format(i = i/2 + 1))
    print("Result-set: ", end="", flush=True)
    if query_results:
      relevant = 0
      for doc in query_results:
        print("{doc_id},".format(doc_id=doc["doc_id"]), end="", flush=True)
        if str(doc["doc_id"]) in result:
          relevant += 1
      print()
      print("Precision:", relevant/len(query_results), ", Recall:", relevant/len(result))
      print()
    else:
      print("No results")