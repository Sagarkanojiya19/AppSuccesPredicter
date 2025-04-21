import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("App Success Prediction")

st.markdown("Fill out the APP details below to predict the success of the app")

Category = [
     "None", "ART AND DESIGN", "AUTO AND VEHICLES", "BEAUTY", "BOOKS AND REFERENCE", "BUSINESS", "COMICS",
    "COMMUNICATION", "DATING", "EDUCATION", "ENTERTAINMENT", "EVENTS", "FAMILY", "FINANCE", "FOOD AND DRINK", "GAME",
    "HEALTH AND FITNESS", "HOUSE AND HOME", "LIBRARIES AND DEMO", "LIFESTYLE", "MAPS AND NAVIGATION",
    "MEDICAL", "NEWS AND MAGAZINES", "PARENTING", "PERSONALIZATION", "PHOTOGRAPHY", "PRODUCTIVITY",
    "SHOPPING", "SOCIAL", "SPORTS", "TOOLS", "TRAVEL AND LOCAL", "VIDEO PLAYERS", "WEATHER"
]

Genres= [
    "None", "Action", "Adventure","Action & Adventure","Arcade", "Art & Design", "Auto & Vehicles", "Beauty", "Board",
    "Books & Reference","Brain Games","Business", "Card", "Casino", "Casual", "Comics", "Communication",
    "Dating", "Education", "Entertainment", "Events", "Finance", "Food & Drink", "Health & Fitness",
    "House & Home", "Libraries & Demo", "Lifestyle", "Maps & Navigation", "Medical", "Music","Music & Video",
    "News & Magazines", "Parenting", "Personalization", "Photography", "Pretend Play","Productivity",
    "Puzzle", "Racing", "Role Playing", "Shopping", "Simulation", "Social", "Sports", "Strategy",
    "Tools", "Travel & Local", "Trivia", "Video Players", "Weather", "Word"
]

Category  = st.selectbox("App Category",Category,index= 0)
Rating = st.number_input("Rating (0.0 to 5.0)", min_value=0.0, max_value=5.0, step=0.1, format="%.1f")
Reviews = st.number_input("Number of Reviews", min_value=1, step=100)
Installs = st.number_input("Number of Installs", min_value=1, step=1000)
Type = st.selectbox("App Type", ["Free", "Paid"])
Content_Rating = st.selectbox("Content Rating", ["Everyone", "Teen", "Mature 17+"])
Genre = st.selectbox("Genre",Genres, index = 0)

input_df = pd.DataFrame([{
    'Category': Category,
    'Rating': Rating,
    'Reviews': Reviews,
    'Installs': Installs,
    'Type': Type,
    'Content Rating': Content_Rating,
    'Genres': Genre
}])


# --- Prediction ---
if Category == "None":
    st.warning("Please select a valid App Category.")
elif Genre == "None":
    st.warning("Please select a valid App Genre.")
elif st.button("Predict Success"):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][prediction]
    label = "✅ Successful" if prediction == 1 else "❌ Unsuccessful"
    st.success(f"Prediction: {label}")