from get_embeddings import ICD9Embeddings

embeddings = ICD9Embeddings()
print(len(embeddings.get('5723')))
print(len(embeddings.get('78959')))
print(len(embeddings.get('5715')))
print(len(embeddings.get('07070')))

# print(repr(embeddings.get('5723')))