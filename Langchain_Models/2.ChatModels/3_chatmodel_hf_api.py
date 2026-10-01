from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

from dotenv import load_dotenv


load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task= "text-generation",
     huggingfacehub_api_token=os.getenv(
        "HUGGINGFACEHUB_API_TOKEN")

)


model= ChatHuggingFace(llm=llm)

result= model.invoke("what is the capital of India?")

print(result.content)
