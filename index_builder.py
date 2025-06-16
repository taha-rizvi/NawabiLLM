# from sentence_transformers import SentenceTransformer
# import faiss
# import json
# import jsonlines

# def build_index(json_file,index_file,model_name="all-MiniLM-L6-v2"):
#     model=SentenceTransformer(model_name)
#     texts=[]
#     metadata=[]
#     # with open(json_file,'r',encoding='utf-8') as f:
#     with jsonlines.open(json_file) as reader:
#         print(json_file)
#         data=list(reader)
#         for item in data:

#             texts.append(item['chunk'])
#             metadata.append({k:v for k,v in item.items() if k!='chunk'})
    
#     embeddings=model.encode(texts,show_progress_bar=True,convert_to_numpy=True)
#     index=faiss.IndexFlatL2(embeddings.shape[1])
#     index.add(embeddings)
#     faiss.write_index(index,index_file)
#     with open(index_file.replace('.index','_meta.json'),"w",encoding='utf-8') as f:
#         json.dump(metadata,f,ensure_ascii=False)
#         print(f"✅ Index saved to {index_file}")
from sentence_transformers import SentenceTransformer
import faiss
import json
import jsonlines
import numpy as np

def build_index(json_file, index_file, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    texts = []
    metadata = []

    with jsonlines.open(json_file) as reader:
        print(f"📂 Reading from: {json_file}")
        data = list(reader)
        for item in data:
            texts.append(item['chunk'])
            # if len(texts.split()) < 20:  # Skip short irrelevant chunks
            #     continue
            # if "library" in texts.lower() or "copyright" in texts.lower():
            #     continue
            metadata.append({k: v for k, v in item.items() if k != 'chunk'})

    print("⚙️ Encoding embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

    # 🔥 Normalize to unit length for cosine similarity
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    print("📦 Building FAISS index with cosine similarity...")
    index = faiss.IndexFlatIP(embeddings.shape[1])  # Use Inner Product
    index.add(embeddings)

    faiss.write_index(index, index_file)
    print(f"✅ FAISS index saved to: {index_file}")

    with open(index_file.replace('.index', '_meta.json'), "w", encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False)
        print(f"✅ Metadata saved to: {index_file.replace('.index', '_meta.json')}")

build_index("data\corpus_general.jsonl", "data\general_index.index")
build_index("data\corpus_sher.jsonl", "data\shers_index.index")        

