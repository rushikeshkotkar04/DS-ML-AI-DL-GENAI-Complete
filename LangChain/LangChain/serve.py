

from fastapi import FastAPI, HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize FastAPI app
app = FastAPI(title="LangChain Server", version="1.0", description="API server using LangChain")

# Initialize the Groq model
model = ChatGroq(model="Gemma2-9b-It", api_key=GROQ_API_KEY)

# Define the prompt template
system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', "{text}")
])

# Initialize the output parser
parser = StrOutputParser()

# Create the chain
chain = prompt_template | model
app=FastAPI()
@app.get("/chain")
def getChain(text,language):
  result=chain.invoke({"language":language,"text":text})
  parts = [part.strip() for part in result.content.strip().split('\n\n') if part.strip()]
  return '\n'.join(parts)

# Run the FastAPI app (for development only)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
