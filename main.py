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

# creating retrieve
retriever = vector_store.as_retriever(
    search_type = "mmr",
    search_kwargs={
        "k":4,
        "fetch_k":10,
        "lambda_mult":0.5
    }
)

llm = ChatMistralAI(model="mistral-small-2506", temperature=0 )

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a strict RAG assistant.

The CONTEXT below is your ONLY source of information.

IMPORTANT:
- You have NO access to external knowledge.
- Ignore everything you learned during training.
- Never answer from your own knowledge.
- Never guess.
- Never make assumptions.
- Never add information that is not explicitly present in the CONTEXT.
- Every factual statement in your answer must be supported by the CONTEXT.
- If the CONTEXT does not contain the answer, say exactly:

"I could not find the answer in the document."

CONTEXT:
{context}
"""
        ),
        (
            "human",
            """Question: {question}

Answer using ONLY the provided CONTEXT."""
        )
    ]
)

print("Rag system created ")

print("press 0 to exit ")

while True:
    query = input("You : ")
    if query == "0":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")


