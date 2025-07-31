import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_similar(query, index_path="eip_index.faiss", metadata_path="eip_metadata.npz", k=5):
    query_vec = model.encode([query], convert_to_numpy=True)

    index = faiss.read_index(index_path)
    data = np.load(metadata_path, allow_pickle=True)
    titles = data["titles"]
    files = data["files"]

    D, I = index.search(query_vec, k=k)
    results = []
    for i in I[0]:
        results.append((titles[i], files[i]))
    return results
