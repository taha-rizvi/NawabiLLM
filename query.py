import argparse
import jsonlines
from ragengine import RAGEngine

def load_corpus(jsonl_path):
    with jsonlines.open(jsonl_path) as reader:
        return list(reader)

def display_results(results, general_corpus, sher_corpus):
    print("\n✨ Top Combined Results:\n")
    for i, result in enumerate(results):
        source = result.get("source", "unknown")
        idx = result['index']
        corpus = general_corpus if source == "Lucknow (The capital of Oudh)" else sher_corpus
        chunk_data = corpus[idx]

        print(f"\n🔹 Result {i + 1}")
        print(f"📌 Topic: {chunk_data.get('topic_name', 'N/A')}")
        print(f"📁 Source: {chunk_data.get('source', 'Unknown')}")
        print(f"📄 Text:\n{chunk_data['chunk']}")
        print(f"🎯 Score: {result['score']:.4f}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Query to search for")
    args = parser.parse_args()

    # Load both RAG engines
    engine_general = RAGEngine("data\general_index.index", "data\general_index_meta.json")
    engine_sher = RAGEngine("data\shers_index.index", "data\shers_index_meta.json")

    # Load corpora
    corpus_general = load_corpus("data\corpus_general.jsonl")
    corpus_sher = load_corpus("data\corpus_sher.jsonl")

    # Search both
    results_general = engine_general.search(args.query, top_k=5)
    results_sher = engine_sher.search(args.query, top_k=5)

    # Add index & source labels
    for i, r in enumerate(results_general):
        r['index'] = i
        r['source'] = "Lucknow (The capital of Oudh)"

    for i, r in enumerate(results_sher):
        r['index'] = i
        r['source'] = "Sher (Ghazal Corpus)"

    # Combine and sort by score
    combined_results = sorted(results_general + results_sher, key=lambda x: x['score'])

    # Display
    display_results(combined_results, corpus_general, corpus_sher)

if __name__ == "__main__":
    main()
