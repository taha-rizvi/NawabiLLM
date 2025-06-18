from ragengine import RAGEngine
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import jsonlines

# Load LLM
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta", device_map="auto", torch_dtype="auto")
rag_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Load corpora
def load_jsonl(file_path):
    with jsonlines.open(file_path, "r") as reader:
        return list(reader)

general_corpus = load_jsonl("data/corpus_general.jsonl")
sher_corpus = load_jsonl("data/corpus_sher.jsonl")

# Build LLM Prompt
def build_prompt(query, enriched_results):
    context = "\n\n".join([f"{i+1}. {item}" for i, item in enumerate(enriched_results)])
    return f"""You are an assistant trained on Urdu poetry and the cultural history of Lucknow.

📚 Context:
{context}

❓ Question:
{query}

🧠 Answer:"""

# Extract actual chunks using metadata
def enrich_results_with_chunks(results, general_corpus, sher_corpus):
    enriched_chunks = []
    for result in results:
        idx = result.get("index", 0)
        corpus_type = result.get("corpus")

        if corpus_type == "general":
            chunk = general_corpus[idx]["chunk"]
        elif corpus_type == "sher":
            chunk = sher_corpus[idx]["chunk"]
        else:
            chunk = "[Unknown corpus]"

        enriched_chunks.append(chunk)
    return enriched_chunks

# Final LLM-based answer generator
def answer_query(query, combined_results, general_corpus, sher_corpus):
    enriched_chunks = enrich_results_with_chunks(combined_results, general_corpus, sher_corpus)
    prompt = build_prompt(query, enriched_chunks)
    output = rag_pipeline(prompt, max_new_tokens=300, do_sample=True, temperature=0.7)[0]['generated_text']
    return output.split("🧠 Answer:")[-1].strip()

# === Main logic ===
if __name__ == "__main__":
    query = input("❓ Ask your question: ")

    general_rag = RAGEngine("data/general_index.index", "data/general_index_meta.json")
    sher_rag = RAGEngine("data/shers_index.index", "data/shers_index_meta.json")

    general_results = general_rag.search(query, top_k=5)
    sher_results = sher_rag.search(query, top_k=5)

    combined_results = general_results + sher_results

    final_response = answer_query(query, combined_results, general_corpus, sher_corpus)

    print("\n🧠 Final Answer:\n")
    print(final_response)

