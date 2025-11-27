import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from agent.tools import city_overview, top_places, food_recommendations, weather

llm=ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.4,
    api_key=OPENAI_API_KEY
)

googel_llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    api_key=GEMINI_API_KEY
)

system_prompt="""
You are smart travel agent.You are going to help user to plan there travel iternary based on 
there city of travel,number of days and interests of user.
Rules to follow:
- Use tools ONLY when needed (web_search, weather,food_).
- Your toolkit:
    - city_overview: Gives a high-level overview of a city.
    - top_places: Returns top tourist attractions.
    - food_recommendations: Lists famous foods in a city.
    - weather: Returns today's weather. 
- Always label weather as “today's weather”.
- After using tools, expand the results into a helpful travel plan.
- Create clean, structured outputs including:
   - A clear city overview
   - Today's weather section
   - Top attractions
   - Local food recommendations
   - A detailed itinerary based on the user's trip duration and interests
   - Morning / Afternoon / Evening activities
   - Recommended neighborhoods
   - Cultural highlights

- When modifying an existing itinerary:
   - Preserve the structure and formatting
   - Apply only the requested changes
   - Improve clarity and usefulness when needed
- Never fabricate tool output—only expand and explain it.
- Even if tool results are short, expand using your own reasoning.
- Keep formatting clean with bullet points and bold titles.
"""

travel_agent=create_agent(
    model=llm,
    tools=[city_overview, top_places, food_recommendations, weather],
    system_prompt=system_prompt,

)

def plan_trip(city:str,days:int,interests:str):
    """create a full travel iternary based on city,days and interests of user"""
    user_msg=(
        f"I am planning a trip to {city} for {days} days. "
        f"My interest are:{interests}"
        "give me a detailed travel iternary with sections for overview, weather, attractions, food, and day-by-day plan."

    )

    result=travel_agent.invoke({ "messages": [ {"role":"user","content":user_msg} ] })

    return result["messages"][-1].content

# def modify_iternary(existing_iternary:str,modification_request:str):
#     """modify an existing travel iternary based on user request"""
#     result=travel_agent.invoke({
#         "messages":[
#             {"role":"system","content":"Modify the existing iternary according to user request.Keep foramt clean and detailed"},
#             {"role":"user","content":f"Here is the existing iternary:\n{existing_iternary}"},
#             {"role": "user", "content": f"Please modify it in this way:\n{modification_request}"}

#         ]
#     }

#      )
    
#     return result["messages"][-1].content

def modify_itinerary(existing_plan: str, request: str):
    """
    Modify an existing itinerary.
    """
    modify_prompt = f"""

    You are a travel itinerary modification assistant.

    The user already has an itinerary. You MUST:
    - Read the existing itinerary carefully
    - Apply ONLY the requested changes
    - Keep the same style, structure, format
    - Expand or adjust activities according to the request
    - Do NOT repeat the same itinerary unless it naturally matches the request
    - Do NOT shorten the plan
    - Do NOT remove useful details unless requested
    - Include new attractions, foods, and neighborhoods if needed
    **Keep the structure and formatting the same.**

    USER REQUEST:
    {request}

    EXISTING ITINERARY:
    {existing_plan}

    Now produce the updated itinerary ONLY.
    """

    result = travel_agent.invoke({
        "messages": [{"role": "user", "content": modify_prompt}]
    })

    return result["messages"][-1].content
