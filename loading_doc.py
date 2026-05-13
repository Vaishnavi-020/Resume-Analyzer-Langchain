from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader=PyPDFLoader('path.pdf')

docs=loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=80
)

chunks=splitter.split_documents(docs)

n=len(chunks)

for i in range (n):
    print(chunks[i].page_content)
    print('\n')
