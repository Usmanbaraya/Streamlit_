import streamlit as st
import pandas as pd

# we are Initialize the session state for students if it doesn't exist
if 'students' not in st.session_state:
    st.session_state.students = []

# Add Function to add a student
def add_student(name, score):
    st.session_state.students.append({'Name': name, 'Score': score})

# Add Title
st.title("Student Tracker")

# Add fields for student name and score
name = st.text_input("Enter Student Name:")
score = st.number_input("Enter Student Score:", min_value=0)

# Add Button to add student
if st.button("Add Student"):
    if name and score >= 0:  # Ensure valid input
        add_student(name, score)
        st.success(f"Added {name} with score {score}")

# Display the table of students
if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.write("### Student List", df)

    # Add Slider to filter students by minimum score
    min_score = st.slider("Filter by Minimum Score:", 0, 100, 0)
    
    # Filtered DataFrame
    filtered_df = df[df['Score'] >= min_score]
    
    st.write(f"### Students with Score >= {min_score}", filtered_df)
else:
    st.write("No students added yet.")