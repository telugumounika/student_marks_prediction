import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load saved model
# -----------------------------
model = joblib.load("student_marks_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Marks Prediction")
st.write("Predict the student's exam score using Machine Learning.")

st.divider()

# -----------------------------
# User Inputs
# -----------------------------

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

parent = st.selectbox(
    "Parental Involvement",
    ["Low", "Medium", "High"]
)

resource = st.selectbox(
    "Access to Resources",
    ["Low", "Medium", "High"]
)

teacher = st.selectbox(
    "Teacher Quality",
    ["Low", "Medium", "High"]
)

learning = st.selectbox(
    "Learning Disabilities",
    ["No", "Yes"]
)

hours = st.slider(
    "Hours Studied",
    0,
    20,
    5
)

attendance = st.slider(
    "Attendance (%)",
    0,
    100,
    80
)

sleep = st.slider(
    "Sleep Hours",
    0,
    12,
    7
)

previous = st.slider(
    "Previous Scores",
    0,
    100,
    70
)

tutoring = st.slider(
    "Tutoring Sessions",
    0,
    20,
    5
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Marks"):

    categorical = pd.DataFrame({
        "Gender":[gender],
        "Parental_Involvement":[parent],
        "Access_to_Resources":[resource],
        "Teacher_Quality":[teacher],
        "Learning_Disabilities":[learning]
    })

    encoded = encoder.transform(categorical)

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out([
            "Gender",
            "Parental_Involvement",
            "Access_to_Resources",
            "Teacher_Quality",
            "Learning_Disabilities"
        ])
    )

    numeric = pd.DataFrame({
        "Hours_Studied":[hours],
        "Attendance":[attendance],
        "Sleep_Hours":[sleep],
        "Previous_Scores":[previous],
        "Tutoring_Sessions":[tutoring]
    })

    final_df = pd.concat([encoded_df, numeric], axis=1)

    feature_order = [
        'Gender_Male',
        'Parental_Involvement_Low',
        'Parental_Involvement_Medium',
        'Access_to_Resources_Low',
        'Access_to_Resources_Medium',
        'Teacher_Quality_Low',
        'Teacher_Quality_Medium',
        'Learning_Disabilities_Yes',
        'Hours_Studied',
        'Attendance',
        'Sleep_Hours',
        'Previous_Scores',
        'Tutoring_Sessions'
    ]

    final_df = final_df.reindex(columns=feature_order, fill_value=0)

    numeric_cols = [
        'Hours_Studied',
        'Attendance',
        'Sleep_Hours',
        'Previous_Scores',
        'Tutoring_Sessions'
    ]

    final_df[numeric_cols] = scaler.transform(final_df[numeric_cols])

    prediction = model.predict(final_df)[0]

    st.success(f"Predicted Exam Score: **{prediction:.2f} / 100**")

    if prediction >= 90:
        st.balloons()
        st.success("Excellent Performance!")
    elif prediction >= 75:
        st.info("Very Good Performance!")
    elif prediction >= 60:
        st.warning("Average Performance")
    else:
        st.error("Needs Improvement")