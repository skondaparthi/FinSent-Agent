import faiss
import numpy as np
import finbert_model

def create_index(df):
  embeddings = np.vstack(df['embeds']).astype('float32')
  dim = embeddings.shape[1]
  index = faiss.IndexFlatL2(dim)
  index.add(embeddings)
  return index

def find_similar(text, index, df, k=3):
  embedded = np.array(finbert_model.embed(text)).reshape(1, -1)
  D, I = index.search(embedded, k=k)
  similars = []
  for dist, idx in zip(D[0], I[0]):
    row = df.iloc[idx]
    similars.append({
      "title": row["title"],
      "category": row["category"],
      "dist": float(dist)
    })
  return similars