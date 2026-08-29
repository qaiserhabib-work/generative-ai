import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
notes_path = os.path.join(BASE_DIR, "notes.txt")

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1,
)

data = TextLoader(notes_path)

docs = data.load()

chunks = splitter.split_documents(docs)

for i in chunks:
    print(i.page_content)
    print()
    print()