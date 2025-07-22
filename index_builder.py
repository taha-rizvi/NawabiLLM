from sentence_transformers import SentenceTransformer
import faiss
import json
import jsonlines
import numpy as np

def build_index(json_file, index_file, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    texts = []
    metadata=[]

    with jsonlines.open(json_file) as reader:
        print(f" Reading from: {json_file}")
        data=list(reader)
        for item in data:
            prompt=item["prompt"]
            response=item["response"]
            if '?' in prompt:
                intent=prompt.split('?')[0].strip()+'?'
                sher=prompt.split('?')[1].strip()
            else: 
                intent=prompt
                sher=""    
            combined=f"{intent}|{sher}"
            texts.append(combined)
            metadata.append(response)

        

    print(" Encoding embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    
    index = faiss.IndexFlatL2(embeddings.shape[1])  
    index.add(embeddings)

    faiss.write_index(index, index_file)
    print(f"✅ FAISS index saved to: {index_file}")

    with open(index_file.replace('.index', '_meta.json'), "w", encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False)
        print(f"✅ Metadata saved to: {index_file.replace('.index', '_meta.json')}")

build_index("data/combined_corpus.jsonl","data/index_combined_corpus.index")


