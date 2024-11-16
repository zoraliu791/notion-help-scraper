import json
import re

def prettify_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(?:\n\s*){2,}', '\n\n', text)
    return text.strip()

def prettify_all_chunks(chunks):
    for chunk in chunks:
        chunk['content'] = prettify_text(chunk['content'])
    return chunks

if __name__ == "__main__":
    with open('chunks.json', 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    prettified_chunks = prettify_all_chunks(chunks)
    with open('prettified_chunks.json', 'w', encoding='utf-8') as f:
        json.dump(prettified_chunks, f, ensure_ascii=False, indent=4)
    print("Prettification complete.")