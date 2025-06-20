from ragengine import RAGEngine
import jsonlines
from llama_cpp import Llama

# Load GGUF LLM
llm = Llama(
    model_path="C:\\Users\mtaha\\.cache\\huggingface\\hub\\models--TheBloke--Mistral-7B-Instruct-v0.2-GGUF\\snapshots\\3a6fbf4a41a1d52e415a4958cde6856d34b2db93\\mistral-7b-instruct-v0.2.Q2_K.gguf",
    n_ctx=1024,
    n_threads=6,  # set according to your CPU
    verbose=False
)

# Load corpus
def load_jsonl(file_path):
    with jsonlines.open(file_path, "r") as reader:
        return list(reader)

general_corpus = load_jsonl("data/corpus_general.jsonl")
sher_corpus = load_jsonl("data/corpus_sher.jsonl")

# Enrich results with chunks
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

# Build prompt
def build_prompt(query, enriched_chunks):
    context = "\n\n".join([f"{i+1}. {chunk}" for i, chunk in enumerate(enriched_chunks)])
    return f"""You are an assistant trained on Urdu poetry and the cultural history of Lucknow.

📚 Context:
{context[:1024]}

❓ Question:
{query}

🧠 Answer:"""

# Ask the model
def answer_query(query, combined_results, general_corpus, sher_corpus):
    enriched_chunks = enrich_results_with_chunks(combined_results, general_corpus, sher_corpus)
    prompt = build_prompt(query, enriched_chunks)

    print("\n📨 Prompt sent to LLM:\n")
    print(prompt[:500] + "...\n")  # Show only first 500 chars for sanity

    output = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7
    )

    return output["choices"][0]["message"]["content"]

# === Main Flow ===
if __name__ == "__main__":
    query = input("❓ Ask your question: ")

    general_rag = RAGEngine("data/general_index.index", "data/general_index_meta.json")
    sher_rag = RAGEngine("data/shers_index.index", "data/shers_index_meta.json")

    general_results = general_rag.search(query, top_k=3)
    sher_results = sher_rag.search(query, top_k=2)

    combined_results = general_results + sher_results

    final_response = answer_query(query, combined_results, general_corpus, sher_corpus)

    print("\n🧠 Final Answer:\n")
    print(final_response)