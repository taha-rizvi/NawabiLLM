from transformers import pipeline
import json

# 🔍 Zero-shot classifier setup (supports Roman Urdu & multilingual)
classifier = pipeline(
    "zero-shot-classification",
    model="joeddav/xlm-roberta-large-xnli"
)

# ✨ Candidate sentiment labels
labels = ["sad", "romantic", "philosophical", "humorous", "satirical", "critical", "political"]

# 📚 Load your sher corpus
with open("data//corpus_sher.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

annotated_data = []

# 🪄 Run sentiment classification
for line in lines:
    entry = json.loads(line)
    sher = entry["chunk"]

    result = classifier(sher, candidate_labels=labels, multi_label=False)

    # Get top predicted label
    sentiment = result['labels'][0]

    # Add to entry
    entry['sentiment'] = sentiment
    annotated_data.append(entry)

# 💾 Save new annotated file
with open("data//corpus_sher_labeled.jsonl", "w", encoding="utf-8") as f:
    for entry in annotated_data:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print("✅ Sentiment labels added to corpus_sher_labeled.jsonl")