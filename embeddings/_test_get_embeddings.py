from get_embeddings import ICD9Embeddings

embeddings = ICD9Embeddings()
print(len(embeddings.get('07070')))

print(repr(embeddings.get('07070')))