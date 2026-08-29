# load pdf
# split into chunks
# create embeddings
# store into chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

# load pdf document
data = PyPDFLoader("documents-loaders/wren_and_martin.pdf")
docs = data.load()

# create a chunk from pdf
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# creating embedding model
embeddings_model = MistralAIEmbeddings(model="mistral-embed")

vector_store = Chroma.from_documents(
    documents= chunks,
    embedding= embeddings_model,
    persist_directory = "chroma-db"
)