import torch


class ICD9Embeddings:
    def __init__(self, filename="./ic9_embeddings.txt"):
        self.embedding_filename = filename
        # self.icd9_to_embeddings = self._read_embeddings()
        self.icd9_to_embeddings = self._read_embeddings_trunc()
        self.embedding_size = 300

    # this reads the 5 digit code correctly
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

    # this does the opposite of greedy it basically just takes the last icd_9 with the first three that match
    def _read_embeddings_trunc(self):
        icd9_to_embeddings = {}
        codes_lost = 0
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
                trunc_code = code[:3]
                # print(trunc_code)
                if trunc_code in icd9_to_embeddings:
                    codes_lost += 1

                icd9_to_embeddings[trunc_code] = torch.tensor(
                    [float(i) for i in embedding], dtype=torch.float32
                )
        # print('codes_lost', codes_lost)
        return icd9_to_embeddings

    def get(self, code):
        if code in self.icd9_to_embeddings:
            return self.icd9_to_embeddings[code]
        else:
            return None

    def get_idx_to_embedding(self, token2idx):
        idx2embedding = {}
        for code, idx in token2idx.items():
            if code in self.icd9_to_embeddings:
                idx2embedding[idx] = self.icd9_to_embeddings[code]
            else:
                idx2embedding[idx] = torch.zeros(
                    self.embedding_size, dtype=torch.float32
                )
                # print("code is not in icd9 embeddings", code)
            print()

        return idx2embedding
