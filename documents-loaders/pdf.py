from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



data = PyPDFLoader("documents-loaders/Qaiser_Resume.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)
