from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# creating embedding model
embeddings_model = MistralAIEmbeddings(model="mistral-embed")

# retrieve embeddings 
vector_store = Chroma(
    embedding_function=embeddings_model,
    persist_directory="chroma-db"
)

# Similarity search
similarity_retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# MMR search
mmr_retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

query = "A noun is a word used as the name of a person, place, or thing."

# print("\n========== SIMILARITY ==========")

# docs = similarity_retriever.invoke(query)

# for i, doc in enumerate(docs):
#     print(f"\n--- Result {i + 1} ---")
#     print(doc.page_content)


print("\n========== MMR ==========")

docs = mmr_retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n--- Result {i + 1} ---")
    print(doc.page_content)