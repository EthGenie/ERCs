import os
import re
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from markdown import markdown
from bs4 import BeautifulSoup

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_md(md_content):
    html = markdown(md_content)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()

def build_index(eip_folder="./ERCS", index_path="eip_index.faiss", metadata_path="eip_metadata.npz"):
    texts = []
    titles = []
    file_paths = []

    for filename in os.listdir(eip_folder):
        if filename.endswith(".md"):
            path = os.path.join(eip_folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                text = extract_text_from_md(content)
                title_match = re.search(r"^title:\s*(.*)", content, re.IGNORECASE | re.MULTILINE)
                title = title_match.group(1) if title_match else filename
                titles.append(title)
                texts.append(text)
                file_paths.append(filename)

    embeddings = model.encode(texts, convert_to_numpy=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, index_path)
    np.savez(metadata_path, titles=titles, files=file_paths)
    print("✅ Index built and saved.")
