import json

def add_source_to_chunks(input_file, output_file="corpus_general.jsonl", source="Lucknow (The Capital of Oudh)"):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        count = 0
        for line in infile:
            if line.strip():  # avoid blank lines
                chunk_data = json.loads(line)
                chunk_data['source'] = source
                outfile.write(json.dumps(chunk_data, ensure_ascii=False) + "\n")
                count += 1

    print(f"✅ {count} chunks processed and saved to `{output_file}` with source = '{source}'.")

# 🔥 Run it
add_source_to_chunks("manual_topic_chunks.jsonl")