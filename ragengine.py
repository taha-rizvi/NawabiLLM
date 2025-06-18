import faiss
import json
from sentence_transformers import SentenceTransformer
import numpy as np
class RAGEngine:
    def __init__(self,index_path,metadata_path,model_name="all-MiniLM-L6-v2"):
        print("[*] Loading Embedding model....")
        self.model=SentenceTransformer(model_name)
        print(f"[*] Loading Faiss index from {index_path}....")
        self.index=faiss.read_index(index_path)
        
        print(f"[*] Loading metadata from {metadata_path}...")
        with open(metadata_path,encoding='utf-8') as f:
            self.metadata=json.load(f)
    def search(self,query,top_k=5):
        print("[*] Encoding query....")
        query_embedding=self.model.encode([query],convert_to_numpy=True)
        
        query_embedding=query_embedding/np.linalg.norm(query_embedding, axis=1, keepdims=True)
        
        print("[*] Performing similarity search...")
        D, I = self.index.search(query_embedding, top_k) 
        
        results = []
        for i,idx in enumerate(I[0]):
            
            result = dict(self.metadata[idx])
            result["score"] = float(D[0][i])
            result["index"] =idx
            result['corpus'] = self.metadata[idx].get('corpus', 'unknown')
            results.append(result)

        return results   