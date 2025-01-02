import json

# Read the original JSON file
with open('document_summaries.json', 'r') as f:
    data = json.load(f)

# Write to JSONL format
with open('document_summaries3.jsonl', 'w') as f:
    for path, metadata in data['documents'].items():
        # Combine all fields into a single text string
        text_content = f"{path} {metadata.get('name', '')} {metadata.get('url', '')} {metadata.get('section', '')}"
        
        # Create entry with the required format
        entry = {
            "inputs": {
                "text": text_content.strip()
            }
        }
        f.write(json.dumps(entry) + '\n')
