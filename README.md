# Student Marks Prediction using Machine Learning

## Project Overview

This project predicts a student's exam marks based on various academic and personal factors using Machine Learning.

The application is developed using **Python**, **Scikit-learn**, and **Streamlit** to provide an interactive web interface for users.

---

## Project Structure

```
Student_Marks_Prediction/
│
├── app.py
├── student_marks_model.pkl
├── encoder.pkl
├── scaler.pkl
├── StudentPerformanceFactors.csv
├── requirements.txt
├── README.md
└── Untitled-1.ipynb
```

---

## Features

- Predict student exam marks
- Interactive Streamlit web interface
- Machine Learning-based prediction
- Easy-to-use input form
- Instant prediction results

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## Dataset

The dataset contains student-related information such as:

- Gender
- Hours Studied
- Attendance
- Previous Scores
- Sleep Hours
- Tutoring Sessions
- Teacher Quality
- Parental Involvement
- Access to Resources
- Learning Disabilities

Target Variable:

- Exam Score

---

## Machine Learning Model

The project uses the following preprocessing techniques:

- One-Hot Encoding
- Standard Scaling

Model Used:

- Random Forest Regressor

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/student-marks-prediction.git
```

Move to the project directory:

```bash
cd student-marks-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## Application Workflow

1. Enter student details.
2. Click **Predict Marks**.
3. The model predicts the expected exam score.
4. The predicted score is displayed instantly.

---

## Future Enhancements

- Student performance dashboard
- Graphical data visualization
- Prediction history
- PDF report generation
- Deployment on Streamlit Community Cloud

---

## Author

**Mounika Ramya**

Student | Machine Learning Enthusiast

---

## License

This project is developed for educational purposes.
