from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import os 
import certifi
from dotenv import load_dotenv

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()

llm=HuggingFaceEndpoint(
    model="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

model=ChatHuggingFace(llm=llm)