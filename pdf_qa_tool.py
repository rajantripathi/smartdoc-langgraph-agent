from sentence_transformers import SentenceTransformer, util

# Load embedding model (small, fast)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Index PDF documents into embeddings
def index_documents(documents):
    texts = [doc.page_content for doc in documents]
    embeddings = embedding_model.encode(texts, convert_to_tensor=True)
    return texts, embeddings

# Search the indexed PDF with a question
def search_pdf(question, texts, embeddings):
    query_embedding = embedding_model.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, embeddings)[0]
    best_idx = int(scores.argmax())
    return texts[best_idx]
