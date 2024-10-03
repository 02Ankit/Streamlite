import streamlit as st
import random

# Define sample exercises and meals
exercises = {
    "upper_body": ["Bench Press", "Pull-ups", "Shoulder Press", "Push-ups", "Chest Fly"],
    "lower_body": ["Squats", "Deadlifts", "Lunges", "Leg Press", "Leg Curls"],
    "full_body": ["Burpees", "Mountain Climbers", "Kettlebell Swings", "Jumping Jacks"],
}

meals = {
    "Vegan": [
        {"meal": "Breakfast", "food": "Oatmeal with almond milk and berries"},
        {"meal": "Lunch", "food": "Quinoa salad with chickpeas and avocado"},
        {"meal": "Dinner", "food": "Grilled tofu with steamed vegetables"},
    ],
    "Vegetarian": [
        {"meal": "Breakfast", "food": "Greek yogurt with granola"},
        {"meal": "Lunch", "food": "Lentil curry with brown rice"},
        {"meal": "Dinner", "food": "Paneer stir-fry with quinoa"},
    ],
    "Keto": [
        {"meal": "Breakfast", "food": "Eggs with avocado"},
        {"meal": "Lunch", "food": "Grilled chicken with spinach and cheese"},
        {"meal": "Dinner", "food": "Salmon with broccoli"},
    ],
    "Non-Vegetarian": [
        {"meal": "Breakfast", "food": "Scrambled eggs with spinach and turkey sausage"},
        {"meal": "Lunch", "food": "Chicken breast with sweet potato and broccoli"},
        {"meal": "Dinner", "food": "Grilled steak with asparagus and quinoa"},
    ],
}

# Function to randomly generate a workout plan for a specific day
def generate_random_workout_plan(fitness_goal):
    if fitness_goal == "Muscle Building":
        workout_plan = random.sample(exercises["upper_body"], 2) + random.sample(exercises["lower_body"], 1)
    elif fitness_goal == "Strength":
        workout_plan = random.sample(exercises["lower_body"], 2) + random.sample(exercises["full_body"], 1)
    else:  # Weight Loss
        workout_plan = random.sample(exercises["full_body"], 3)
    
    # Randomize sets and reps based on fitness goal
    sets_reps = []
    for exercise in workout_plan:
        if fitness_goal == "Muscle Building":
            sets_reps.append({"exercise": exercise, "sets": random.randint(3, 5), "reps": random.randint(8, 12)})
        elif fitness_goal == "Strength":
            sets_reps.append({"exercise": exercise, "sets": random.randint(4, 5), "reps": random.randint(4, 6)})
        else:  # Weight Loss
            sets_reps.append({"exercise": exercise, "sets": random.randint(2, 3), "reps": random.randint(12, 15)})
    
    return sets_reps

# Function to randomly generate a daily diet plan for a specific day
def generate_random_diet_plan(dietary_preference):
    return random.sample(meals[dietary_preference], 3)

# Streamlit app layout with compact UI
st.title("Randomized Weekly Workout and Diet Plan Simulation")

# Compact input layout using columns
col1, col2, col3, col4 = st.columns(4)

# Input fields for personal information
with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
with col2:
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
with col3:
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
with col4:
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)

# More compact input layout for fitness and diet goals
col5, col6 = st.columns(2)

with col5:
    experience_level = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
with col6:
    fitness_goal = st.selectbox("Fitness Goal", ["Muscle Building", "Strength", "Weight Loss"])

dietary_preference = st.selectbox("Dietary Preference", ["Vegan", "Vegetarian", "Keto", "Non-Vegetarian"])

# Button to generate weekly plan
if st.button("Generate Weekly Plan"):
    days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    
    # Create tabs for each day of the week
    tabs = st.tabs([f"{day}" for day in days])
    
    for i, tab in enumerate(tabs):
        day = days[i]
        with tab:
            # Display randomized workout plan for the day
            st.subheader(f"{day} Workout Plan")
            workout_plan = generate_random_workout_plan(fitness_goal)
            for exercise in workout_plan:
                st.write(f"{exercise['exercise']}: {exercise['sets']} sets of {exercise['reps']} reps")
            
            # Display randomized diet plan for the day
            st.subheader(f"{day} Diet Plan")
            diet_plan = generate_random_diet_plan(dietary_preference)
            for meal in diet_plan:
                st.write(f"{meal['meal']}: {meal['food']}")
    
    # Display user profile information
    st.subheader("User Profile Information")
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"Gender: {gender}")
        st.write(f"Age: {age}")
    with col8:
        st.write(f"Weight: {weight} kg")
        st.write(f"Height: {height} cm")