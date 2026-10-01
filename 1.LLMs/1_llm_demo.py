# from langchain_openai import OpenAI

# from dotenv import load_dotenv

# load_dotenv()



# llm= OpenAI(model='gpt-3.5-turbo-instruct')

# result= llm.invoke("what is the capital of India?")

# print(result)


##Above code is for using OpenAI model

from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")

llm= ChatGoogleGenerativeAI(model='gemini-3.8-flash',
                                google_api_key=api_key,
                               temperature= 0)

result= llm.invoke("What is the capital of India?")

print(result)


