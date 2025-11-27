import streamlit as st
from dotenv import load_dotenv

import os

load_dotenv()

st.sidebar.title("🔑 API Keys")

openai_key_input = st.sidebar.text_input(
    "Enter OpenAI API Key",
    type="password",
    placeholder="sk-xxxxxxxx"
)
if openai_key_input:
    os.environ["OPENAI_API_KEY"] = openai_key_input
if not os.getenv("OPENAI_API_KEY"):
    st.warning("Please enter your OpenAI API Key in the sidebar to continue.")
    st.stop()

from agent.travel_agent import plan_trip, modify_itinerary
from agent.clean import strip_markdown


st.title("🧳 Travel Buddy")
st.write("---")
st.header("Create your own itinerary")


if "plan" not in st.session_state:
    st.session_state["plan"] = None


 

# Trip creation form
with st.form("trip_form"):
    city = st.text_input("✈️ Enter the city you plan to visit:")
    days = st.number_input("🗓 Trip duration (in days):", min_value=1, max_value=30, value=3)
    interests = st.text_input("Your interests (comma separated):")

    submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        try:
            with st.spinner("Planning your trip..."):
                result = plan_trip(city, days, interests)
            st.session_state["plan"] = result

            st.subheader("Your Travel Itinerary:")
            st.write(result)
        except Exception:
            st.error("⚠️ Unable to generate itinerary. Please try again.")

# Only show modification section if an itinerary exists
st.write("---")

if "plan" in st.session_state:
    st.header("Modify your existing trip plan")

    modified_input = st.text_input("Enter your modification request:")

    if st.button("Modify Itinerary"):
        try:
            with st.spinner("Updating your plan..."):
                updated_plan = modify_itinerary(st.session_state["plan"], modified_input)

            st.session_state["plan"] = updated_plan
    

            st.subheader("📝 Updated Travel Itinerary:")
            st.markdown(updated_plan)

        except Exception:
            st.error("⚠️ Unable to modify itinerary. Try simplifying your request.")


if st.session_state["plan"]:
    st.header("📥 Download Your Itinerary")
    clean_text = strip_markdown(st.session_state["plan"])

    st.download_button(
        label="Download Itinerary as Text File",
        data=clean_text,
        file_name="travel_itinerary.txt",
        mime="text/plain"
    )


