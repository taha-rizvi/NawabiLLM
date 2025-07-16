import json
import jsonlines
import random
input_path = "data//corpus_general.jsonl"
output_path = "data//corpus_general_cleaned.jsonl"



with jsonlines.open(input_path, mode='r') as reader, jsonlines.open(output_path, mode='w') as writer:
    for obj in reader:
        topic = obj.get("topic", "").strip().lower()
        if topic == "misc" or topic == "":
            obj["topic"] = "Lucknow"
        writer.write(obj)

print(f"✅ Cleaned general corpus saved to {output_path}")
