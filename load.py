
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkdin_scraper import scrape_linkedin_profile

# Load environment variables if needed
load_dotenv()

# Define the prompt template correctly
template = """Given the linkdin information of the person: {my_prompt}, provide the following information:
1. What is he doing?
2. Tell me two facts about him.
3.what's his name?"""

# Create the prompt template
prompt = PromptTemplate(
    input_variables=["my_prompt"],
    template=template
)

output_parser = StrOutputParser()

# Load Ollama model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Chain the prompt with the model
chain = prompt | llm | output_parser

if __name__ == "__main__":
    #user_input = input("Enter person information: ")
    user_input = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/haribaskar-a-a56045301/")
    result = chain.invoke({"my_prompt": user_input})
    print(result)
