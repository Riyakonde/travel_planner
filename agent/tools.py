from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests

duckduckgo=DuckDuckGoSearchRun()

@tool
def city_overview(city:str):
    """returns a brief overview of city using duckduckgo search"""
    query=f"give me a brief overview of {city}"
    result=duckduckgo.invoke(query)
    return result

@tool
def top_places(city:str):
    """Returns the top places to visit in a given city."""
    query=f"top famous places to visit in {city}"
    result=duckduckgo.invoke(query)
    return result if result else "no place found"

@tool
def food_recommendations(city:str):
    """returns the best food to try in a given city."""
    query=f"famous food to try in {city}"
    result=duckduckgo.invoke(query)
    return result if result else "no food found"

@tool
def weather(city:str):
    """Fetch today's weather using wttr.in."""
    try:
        url = f"https://wttr.in/{city}?format=%C+%t"
        text = requests.get(url, timeout=6).text.strip()
        return f"Today's weather in {city}: {text}"
    except:
        return "Weather unavailable."


