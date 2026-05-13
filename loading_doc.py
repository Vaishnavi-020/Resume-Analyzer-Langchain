from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

loader=PyPDFLoader('path.pdf')

docs=loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=80
)

chunks=splitter.split_documents(docs)

# n=len(chunks)

# for i in range (n):
#     print(chunks[i].page_content)
#     print('\n')

text=[chunk.page_content for chunk in chunks]

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

chunk_embeddings=embeddings.embed_documents(text)

print(chunk_embeddings[0])
print(len(chunk_embeddings))