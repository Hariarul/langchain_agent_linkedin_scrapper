import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor


load_dotenv()

from tools.my_tools import get_profile_url_tavily
import os

def lookup(name:str)->str:

    llm = ChatOpenAI(
        model='gpt-4o-mini',
        temperature = 0
    )

    prompt = """ Given a name {name_of_person} search through google and get the linkeding profile url, only return linkeding url of the particular person"""

    prompt_template = PromptTemplate(input_variables=['name_of_person'], template=prompt)

    tools_for_agent = [
        Tool(
            name="crawl google 4 linkeding profile page",
            func = get_profile_url_tavily,
            description= "useful for when you need to get the linkeding url"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input":prompt_template.format_prompt(name_of_person=name)})

    linkedin_profile_url = result['output']

    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name=input("Enter the name here:"))
    print(linkedin_url)