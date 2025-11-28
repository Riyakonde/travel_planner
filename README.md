# Travel Buddy — AI Travel Itinerary Planner

Travel Buddy is an AI-powered travel planning app built with Streamlit and OpenAI.  
It generates detailed itineraries based on your city, trip duration, and interests.  
You can also modify itineraries using natural language and download the final version.

---

## Features

### 1. Generate a Travel Itinerary
Based on:
- City
- Number of days
- User interests

The generated itinerary includes:
- City overview  
- Today’s weather  
- Key attractions  
- Food recommendations  
- Day-by-day detailed plan  

---

### 2. Modify Existing Itinerary
You can update your itinerary simply by typing what you want changed.

Examples:
- "Add more cafes"
- "Remove museums"
- "Include nightlife options"

The assistant will:
- Keep the same structure
- Apply only the requested changes
- Expand details when needed

---

### 3. Download Plan
You can download your itinerary as a plain text file.

---

## Tech Stack

- Python  
- Streamlit  
- LangChain  
- OpenAI API  
- Custom tools:
  - City overview
  - Top places
  - Food recommendations
  - Weather

---

## Setup (API Key Required)

### Local Development

Create a `.env` file:
- Add api keys in env file 

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt

---


## Run the app
streamlit run app.py

 


