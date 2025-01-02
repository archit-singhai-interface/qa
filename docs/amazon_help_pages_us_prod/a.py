import json

def convert_to_valid_jsonl():
    # Read the original JSON file
    with open('document_summaries.json', 'r') as f:
        data = json.load(f)

    # Write to JSONL format
    with open('./hello.jsonl', 'w') as f:
        for path, metadata in data['documents'].items():
            # Create a valid entry with the required input field
            entry = {
                "input": {
                    "path": path,
                    "name": metadata.get('name', path.split('/')[-1].replace('.md', '')),
                    "url": metadata.get('url', ''),
                    "section": metadata.get('section', 'General Documentation')
                }
            }
            # Write the line
            f.write(json.dumps(entry) + '\n')
