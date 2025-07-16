import faiss
import json
import jsonlines
from sentence_transformers import SentenceTransformer
import numpy as np
class RAGEngine:
    def __init__(self,index_path,metadata_path,model_name="all-MiniLM-L6-v2"):
        print("[*] Loading Embedding model....")
        self.model=SentenceTransformer(model_name)
        print(f"[*] Loading Faiss index from {index_path}....")
        self.index=faiss.read_index(index_path)
        
        print(f"[*] Loading data from {metadata_path}...")
        with open(metadata_path,"r", encoding="utf-8") as reader:
            print(f"📂 Reading from: {metadata_path}")
            corpus=json.load(reader)
            
            self.data=[item for item in corpus]
        
    def search(self,query,top_k=1):
        print("[*] Encoding query....")
        if '?' in query:
            intent = query.split('?')[0].strip() + "?"
            sher = query.split('?')[1].strip()
        else:
            intent = query
            sher = ""
        query=f"{intent}|{sher}"    
        query_embedding=self.model.encode([query],convert_to_numpy=True)
        
        
        print("[*] Performing similarity search...")
        D, I = self.index.search(query_embedding, top_k) 
        print(self.index.ntotal)
        print(len(self.data))
        # results = []
        for i in I[0]:
            
            result = self.data[i]
            # result["score"] = float(D[0][i])
            # result["index"] =idx
            
            # results.append(result)

        return result  