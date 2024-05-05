import torch


class ICD9Embeddings:
    def __init__(self, filename="./ic9_embeddings.txt"):
        self.embedding_filename = filename
        self.icd9_to_embeddings = self._read_embeddings()

    def _read_embeddings(self):
        icd9_to_embeddings = {}
        with open(self.embedding_filename, "r") as infile:
            data = infile.readlines()
            for row in data:
                eles = row.strip().split(" ")
                name = eles[0]
                embedding = eles[1:]
                code = name[4:]

                code = code.replace(".", "")
                if len(code) > 5 or len(code) < 3:
                    print("code is bad")
                icd9_to_embeddings[code] = torch.tensor(
                    [float(i) for i in embedding], dtype=torch.float32
                )
        return icd9_to_embeddings

    def get(self, code):
        if code in self.icd9_to_embeddings:
            return self.icd9_to_embeddings[code]
        else:
            return None

    def get_idx_to_embedding(self, token2idx):
        idx2embedding = {}
        for code in self.icd9_to_embeddings.keys():
            if code in token2idx:
                idx2embedding[token2idx[code]] = self.icd9_to_embeddings[code]

        return idx2embedding
