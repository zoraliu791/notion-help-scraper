def chunk_text(text, max_length=750):
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) + 2 > max_length:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""
        current_chunk += para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def chunk_all_articles(articles):
    all_chunks = []
    for url, text in articles.items():
        chunks = chunk_text(text)
        for chunk in chunks:
            all_chunks.append({
                'url': url,
                'content': chunk
            })
    return all_chunks

if __name__ == "__main__":
    import json
    with open('articles.json', 'r', encoding='utf-8') as f:
        articles = json.load(f)
    chunks = chunk_all_articles(articles)
    with open('chunks.json', 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=4)
    print(f"Total chunks created: {len(chunks)}")