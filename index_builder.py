from sentence_transformers import SentenceTransformer
import faiss
import json

def build_index(json_file,index_file,model_name="all-MiniLM-L6-v2"):
    model=SentenceTransformer(model_name)
    texts=[]
    metadata=[]
    with open(json_file,'r',encoding='utf-8') as f:
        for line in f:
            data=[json.loads(line) for line in f if line.strip()]
            texts.append(data['chunk'])
            metadata.append({k:v for k,v in data.items() if k!='chunk'})
    
    embeddings=model.encode(texts,show_progress_bar=True,convert_to_numpy=True)
    index=faiss.IndexFlatL2(embeddings.shape(1))
    index.add(embeddings)
    faiss.write_index(index,index_file)
    with open(index_file.replace('.index','_meta.json'),"w",encoding='utf-8'):
        json.dump(metadata,f,ensure_ascii=False)
        print(f"✅ Index saved to {index_file}")

build_index("data\corpus_general.jsonl", "data\general_index.index")
build_index("data\corpus_sher.jsonl", "data\shers_index.index")        

