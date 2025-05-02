from langchain_ollama import OllamaEmbeddings

embeddings=OllamaEmbeddings(model="gemma:2b")
r1=embeddings.embed_documents(
    [
        "Apha is the first charecter of Greek alphabet",
        "Beta is the second charecter of Greek alphabet"
    ]
)
# print(r1)

r2=embeddings.embed_query("What is the second letter of greek alphabet")


print(r2)