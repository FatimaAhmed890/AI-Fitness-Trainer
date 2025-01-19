import streamlit as st

st.set_page_config(
    page_title="AI_Fitness_Trainer",
    page_icon="💪🏻"
)

st.image('../assets/app.png', width=630)
st.title("Welcome to AI Fitness 💪🏻 Trainer")
st.sidebar.success("Select a page above")

st.markdown("""
## Smart Posture Guidance for Effective Workouts

Our innovative AI-powered fitness app enhances your home workouts by providing real-time posture correction and injury prevention. Leveraging advanced machine learning algorithms, our app helps users maintain proper form during exercises, ensuring safer and more effective workouts.

How it works:

    Users select an exercise from our library.
    The app uses AI to analyze the user's posture in real-time.
    Instant feedback is provided through visual indicators.
    Users receive guidance to adjust their form for optimal performance and safety.

Benefits:

    Reduce risk of injury from improper form
    Improve overall workout efficiency
    Enhance muscle engagement and exercise effectiveness
    Learn proper form through guided corrections
    Enjoy workouts safely at home

Our AI fitness trainer empowers users to get the most out of their home workouts while maintaining proper form and minimizing injury risk. Whether you're a fitness enthusiast or just starting your exercise journey, our app provides personalized guidance to help you achieve your goals safely and effectively.

By focusing on posture correction and injury prevention, this app addresses a critical need in at-home fitness, helping users perform exercises correctly and avoid common pitfalls associated with improper form.
            """)