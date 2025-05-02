from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader('E:\\DS_ML_AI_DL_GENAI_practice\\LangChain\\LangChain\\FAISS\\speech.txt')

documents=loader.load()
text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=30)

text_splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=30)
docs=text_splitter.split_documents(documents)
embeddings=OllamaEmbeddings(model="llama3")
db=Chroma.from_documents(docs,embeddings)
# print(db)
query="How does the speaker describe the desired outcome of the wat?"
results=db.similarity_search(query)
# print(results[0].page_content)

## To convert into retriever

retriever=db.as_retriever()
retriever.invoke(query)


### Simillarity search with score: Based on manhatten Score

docs_and_score=db.similarity_search_with_score(query)
print(docs_and_score)