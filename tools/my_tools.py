from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
import os

def get_profile_url_tavily(name:str):
    """searches for linkedin or twitter profile page"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res